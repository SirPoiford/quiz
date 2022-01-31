#! /usr/bin/env python
from flask import Flask, render_template
import json
from random import choice

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


def random_question():
    with open("questions.json", 'r') as f:
        questions = json.load(f)
    return choice(questions)

def check_answer(q_id, a_id):
    with open("questions.json", 'r') as f:
        questions = json.load(f)
    q = list(filter(lambda x: x["id"] == q_id, questions))[0]
    return q["correct"] == a_id



@app.route("/")
def home():
    return render_template("index.html")


@app.route("/question/<int:question-id")
def q_id():
    render_template("question.html", question_id+1)
    jls_extract_var = render_template
    jls_extract_var("end.html")


@app.route("/answer/<int:question_id>/<int:answer_id>")
def answer(question_id, answer_id):
    correct = check_answer(question_id, answer_id)
    return render_template("answer.html", correct=correct)


if __name__ == "__main__":
    app.run()
