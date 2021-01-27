import random
import time

counter = 0

# Intro
print("---Escape Room---\n")
print("You suddenly appear in a room \n\nYou see the words in red, ESCAPE")
print("You must complete the escape room to survive.")

# Loops unstil 
while True:
  answer = input("Are you ready? (y/n)")
  answer = answer.lower()

  if answer == "y":
    print("\nYou walk into the first room")
    break
  else:
    print("\nYou are not ready.")

# Room 1
print("You must solve the puzzles and questions to escape each room \nYou see on the wall a question with multiple answers")

print("counter to complete the puzzles in the first counter!")

print("\nWhat does Ransomware do?")
print("\nA.) Disguises itself as legitimate software \nB.) Threatens to publish the victim's data or  block access to it  \nC.) Aims to gather information about a person or organization \nD.) Automatically generates advertisements")

round1 = 0
while True:
  round1 += 1

  answer = input("\nAnswer: ")
  answer = answer.lower()

  if answer == "b":
    print("\nPuzzle Piece Found!! Letter found: B")
    print("Well done. You completed this puzzle in ", round1, " tries.")
    break
  elif answer == "a" or answer == "c" or answer == "d":
    print("\n---Incorrect---")
  else:
    print("\nPlease enter a valid option.")

if round1 == 1:
  counter += 1

else:
  counter += 0

#---------------------------
print("\nAnother puzzle is on the wall")

print("\nWhat is the most crucial component to any computer system?")
print("\nA.) Power Supply \nB.) RAM  \nC.) Hard Drive \nD.) CPU ")

round2 = 0
while True:
  round2 += 1

  answer = input("\nAnswer: ")
  answer = answer.lower()

  if answer == "a":
    print("\nPuzzle Piece Found!! Letter found: R")
    print("Well done. You completed this puzzle in ", round2, " tries.")
    break
  elif answer == "b" or answer == "c" or answer == "d":
    print("\n---Incorrect---")
  else:
    print("\nPlease enter a valid option.")

if round2 == 1:
  counter += 1

else:
  counter += 0

print("\nOne question remains, written on the ground")

print("\nWhat is an example of an input device?")
print("\nA.) Monitor \nB.) Speakers  \nC.) Mouse \nD.) Headset ")

round3 = 0
while True:
  round3 += 1
  answer = input("\nAnswer: ")
  answer = answer.lower()

  if answer == "c":
    print("\nPuzzle Piece Found!! Letter found: I")
    print("Well done. You completed this puzzle in ", round3, " tries.")
    break
  elif answer == "b" or answer == "c" or answer == "d":
    print("\n---Incorrect---")
  else:
    print("\nPlease enter a valid option.")

if round3 == 1:
  counter += 1

else:
  counter += 0

print("First Tries Score: ", counter)

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
time.sleep(1.5)

while True:
  option = input("What do you do \n1. Wake it up and attack it \n2. counter to walk around \nAnswer:")
  if option == "1":
    print("------------------------------------------------------------")
    print("\nYou quickly sprint to the creature, seeing as it is weak while sleeping, you begin punching it with your hands")
    time.sleep(1.5)
    print("You quickly realize that are you are doing next to nothing, and the creature wakes up.")
    time.sleep(1.5)
    print("\nIt rises and it towers over you \nYou see that it is a computer virus!")
    time.sleep(1.5)
    break

  elif option == "2":
    print("------------------------------------------------------------")
    print("You attempt to sneak around this creature, but you clumsily fall over and make a lound noise")
    time.sleep(1.5)
    print("\nBy attempting to sneak around it, you accidentally woke up the creature.")
    print("\nIt rises and it towers over you \nYou see that it is a computer virus!")
    break
  else:
    print("Invalid Answer")

print("Now that it is awake it looks at you, ready to attack.")
time.sleep(1.5)
print("A sword appears in front of you!")
time.sleep(1.5)
print("\nYou now have three options")

# Boss Battle (Room 2)
health = 100
virus_health = 160

while health > 0 and virus_health > 0:
  
  virus = random.randint(1,3)
  answer = int(input("\n1. Attack \n2. Heal \n3. Dodge\n\n"))
  
  if virus == 1:
    print("\nThe virus spams you with advertisements")
    health -= 35
    print("Your health: ", health)
  
  elif virus == 2:
    print("\nThe virus attacks you by multiplying")
    health -= 25
    print("Your health: ", health)

  elif virus == 3:
    print("\nThe virus' attack missed!")
    print("Your health: ", health)

  print("\n")
  if answer == 1:
    print("You attack!")
    virus_health -= 40
    print("virus's health: ", virus_health)

  elif answer == 2:
    print("You decided to heal.")
    health += 40
    print("virus's health: ", virus_health)
    print("Your health: ", health)

  elif answer == 3:
    print("You really think you can dodge a virus?")
    print("virus's health: ", virus_health)

if health <= 0:
  print("\nYOU HAVE DIED...")
  quit()

print("The virus has been slain.")
time.sleep(1.5)

# Key to advance
print("\nYou receive more parts of the code")
time.sleep(2)
print("\nSo far you have: \nB \nR \nI \n\nYour new parts of the code: \nS \nK")
time.sleep(3)

# Room 3 - Multiple Choice Quiz
print("\nYou advance to the next room, it is dimly light, and there appears to be small table. A multiple choice test, what?!?!?!")

print("\nYou see written on it you must get above 7/10 to pass the test, or you die!")

score = 0

print("\nWhat does is the purpose of the GPU?")

print("\nA.) Powers the computer \nB.) The brain of the computer  \nC.) Displays the graphics \nD.) Stores the memory")

while True:
  answer = input("\nAnswer: ")
  answer = answer.lower()
  
  if answer == "c":
    score += 1
    print("\nCorrect")
    print("Score: ", score)
    break

  elif answer == "a" or answer == "b" or answer == "d":
    print("\nIncorrect")
    print("Score: ", score)
    break
    
  else:
    print("\nPlease enter a valid option.")

print("\nWhat type of memory is stored on the hard drive?")

print("\nA.) Temporary  \nB.) Permanent  \nC.) Slow memory \nD.) Fast memory")

while True:
  answer = input("\nAnswer: ")
  answer = answer.lower()
  
  if answer == "b":
    score += 1
    print("\nCorrect")
    print("Score: ", score)
    break

  elif answer == "a" or answer == "c" or answer == "d":
    print("\nIncorrect")
    print("Score: ", score)
    break
    
  else:
    print("\nPlease enter a valid option.")

print("\nThis type of memory is the slowest in the memory hierarchy:")

print("\nA.) External memory  \nB.) Storage \nC.) On chip \nD.) Internal memory")

while True:
  answer = input("\nAnswer: ")
  answer = answer.lower()
  
  if answer == "b":
    score += 1
    print("\nCorrect")
    print("Score: ", score)
    break

  elif answer == "a" or answer == "c" or answer == "d":
    print("\nIncorrect")
    print("Score: ", score)
    break
    
  else:
    print("\nPlease enter a valid option.")

print("\nWhich of the following best describes a computer virus:")

print("\nA.) Record your keystrokes that saves the data locally  \nB.) Pretends to remove other types of malware \nC.) Redirects and stores search history and activity \nD.) Reproduces itself when it is run")

while True:
  answer = input("\nAnswer: ")
  answer = answer.lower()
  
  if answer == "d":
    score += 1
    print("\nCorrect")
    print("Score: ", score)
    break

  elif answer == "a" or answer == "b" or answer == "c":
    print("\nIncorrect")
    print("Score: ", score)
    break
    
  else:
    print("\nPlease enter a valid option.")

print("\nWhich of the following is NOT considered a performance measure of RAM:")

print("\nA.) DDR Type \nB.) Storage (GB) \nC.) Resolution \nD.) Clock Speed (MHz)")

while True:
  answer = input("\nAnswer: ")
  answer = answer.lower()

  if answer == "c":
    score += 1
    print("\nCorrect")
    print("Score: ", score)
    break

  elif answer == "a" or answer == "b" or answer == "d":
    print("\nIncorrect")
    print("Score: ", score)
    break
    
  else:
    print("\nPlease enter a valid option.")

print("\nThis component handles all logical processing in a computer.")

print("\nA.) Motherboard \nB.) Hard Drive (GB) \nC.) RAM \nD.) CPU")

while True:
  answer = input("\nAnswer: ")
  answer = answer.lower()

  if answer == "d":
    score += 1
    print("\nCorrect")
    print("Score: ", score)
    break

  elif answer == "a" or answer == "b" or answer == "c":
    print("\nIncorrect")
    print("Score: ", score)
    break
    
  else:
    print("\nPlease enter a valid option.")

print("\nMeasured in Hertz (Hz), this specification determines how fast a monitor can refresh pixels.")

print("\nA.) Refresh Rate \nB.) Pixels per Inch \nC.) Reload Rate \nD.) Resolution")

while True:
  answer = input("\nAnswer: ")
  answer = answer.lower()

  if answer == "a":
    score += 1
    print("\nCorrect")
    print("Score: ", score)
    break

  elif answer == "b" or answer == "c" or answer == "d":
    print("\nIncorrect")
    print("Score: ", score)
    break
    
  else:
    print("\nPlease enter a valid option.")

print("\nThis type of modem converts data to be transferred via telephone lines.")

print("\nA.) Cable \nB.) DSL \nC.) USB \nD.) Cat 5")

while True:
  answer = input("\nAnswer: ")
  answer = answer.lower()

  if answer == "b":
    score += 1
    print("\nCorrect")
    print("Score: ", score)
    break

  elif answer == "a" or answer == "c" or answer == "d":
    print("\nIncorrect")
    print("Score: ", score)
    break
    
  else:
    print("\nPlease enter a valid option.")

print("\nWhich of these wireless standards provides the fastest data transmission rate?")

print("\nA.) 802.11 \nB.) 802.11n \nC.) 802.11ac \nD.) 802.11g")

while True:
  answer = input("\nAnswer: ")
  answer = answer.lower()

  if answer == "c":
    score += 1
    print("\nCorrect")
    print("Score: ", score)
    break

  elif answer == "a" or answer == "b" or answer == "d":
    print("\nIncorrect")
    print("Score: ", score)
    break
    
  else:
    print("\nPlease enter a valid option.")

print("\nThis unit of measurement is often used to indicate internet download speed")

print("\nA.) Mbps \nB.) MB/s \nC.) MHz \nD.) bpm")

while True:
  answer = input("\nAnswer: ")
  answer = answer.lower()

  if answer == "a":
    score += 1
    print("\nCorrect")
    print("Score: ", score)
    break

  elif answer == "b" or answer == "c" or answer == "d":
    print("\nIncorrect")
    print("Score: ", score)
    break
    
  else:
    print("\nPlease enter a valid option.")

if score >= 7:
  print("\nNot bad. You survived by getting 7 or above on the quiz.")

else:
  print("Unfortunately, you did not get 7 or above on the quiz")
  print("The floor opens up, and you fall.")
  print("GG")
  quit()

print("You receive more parts of the code: \nE, T")

print("\nSo far you have: \nB \nR \nI \nS \nK")

print("\n\nPut all the letters together to form the code: ")

while True:

  answer = input("\nAnswer: ")
  answer = answer.lower()
  if answer == "brisket":
    print("\nWell done. You advance to the next room.")
    break
  else:
    print("\nYOU ARE RUNNING OUT OF TIME")

# Room 4

print("\nYou walk into the next room, and it appears to be the inside of a Canada Computers??? \n\nTo complete this room, you have to learn what each computer part does.")

cpu = 0
gpu = 0
ram = 0
hard_drive = 0
motherboard = 0
power_supply = 0

while cpu == 0 or gpu == 0 or ram == 0  or hard_drive == 0  or motherboard == 0  or power_supply == 0:
  time.sleep(1.5)
  answer = input("\nWhat would you like you learn about? \n\n•CPU \n•GPU \n•RAM \n•Hard Drive \n•Motherboard \n•Power Supply\n\nAnswer: ")
  answer = answer.lower()
  if answer == "cpu":
    cpu += 1
    print("\nThe CPU is the electronic circuicounter within a computer that executes instructions that make up a computer program.")

  elif answer == "gpu":
    gpu += 1
    print("\nA graphics processing unit is a specialized electronic circuit designed to rapidly manipulate and alter memory to accelerate the creation of images")

  elif answer == "ram":
    ram += 1
    print("\nRandom-access memory is a form of computer memory that can be read and changed in any order, typically used to store working data and machine code.")
  elif answer == "hard drive":
    hard_drive +=1
    print("\nA high-capacity, self-contained storage device containing a read-write mechanism plus one or more hard disks, inside a sealed unit.")

  elif answer == "motherboard":
    motherboard +=1
    print("\nThe Motherboard holds and allows communication between many of the crucial electronic components of a system, such as the central processing unit and memory.")
    
  elif answer == "power supply":
    power_supply +=1
    print("\nAn electrical device that supplies electric power to an electrical load, such as powering a PC")
  else:
    print("\nInvalid Answer")


# Room  5
time.sleep(2.5)
print("\n\nWell done. One room remains ahead of you.")

time.sleep(2.5)
print("\n\nYou walk into the final room, with a small monitor in it. On the monitor you see Mr. Fabroa's google meeting.")

time.sleep(2.5)

print("\nYou suddenly recall all the 30 minute attendances and countless memes that were presented during each google meeting.")

time.sleep(2.5)
print("\nYou see a pufferfish appear in front of you.")

time.sleep(2.5)

while True:
  # Check if input is an integer
  try:
    augh = int(input("\nPlease enter an integer: "))
  
  # If not an integer, go back to start of loop
  except ValueError:
    print("\nInvalid Answer!")
    continue

  if augh < 0:
    print("\nNo negative numbers!")
    continue

  else:
    break

for i in range(augh):
  print("\nAUGH")


print("\nYou escaped and finished ICS201a!")