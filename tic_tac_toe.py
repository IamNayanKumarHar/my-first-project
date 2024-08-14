import time

import random

computerChoice = []


def generate_random_excluding(min_num, max_num, exclusions):

  possible_numbers = [
      num for num in range(min_num, max_num + 1) if num not in exclusions
  ]

  if not possible_numbers:
    raise ValueError(
        "No possible numbers to choose from, all numbers are excluded.")

  return random.choice(possible_numbers)


# Defining the range of computer generated number

min_num = 1
max_num = 9


def computer_generated_number():

  while True:
    try:
      combined_input = computerChoice + playerChoice
      excluding = [int(num) for num in combined_input]
      random_number = generate_random_excluding(min_num, max_num, excluding)
      # print(f"Random number generated : {random_number}")
      computerChoice.append(random_number)

    except ValueError as e:
      print(e)

    break


# Defining the board


def printBoardWithNumbers():
  print(" ")
  print(" 1 | 2 | 3 ")
  print("---|---|---")
  print(" 4 | 5 | 6 ")
  print("---|---|---")
  print(" 7 | 8 | 9 ")
  print(" ")


# defining the board where the user will see while playing the game
def printBoardWithoutNumbersBeforeTheFirstInput():
  print(" ")
  print("   |   |   ")
  print("---|---|---")
  print("   |   |   ")
  print("---|---|---")
  print("   |   |   ")
  print(" ")


def printBoardWithoutNumbersAfterTheFirstInput():
  one = "X" if 1 in playerChoice else ("O" if 1 in computerChoice else " ")
  two = "X" if 2 in playerChoice else ("O" if 2 in computerChoice else " ")
  three = "X" if 3 in playerChoice else ("O" if 3 in computerChoice else " ")
  four = "X" if 4 in playerChoice else ("O" if 4 in computerChoice else " ")
  five = "X" if 5 in playerChoice else ("O" if 5 in computerChoice else " ")
  six = "X" if 6 in playerChoice else ("O" if 6 in computerChoice else " ")
  seven = "X" if 7 in playerChoice else ("O" if 7 in computerChoice else " ")
  eight = "X" if 8 in playerChoice else ("O" if 8 in computerChoice else " ")
  nine = "X" if 9 in playerChoice else ("O" if 9 in computerChoice else " ")
  print(" ")
  print(f" {one} | {two} | {three} ")
  print("---|---|---")
  print(f" {four} | {five} | {six} ")
  print("---|---|---")
  print(f" {seven} | {eight} | {nine} ")
  print(" ")


# check if the user won
def check_win(playerChoice):
  if 1 in playerChoice and 2 in playerChoice and 3 in playerChoice:
    return True

  elif 4 in playerChoice and 5 in playerChoice and 6 in playerChoice:
    return True

  elif 7 in playerChoice and 8 in playerChoice and 9 in playerChoice:
    return True

  elif 1 in playerChoice and 4 in playerChoice and 7 in playerChoice:
    return True

  elif 2 in playerChoice and 5 in playerChoice and 8 in playerChoice:
    return True

  elif 3 in playerChoice and 6 in playerChoice and 9 in playerChoice:
    return True

  elif 1 in playerChoice and 5 in playerChoice and 9 in playerChoice:
    return True

  elif 3 in playerChoice and 5 in playerChoice and 7 in playerChoice:
    return True


# check if the user loos
def check_lose(computerChoice):
  if 1 in computerChoice and 2 in computerChoice and 3 in computerChoice:
    return True

  elif 4 in computerChoice and 5 in computerChoice and 6 in computerChoice:
    return True

  elif 7 in computerChoice and 8 in computerChoice and 9 in computerChoice:
    return True

  elif 1 in computerChoice and 4 in computerChoice and 7 in computerChoice:
    return True

  elif 2 in computerChoice and 5 in computerChoice and 8 in computerChoice:
    return True

  elif 3 in computerChoice and 6 in computerChoice and 9 in computerChoice:
    return True

  elif 1 in computerChoice and 5 in computerChoice and 9 in computerChoice:
    return True

  elif 3 in computerChoice and 5 in computerChoice and 7 in computerChoice:
    return True


# player choice

playerChoice = []

# defining the board variable

# display greeting and the rules of the game

print("Hey This is Tic Tac Toe")
time.sleep(1)
userName = input("Enter your name: ")
time.sleep(0.5)
print(f"Hello {userName}! Let's play Tic Tac Toe")
time.sleep(1)
print("Rules")
printBoardWithNumbers()
time.sleep(1)
print("Rule 1: You can only choose a number between 1 and 9")
time.sleep(1)
print("Rule 2: You can only choose a number once")
time.sleep(1)
print("Rule 3: You can only choose a number that is not already taken")
time.sleep(1)
print("Rule 4: You can only choose a number that is on the board")
print(" ")
print("You are X")
print("Lets go!")

printBoardWithoutNumbersBeforeTheFirstInput()

# list that stores the input return

while True:
  if check_win(playerChoice) == True:
    print("You won!")
    exit()

  elif check_lose(computerChoice) == True:
    print("You lose!")
    exit()
  else:
    entry = int(input("Enter your choice: "))
    playerChoice.append(entry)

    printBoardWithoutNumbersAfterTheFirstInput()

    print("It's Computer's turn")
    computer_generated_number()
    printBoardWithoutNumbersAfterTheFirstInput()
