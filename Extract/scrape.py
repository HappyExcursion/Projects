import yaml
import json
from bs4 import BeautifulSoup

# Function to read and parse the HTML of a local file


def read_and_parse_file(file_path):
    with open(file_path, 'r') as file:
        contents = file.read()
    soup = BeautifulSoup(contents, 'html.parser')
    return soup


# List of file paths
# Update this list with your actual file paths
file_paths = ["page1.html", "page2.html", "page3.html"]

# List to store the scraped data
Titles = []
Links = []
Nums = []
Num = 1

# Loop over the files
for file_path in file_paths:
    # Read and parse the file
    soup = read_and_parse_file(file_path)

    # Extract the data from the list items
    items = soup.select(
        'body > div.container.main-container > main > div > div.l-main-content.l-centered.ng-scope > div > ul.recommended-list > li')

    for item in items:
        # Extract the data from the individual item
        element = item.select_one('div > div.recommended-info > a')
        if element is not None:
            data = element.get('title')
            link = element.get('href')
            if data is not None and data.strip() not in Titles:
                # Append the data to the list
                Titles.append(data.strip())
                Links.append("https://inplace.qut.edu.au" + link.strip())
                Nums.append(Num)
                Num += 1


# Print the scraped data
# for title, link in zip(Titles, Links):
#     print(title, "\n", link)

# Export to JSON
# Create a list to hold the dictionaries
data_list = []

# Loop through the titles and links and create a dictionary for each pair
for title, link, num in zip(Titles, Links, Nums):
    # Initialize an empty comments list
    comments = [
        {"James ": "", "Xavier": "", "Chelsey ": "", "Ryan": ""}
    ]

    data_dict = {"Num": num, "Title": title, "Link": link, "Location": "", "Summary": "", "Preference": "",
                 "Comments": comments}
    data_list.append(data_dict)

# Write the list of dictionaries to a JSON file
with open("projects.json", "w") as file:
    json.dump(data_list, file, indent=4)


# create a YAML version
# Create a list to hold the dictionaries
data_list = []

# Loop through the titles and links and create a dictionary for each pair
for title, link, num in zip(Titles, Links, Nums):
    # Initialize an empty comments list
    comments = [
        {"Attribute1": "", "Attribute2": "", "Attribute3": "", "Attribute4": ""}
    ]

    data_dict = {"Num": num, "Title": title,
                 "Link": link, "Comments": comments}
    data_list.append(data_dict)

# Write the list of dictionaries to a YAML file
with open("projects.yaml", "w") as file:
    yaml.dump(data_list, file)
