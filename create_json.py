import os
import json
import parse_report

# Create an empty dictionary to store the data
data = {}

# Get a list of all the files in the directory
for filename in os.listdir():
    # Check if the file is an HTML file
    if filename.endswith(".html") or filename.endswith("htm"):
        # Open the file
        with open(filename, "rb") as file:
            # Read the contents of the file
            contents = parse_report.clean(file.read())
            # Add the contents to the dictionary with the filename as the key
            data[filename] = contents

# Write the dictionary to a JSON file
with open("data.json", "w") as file:
    json.dump(data, file)
