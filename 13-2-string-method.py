# Valid user input exercise 
#1. username is no more than 12 characters
#2. username must not contain spaces
#3. username must mot contain digits

username = input("Enter a username: ")

if len(username) > 12 :
  print("user name must be less than 12 characters")

elif(not username.find(" ") == -1):
  print("user name must not contains spaces")

elif(not username.isalpha()):
  print("user name must not contains digits")
  
else: 
  print(f"Welcome {username}")

