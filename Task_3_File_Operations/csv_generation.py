
import os
import re
import csv

try:
    # Define file paths
    contacts_file = os.path.join("organized", "txt", "contacts.txt")
    log_file = os.path.join("organized", "log", "transactions.log")

    # Check whether files exist
    if not os.path.isfile(contacts_file):
        raise FileNotFoundError("Contacts file not found!")

    if not os.path.isfile(log_file):
        raise FileNotFoundError("Transaction log not found!")

    # Extract emails
    with open(contacts_file, "r", encoding="utf-8") as file:
        emails = re.findall(
            r'[\w\.-]+@[\w\.-]+\.\w+',
            file.read()
        )

    # Extract transactions
    with open(log_file, "r", encoding="utf-8") as file:
        content = file.read()

    pattern = r"Transaction ID:\s*(TXN\d+)\s+Amount:\s*(\d+)"
    transactions = re.findall(pattern, content)

    # Generate CSV
    with open("extracted_data.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow(["Type", "Email", "Transaction ID", "Amount"])

        for email in emails:
            writer.writerow(["Contact", email, "", ""])

        for transaction_id, amount in transactions:
            writer.writerow(["Transaction", "", transaction_id, amount])

    print("CSV report generated successfully!")

except FileNotFoundError as error:
    print(f"File Error: {error}")

except PermissionError:
    print("Error: Permission denied while accessing a file.")

except OSError as error:
    print(f"Operating System Error: {error}")
