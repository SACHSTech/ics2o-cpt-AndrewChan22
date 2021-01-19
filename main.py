import random

""""
print("---Escape Room---\n")
print("You suddenly appear in a room \n\nYou see the words in red, ESCAPE")
print("You must complete the escape room to survive.")

while True:
  answer = input("Are you ready? (y/n)")
  answer = answer.lower()

  if answer == "y":
    print("\nYou walk into the first room")
    break
  else:
    print("\nYou are not ready.")


print("You must solve the puzzles and questions to escape each room \nYou see on the wall a question with multiple answers")

print("\nWhat does Ransomware do?")
print("\nA.) Disguises itself as legitimate software \nB.) Threatens to publish the victim's data or  block access to it  \nC.) Aims to gather information about a person or organization \nD.) Automatically generates advertisements")

while True:
  answer = input("\nAnswer: ")
  answer = answer.lower()
  if answer == "b":
    print("\nPuzzle Piece Found!! Letter found: B")
    break
  else:
    print("\nINCORRECT")

#---------------------------
print("\nAnother puzzle is on the wall")

print("\nWhat is the most crucial component to any computer system?")
print("\nA.) Power Supply \nB.) RAM  \nC.) Hard Drive \nD.) CPU ")

while True:

  answer = input("\nAnswer: ")
  answer = answer.lower()
  if answer == "a":
    print("\nPuzzle Piece Found!! Letter found: R")
    break
  else:
    print("\nINCORRECT")

print("\nOne question remains, written on the ground")

print("\nWhat is an example of an input device?")
print("\nA.) Monitor \nB.) Speakers  \nC.) Mouse \nD.) Headset ")

while True:

  answer = input("\nAnswer: ")
  answer = answer.lower()
  if answer == "c":
    print("Puzzle Piece Found!! Letter found: I")
    break
  else:
    print("\nINCORRECT")

print("\nTo advance to the next room, please enter the key.")


while True:

  answer = input("\nAnswer: ")
  answer = answer.lower()
  if answer == "bri":
    print("Well done. You advance to the next room.")
    break
  else:
    print("\nYOU ARE RUNNING OUT OF TIME")
  
print("\nYou walk into the next room, but instead of puzzles you see a creature sleeping, chained to the ground.")

option = input("What do you do \n1. Wake it up and attack it \n2. Try to walk around")

if option == "1":
  print("You quickly sprint to the creature, seeing as it is weak while sleeping, you begin punching it with your hands")
  print("You quickly realize that are you are doing next to nothing, and the creature wakes up.")
  print("\nIt rises and it towers over you \nYou see that it is a dragon")

elif option == "2":
  print("You attempt to sneak around this creature, but you clumsily fall over and make a lound noise")
  print("\nBy attempting to sneak around it, you accidentally woke up the creature.")
  print("\nIt rises and it towers over you \nYou see that it is a dragon")
"""
print("Now that it is awake it looks at you, ready to attack")
print("A sword appears in front of you")
print("\nYou now have three options")

health = 100
dragon_health = 200

while health > 0 and dragon_health > 0:
  
  dragon = random.randint(1,3)
  answer = int(input("\n1. Attack \n2. Heal \n3. Dodge\n\n"))
  
  if dragon == 1:
    print("\nThe dragon breathes a breathe of fire onto you, you are severely hurt")
    health -= 35
    print("Your health: ", health)
  
  elif dragon == 2:
    print("\nThe dragon slashes you with it's tail")
    health -= 25
    print("Your health: ", health)

  elif dragon == 3:
    print("\nThe dragon's attack missed!")
    print("Your health: ", health)

  print("\n")
  if answer == 1:
    print("You attack!")
    dragon_health -= 40
    print("Dragon's health: ", dragon_health)

  elif answer == 2:
    print("You decided to heal.")
    health += 40
    print("Dragon's health: ", dragon_health)
    print("Your health: ", health)

  elif answer == 3:
    print("You really think you can dodge a dragon?")
    print("Dragon's health: ", dragon_health)

if health <= 0:
  print("\nYOU HAVE DIED...")
  quit()

print("The dragon has been slain.")

print("\nYou receive more parts of the code")
print("\nSo far you have: \nB \nR \nI \n\nYour new parts of the code: \nS \nK")

print("\nYou advance to the next room, it is dimly light, and there appears to be small table. A multiple choice test what?!?!?!")

print("\nYou see written on it you must get above 7/10 to pass the test, or you die!")

score = 0

print("What does is the purpose of the GPU")

answer1 = input("\nA.) Powers the computer \nB.) The brain of the computer  \nC.) Displays the graphics \nD.) Stores the memory")
answer1 = answer1.lower()

if answer1 == "c":
  score += 1
else:
  score += 0

print("What type of memory is stored on the hard drive?")

answer2 = input("\nA.) Temporary  \nB.) Permanent  \nC.) Slow memory \nD.) Fast memory")
answer2 = answer2.lower()

if answer2 == "b":
  score += 1
else:
  score += 0

print("This type of memory is the slowest in the memory hierarchy:")

answer3 = input("\nA.) External memory  \nB.) Storage \nC.) On chip \nD.) Internal memory")
answer3 = answer3.lower()

if answer3 == "b":
  score += 1
else:
  score += 0

print("Which of the following best describes a computer virus")

answer4 = input("\nA.) Record your keystrokes that saves the data locally  \nB.) Pretends to remove other types of malware \nC.) Redirects and stores search history and activity \nD.) Reproduces itself when it is run")
answer4 = answer4.lower()

if answer4 == "d":
  score += 1
else:
  score += 0

print("Which of the following is NOT considered a performance measure of RAM")

answer5 = input("\nA.) DDR Type \nB.) Storage (GB) \nC.) Resolution \nD.) Clock Speed (MHz)")
answer5 = answer5.lower()

if answer5 == "c":
  score += 1
else:
  score += 0
