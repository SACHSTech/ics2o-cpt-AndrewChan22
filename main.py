import random

rounds = 0
points = 0

print("---Welcome to the Jeopardy Game of ICS201a---")
print("There are :200: :400: :600: :800: :1000: point options.\n\nYou will only get 10 questions to gain the most amount of points. \nPlease select the letter corresponding to your answer. \nGoal to beat is 10000 points!")
print("\nEnter the number value (e.g 200, 400")



while rounds <  10:
  rounds += 1
  
  option = int(input("\nWhich question will you choose?: "))

  question_200 = random.randint(1, 3)
  question_400 = random.randint(1, 3)
  question_600 = random.randint(1, 3)
  question_800 = random.randint(1, 3)
  question_1000 = random.randint(1, 3)

  if option == 200:
    print("You picked a 200 point question.")

    if question_200 == 1:
      print("What does CPU stand for? ")
      print("A.) Central Processing Unit \nB.) Computer Processing Unit \nC.) Central Processing Utility")
      answer1 = input("Answer: ")
      answer1 = answer1.lower()

      if answer1 == "a":
        print("\nCORRECT")
        points += 200
        print("Score: ",points)
      else:
        print("\nINCORRECT")
        print("Score: ",points)

    elif question_200 == 2:
      print("What does GPU stand for? ")
      print("A.) Global Production Unit \nB.) Graphics Processer \nC.) Graphics Processing Unit")
      answer2 = input("Answer: ")
      answer2 = answer2.lower()

      if answer2 == "c":
        print("\nCORRECT")
        points += 200
        print("Score: ",points)
      else:
        print("\nINCORRECT")
        print("Score: ",points)

    elif question_200 == 3:
      print("What is an example of an input device?")
    
      print("A.) Headset \nB.) Monitor \nC.) Mouse")
      answer3 = input("Answer: ")
      answer3 = answer3.lower()

      if answer3 == "c":
        print("\nCORRECT")
        points += 200
        print("Score: ",points)
      else:
        print("\nINCORRECT")
        print("Score: ",points)

  elif option == 400:
    print("You picked a 400 point question.")

    if question_400 == 1:
      print("What does Ransomware do? ")

      print("A.) Disguises itself as legitimate software \nB.) Threatens to publish the victim's data or  block access to it  \nC.) Aims to gather information about a person or organization")
      answer4 = input("Answer: ")
      answer4 = answer4.lower()

      if answer4 == "b":
        print("\nCORRECT")
        points += 400
        print("Score: ",points)
      else:
        print("\nINCORRECT")
        print("Score: ",points)

    elif question_400 == 2:
      print("What is most common type of Malware ")

      print("A.) Adware \nB.) Trojan Horse  \nC.) Spyware \nD.")
      answer5 = input("Answer: ")
      answer5 = answer5.lower()

      if answer4 == "a":
        print("\nCORRECT")
        points += 400
        print("Score: ",points)
      else:
        print("\nINCORRECT")
        print("Score: ",points)


  else:
    print("Invalid option")
    rounds += 1


if points >= 10000:
  print("You beat the record!")

else:
  print("You did not beat the record of 10000 :(")


