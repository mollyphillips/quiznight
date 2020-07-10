from dadsCode import getQuestionsFromCSV
import time
from pygame import mixer 

questions = getQuestionsFromCSV("quiz.csv")

mixer.init()
mixer.music.load('phoenix.mp3')
# mixer.music.play()

Title = "Molly's Mutichoice"
Instructions = "Answer a multi-choice question for $$$ prize"

print("\n\n")
print("Welcome to "+ Title + ", here are some instructions:")
print(Instructions)
print("\n")

Score = 0
startTime = time.time()

for question in questions:
    print("get ready for a question !! \n")
    time.sleep(1)
    print(question["prompt"])
    print("\n")
    Answer = (input("Enter your answer and press enter..."))
    if (Answer == question["answer"]):
        print("correct !! \n")
        Score = Score + 1
    else:
        print("sorry... wrong answer \n")
    print("your time so far is: " + str(int(time.time() - startTime)) + " seconds")
    print("Your score so far is: " + str(Score)) 

print("\n")
print("you scored " + str(Score) + " out of " + str(len(questions)) + " in the Molly Quiz Night \n")
print("your time was " + str(int(time.time() - startTime)) + " seconds")
print("Thanks for playing !!!! \n")