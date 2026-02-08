# Python reading files (.txt, .json, .csv)

import csv

file_path = "C:/Users/asus/Desktop/output3.csv"

try: 
  with open(file_path, "r") as file:
    content = csv.reader(file)
    for line in content:
      print(line)

except FileNotFoundError:
  print("That file was not found")
except PermissionError:
  print("You don't have permission to read that file") 