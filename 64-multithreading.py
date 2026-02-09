# multithreading = Used to perform multiple tasks concurrently (myltitasking)
#                  Good for I/O bound tasks like reading files or fetching data from APIs
#                  threading.Thread(target=my_function)

import threading
import time 

def walk_dog():
  time.sleep(8)
  print("You finished walking the dog") 

def get_mail():
  time.sleep(4)
  print("You get the mail")

def take_out_trash():
  time.sleep(2)
  print("You take out the trash")

chore1 = threading.Thread(target=walk_dog)
chore2 = threading.Thread(target=get_mail)
chore3 = threading.Thread(target=take_out_trash)

chore1.start()
chore2.start()
chore3.start()
