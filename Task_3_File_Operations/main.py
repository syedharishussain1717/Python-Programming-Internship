# Name: Syed Haris Hussain Shah
# Internship ID: B9_2265
import os
import shutil

# Define folder paths
data_folder = "data"
organized_folder = "organized"

# Scan all files inside the data folder
files = os.listdir(data_folder)

# Process each file
for file in files:

    # Get file extension
    extension = os.path.splitext(file)[1].lower()

    # Remove the dot from extension
    extension = extension.replace(".", "")

    # Create destination folder
    destination_folder = os.path.join(organized_folder, extension)

    # Create folder if it doesn't exist
    os.makedirs(destination_folder, exist_ok=True)

    # Define source and destination paths
    source_path = os.path.join(data_folder, file)
    destination_path = os.path.join(destination_folder, file)

    # Move file to its respective folder
    shutil.move(source_path, destination_path)

    print(f"Moved {file} to {destination_folder}")

print("\nFile organization completed successfully!")
