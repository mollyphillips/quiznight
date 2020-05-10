from flask import Flask, render_template, request, session
from typing import List
from dadsCode import getQuestionsFromCSV
import time

app = Flask(__name__)
app.secret_key = "any random string"

nQuestions: int = 0
questions: List[dict] = []
score: int = 0
startTime: int
currentQuestion: dict = {}
questionNumber:int= 0

@app.route('/')
def begin_webapp():
    session['questions'] = getQuestionsFromCSV("quiz.csv")
    session['nQuestions'] = len(session['questions'])
    session['startTime'] = time.time()
    session['questionNumber'] = 0
    session['currentQuestion'] = session['questions'][session['questionNumber']]
    session['score'] = 0
    return render_template('quiz.html', question = session['currentQuestion']["question"], number = session['questionNumber'] + 1 )

@app.route('/result',methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        answer = request.form["answer"]
        if answer == session['currentQuestion']["answer"]:
            session['score'] = session['score'] + 1
        session['questionNumber'] = session['questionNumber'] + 1
        if session['questionNumber'] < session['nQuestions']:
            session['currentQuestion']  = session['questions'][session['questionNumber']]
            return render_template('quiz.html', question = session['currentQuestion']["question"], number = session['questionNumber'] + 1 )
        else:
            return render_template("result.html",score = session['score'], time = int(time.time()-session['startTime']))

if __name__ == '__main__':
   app.run(debug = True)