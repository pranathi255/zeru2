import requests
import pandas as pd
import time

API_KEY = "cqt_rQD8YK73H3qhqGYCPKt9mHktvBJg"
BASE = "https://api.goldrush.dev/v1/wallet"

df = pd.read_csv("wallet_scores.csv")
results = []
print("Script started")

for wallet in df['wallet_id'].str.strip().str.lower():
    print("Fetching", wallet)
    url = f"{BASE}/{wallet}/compound"
    headers = {"accept": "application/json", "x-api-key": API_KEY}

    try:
        resp = requests.get(url, headers=headers)
        if resp.status_code == 200:
            j = resp.json()
            total_sup = j.get("total_supply_usd", 0) or 0
            total_bor = j.get("total_borrow_usd", 0) or 0
            util = (total_bor / total_sup) if total_sup > 0 else 1.0
            score = max(0, min(1000, int((1 - util) * 1000)))
        else:
            print("API error", resp.status_code, resp.text)
            score = 0
    except Exception as e:
        print("Exception:", e)
        score = 0

    results.append({"wallet_id": wallet, "score": score})
    time.sleep(0.5)

pd.DataFrame(results).to_csv("output.csv", index=False)
print("Done — output.csv created")
