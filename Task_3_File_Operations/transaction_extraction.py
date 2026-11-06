
import os
import re

# Define the log file path
log_file = os.path.join("organized", "log", "transactions.log")

# Read the transaction log
with open(log_file, "r") as file:
    content = file.read()

# Extract transaction IDs and amounts
pattern = r"Transaction ID:\s*(TXN\d+)\s+Amount:\s*(\d+)"

transactions = re.findall(pattern, content)

# Display extracted information
print("Extracted Transactions:\n")

for transaction_id, amount in transactions:
    print(f"Transaction ID: {transaction_id} | Amount: {amount}")
