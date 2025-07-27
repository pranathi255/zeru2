Compound Wallet Risk Scoring

This project assigns a risk score (0–1000) to 100 Ethereum wallet addresses based on their historical activity on the Compound V2 and V3 protocols. It uses on-chain data to evaluate how safely or aggressively each wallet interacts with lending and borrowing.

Project Structure

compound-risk-score/
├── scores.py 
├── wallet_scores.csv
├── README.md 
└── analysis.md

 How It Works

1. Input: A list of 100 wallet addresses in wallets.csv.
2. Data Fetching: For each wallet, the script fetches Compound protocol activity using the [GoldRush API](https://goldrush.dev/platform).
3. Feature Extraction: Metrics like `total_supplied`, `total_borrowed`, and `borrow/supply ratio` are calculated.
4. Scoring: A score between 0 and 1000 is computed for each wallet based on risk factors.
5. Output: The scores are saved in `scores.csv`.

Score Interpretation
Score Range	Risk Level	Meaning
900–1000🟢 Very Low Risk	Only supplies to Compound
800–900	🟢 Low Risk	Supplies actively, does not borrow
700–800	🟡 Medium Risk	Moderate borrowing, well-collateralized
500–700	🟠 High Risk	Borrowing close to supplied amount
200–500	🔴 Very High Risk	Aggressively borrowing relative to supply
0–200	⚫ Unknown/Empty	No meaningful Compound activity found