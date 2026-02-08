# Python reading files (.txt, .json, .csv)

file_path = "C:/Users/asus/Desktop/output1.txt"

try: 
  with open(file_path, "r") as file:
    content = file.read()
    print(content)
except FileNotFoundError:
  print("That file was not found")
except PermissionError:
  print("You don't have permission to read that file") 