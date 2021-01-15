import random

rounds = 0
points = 0

print("---Welcome to the Jeopardy Game of ICS201a---")
print("There are :200: :400: :600: :800: :1000: point options.\nYou will only get 10 questions to gain the most amount of points. \nPlease select the letter corresponding to your answer. \nGoal to beat is 10000! points")


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
        print("CORRECT")
        points += 200
        print("Score: ",points)
      else:
        print("INCORRECT")
        print("Score: ",points)
    elif question_200 == 2:
      print("What does GPU stand for? ")
      print("A.) Global Production Unit \nB.) Graphics Processer \nC.) Graphics Processing Unit")
      answer2 = input("Answer: ")
      answer2 = answer2.lower()

      if answer2 == "c":
        print("CORRECT")
        points += 200
        print("Score: ",points)
      else:
        print("INCORRECT")
        print("Score: ",points)

    elif question_200 == 3:
      print("What is an example of an input device?")
    
      print("A.) Headset \nB.) Monitor \nC.) Mouse")
      answer3 = input("Answer: ")
      answer3 = answer3.lower()

      if answer3 == "c":
        print("CORRECT")
        points += 200
        print("Score: ",points)
      else:
        print("INCORRECT")
        print("Score: ",points)