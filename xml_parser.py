import os
from bs4 import BeautifulSoup as bs

# File to parse
source = "sma_gentext.xml"

# We want to find
parent_element = "trans-unit"
child_element = "target"
attr = {"id": "42007"}

# Get source and create a BeautifulSoup object
with open(source, "r") as file:
    soup = bs(file, "xml")

element_found = soup.find(parent_element, attr)

if element_found:
    with open(f"{list(attr.keys())[0]}_{attr['id']}_{child_element}.txt", "w") as file:
        file.write(element_found.find(child_element).text)
        print("File saved successfully.")
else:
    print(f"Failed to save file: No {parent_element} with attributes {attr} found.")