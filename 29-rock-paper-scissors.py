import random 

options = ("rock", "paper", "scissors")
player = None

win = 0
loose = 0
tie = 0

is_running = True

while is_running:
  computer = random.choice(options)
  player = input("Enter a choice (rock,paper,scissors): ")

  while player not in options:
    player = input("Enter a choice (rock,paper,scissors): ")

  print(f"Computer picked: {computer}")
  print(f"You picked: {player}")

  if player == computer:
    print("It's a tie")
    tie+= 1 
  elif player == "rock" and computer == "scissors":
    print("You win!")
    win+= 1
  elif player == "paper" and computer == "rock":
    print("You win!")
    win+= 1
  elif player == "scissors" and computer == "paper":
    print("You win!")
    win+= 1
  else:
    print("You lose!")
    loose+= 1
  
  print(f"wins: {win} looses: {loose} ties: {tie}")
  

  play_again = input("play again? (y/n) :").lower()

  if not play_again == "y":
    is_running = False

print("Thanks for playing")
  
