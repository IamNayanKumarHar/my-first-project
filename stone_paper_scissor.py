import random

'''
0 for stone 
1 for paper
2 for scissors
'''

User_name = input("Plaease enter your name here: ")
print("Welcome to the game", User_name)

play_or_not = input("Do you want to play the game? (y/n): ")
if play_or_not.lower() == "y":
  print("Let's start the game")
elif play_or_not.lower() == "n":
  print("Thank you for visiting")
  exit()
else:
  print("Please enter a valid input")


play_time = int(input("How many times do you want to play? "))

win = 0
lose = 0

for i in range(play_time):


# input for the user

  player = input("Enter s for stone, p for paper, and c for scissors: ")
  player_dict = {"s" : 0, "p" : 1, "c" : 2}
  player = player_dict[player]

# printing the user input

  if player == 0:
    print("You chose stone")

  elif player == 1:
    print("You chose paper")

  elif player == 2:
    print("You chose scissors")

  else:
    print("Please enter a vaild input")

# input fo the computer
  computer = random.randint(0, 2)

# printing the computer input

  if computer == 0:
    print("Computer chose stone")

  if computer == 1:
    print("Computer chose paper")

  if computer == 2:
    print("Computer chose scissors")

# logic

  if player == computer:
    print("Draw")
    

  elif player == 0 and computer == 1:
    print("Computer wins")
    lose += 1

  elif player == 0 and computer == 2:
    print("Player wins")
    win += 1

  elif player == 1 and computer == 2:
    print("Computer wins")
    lose += 1

  elif player == 1 and computer == 0:
    print("Player wins")
    win += 1

  elif player == 2 and computer == 1:
    print("Player wins")
    win += 1

  elif player == 2 and computer == 0:
    print("Computer wins")
    lose += 1

  else:
    print("Invalid input")

  print(f"Score board: {User_name}: {win} | Computer: {lose}")

if win > lose:
  print("Congratulations! You won the game")

elif win<lose:
  print("Sorry! You lost the game")

elif win == lose:
  print("The game is a draw")
