# Python file detection

import os

file_path = "Exercises/Exercise1.py"

if os.path.exists(file_path):
  print(f"The location {file_path} exists")

  if os.path.isfile(file_path):
    print(f"The location is a file'")
  elif os.path.isdir(file_path):
    print(f"The location is a directory'")
else:
  print("That location doesn't exist")