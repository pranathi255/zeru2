import pandas as pd
import random

print("Processing started...")

# Step 1: Read wallet IDs from file
with open("wallet.txt", "r") as f:
    wallet_ids = [line.strip().lower() for line in f if line.strip().startswith("0x")]

# Step 2: Generate scores (replace this with real scoring logic)
wallet_scores = [{"wallet_id": wallet, "score": random.randint(300, 950)} for wallet in wallet_ids]

# Step 3: Save to CSV
df = pd.DataFrame(wallet_scores)
df.to_csv("wallet_scores.csv", index=False)

print("✅ Done! Output saved to wallet_scores.csv")
