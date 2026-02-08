# Python reading files (.txt, .json, .csv)

import json

file_path = "C:/Users/asus/Desktop/output2.json"

try: 
  with open(file_path, "r") as file:
    content = json.load(file)
    print(content["name"])
except FileNotFoundError:
  print("That file was not found")
except PermissionError:
  print("You don't have permission to read that file") 