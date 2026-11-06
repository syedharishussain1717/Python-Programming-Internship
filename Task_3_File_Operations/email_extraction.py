
import os
import re

# Define file paths
contacts_file = os.path.join("organized", "txt", "contacts.txt")

# Read contacts file
with open(contacts_file, "r") as file:
    content = file.read()

# Extract email addresses
emails = re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', content)

print("Extracted Email Addresses:")

for email in emails:
    print(email)
