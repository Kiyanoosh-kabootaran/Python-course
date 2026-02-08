#Python writing files (.txt, .json, .csv)
#.json

import json

employee = {
  "name": "Spongebob",
  "age": 30,
  "job": "cook"
}

file_path = "C:/Users/asus/Desktop/output2.json"

try:
  with open(file=file_path, mode="w") as file:
    json.dump(employee, file, indent=4)
    print(f"jsobn file '{file_path}' was created")
except FileExistsError:
  print("That file already exists!")