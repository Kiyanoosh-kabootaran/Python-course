#Python writing files (.txt, .json, .csv)
# .txt

employees = ["Eugene" , "Squidward", "Spongebob", "Patrick"]

file_path = "C:/Users/asus/Desktop/output1.txt"

# mode = "a" will append data
try:
  with open(file=file_path, mode="w") as file:
    for employee in employees:
      file.write(employee + "\n")
    print(f"txt file '{file_path}' was created")
except FileExistsError:
  print("That file already exists!")