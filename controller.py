# controller.py
from package.personality import ask_question, personalityResults
from package.subjectquiz import subjectQuiz

def start_personality_quiz():
    ask_question()

def start_subject_quiz():
    subjectQuiz()