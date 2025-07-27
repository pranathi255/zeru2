Analysis: Compound Wallet Risk Scoring

This document explains the rationale behind data collection, feature selection, scoring method, and the indicators used to assess wallet risk for the Compound protocol.

Data Collection Method

I used the GoldRush API to collect on-chain data for 100 Ethereum wallet addresses. The process involved:
- Extracting all Compound V2 and V3 transaction events for each wallet.
- Aggregating historical lending and borrowing actions at the wallet level.
- Calculating total supplied and total borrowed amounts per wallet.


Feature Selection Rationale

To evaluate the risk profile of each wallet, we engineered the following features:

- Total Supplied: Sum of all assets supplied to Compound by a wallet.
- Total Borrowed: Sum of all assets borrowed.
- Borrow/Supply Ratio: Indicates leverage level.
- Borrow Count & Supply Count: Measures activity patterns.


Scoring Method

Each wallet was assigned a score between 0 and 1000, based on a heuristic function:

if only_supplied:
score = 900–1000
elif supplied > 0 and borrowed == 0:
score = 800–900
elif borrowed/supplied ≤ 0.5:
score = 700–800
elif 0.5 < borrowed/supplied ≤ 1.0:
score = 500–700
elif borrowed/supplied > 1.0:
score = 200–500
else:
score = 0–200



 Justification of Risk Indicators Used

- Only Supplying→ low protocol risk (no debt taken), hence high score.
- Moderate Borrowing → implies well-collateralized use of the protocol, thus medium score.
- High Borrow-to-Supply Ratio → indicates aggressive leverage, more likely to face liquidation risk, hence lower score.
- No Activity→ not enough signal to trust, so lowest score bucket (0–200).





