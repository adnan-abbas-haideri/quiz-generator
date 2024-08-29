from flask import Blueprint, render_template, request, redirect, url_for
from models import Quiz, Question, db

quiz_blueprint = Blueprint('quiz', __name__)

@quiz_blueprint.route('/')
def index():
    quizzes = Quiz.query.all()
    return render_template('index.html', quizzes=quizzes)

@quiz_blueprint.route('/quiz/<int:quiz_id>')
def quiz(quiz_id):
    quiz = Quiz.query.get(quiz_id)
    return render_template('quiz.html', quiz=quiz)

@quiz_blueprint.route('/submit/<int:quiz_id>', methods=['POST'])
def submit(quiz_id):
    quiz = Quiz.query.get(quiz_id)
    score = 0
    for question in quiz.questions:
        answer = request.form.get(f'question-{question.id}')
        if answer == question.correct_answer:
            score += 1
    return render_template('result.html', score=score, total=len(quiz.questions))

