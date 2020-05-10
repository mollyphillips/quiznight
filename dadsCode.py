from typing import List
import csv
import random

def getQuestionsFromCSV(filename: str) -> List[dict]:
        
    csvAsList = []
    allQuestions = []

    with open(filename, "r") as quiz_csv:
        reader = csv.reader(quiz_csv)
        for row in reader:
                csvAsList.append(row)

    for x in csvAsList:
        allQuestions.append({"question" : x[1] + "\n" + x[2] + "\n"  + x[3] + "\n" + x[4]+ "\n" + x[5],"answer": x[0]})
    
    random.shuffle(allQuestions)
    
    return allQuestions
 
