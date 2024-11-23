#!/usr/bin/python3

import json

with open('../../DS2022/labs/data/schacon.repos.json', 'r') as file:
    data = json.load(file)
    i = 0
    with open('chacon.csv', 'w') as csv_file:
        while i < 5:
            name = data[i]["name"]
            html_url = data[i]["html_url"]
            updated_at = data[i]["updated_at"]
            visibility = data[i]["visibility"]
            csv_line = f"{name},{html_url},{updated_at},{visibility}\n"
            csv_file.write(csv_line)
            i += 1

with open('chacon.csv', 'r') as chacon:
    contents = chacon.read()

print(contents)
