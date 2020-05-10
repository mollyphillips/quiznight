from typing import List
import csv
import random

class QuestionEngine:

    qNotYetAsked: List[List[str]] = [[]]
    qAlreadyAsked: List[List[str]] = [[]]
    numberOfQuestions: int = 0

    def __init__(self, file_name: str):
        self.qNotYetAsked = self.getCsvAsList(file_name)
        self.numberOfQuestions = len(self.qNotYetAsked)

    def getCsvAsList(self, file_name: str) -> List[List[str]]:
        return_array = []
        with open(file_name, "r") as quiz_csv:
            reader = csv.reader(quiz_csv)
            for row in reader:
                    return_array.append(row)  
        return return_array

    def getAQuestion(self) -> dict:
        if len(self.qNotYetAsked) == 0:
            return False
        r = random.randint(0,len(self.qNotYetAsked)-1)
        question = self.qNotYetAsked[r]
        self.qNotYetAsked.remove(question)
        self.qAlreadyAsked.append(question)
        return {
            "question" : question[1] + "\n" + question[2] + "\n"  + question[3] + "\n" + question[4],
            "answer": question[0]
        }
    
    def getAllQuestions(self) -> List[dict]:
        allQuestions = []
        for x in self.qNotYetAsked:
            allQuestions.append({"question" : x[1] + "\n" + x[2] + "\n"  + x[3] + "\n" + x[4],"answer": x[0]})
        random.shuffle(allQuestions)
        return allQuestions

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
 
