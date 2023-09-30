# Google API imported with thanks to Code Institute Tutorial 'Love Sandwiches' by Anna Greaves.

import json #https://docs.python.org/3/library/json.html
import gspread #https://docs.gspread.org/en/latest/
import requests #https://docs.python-requests.org/en/latest/
import html #https://docs.python.org/3/library/html.html
import random #https://docs.python.org/3/library/random.html
import os #https://docs.python.org/3/library/os.html
import sys
from google.oauth2.service_account import Credentials
from pprint import pprint

SCOPE = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive.file',
    'https://www.googleapis.com/auth/drive'
]

CREDS = Credentials.from_service_account_file('creds.json') # creds.json is a file that is not pushed to github
SCOPED_CREDS = CREDS.with_scopes(SCOPE) #creds.with_scopes is a method that takes in the scope variable. The scope variable is a list of API's that we want to access.
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS) # gspread.authorize is a method that takes in the SCOPED_CREDS variable. This variable is the credentials we created to access the API's.
SHEET = GSPREAD_CLIENT.open('Steam_Test') # name of the spreadsheet

class SubjectScore:
    """
    Update the score in the local variable, using a class to update
    player1. updateScore += 1
    """
    def __init__(self, scoreScience, scoreTechnology, scoreEnglish, scoreArt, scoreMath, scoreTotal):
        self.scoreScience = scoreScience
        self.scoreTechnology = scoreTechnology
        self.scoreEnglish = scoreEnglish
        self.scoreArt = scoreArt
        self.scoreMath = scoreMath
        self.scoreTotal = scoreTotal
    
    def updateScienceScore(self):
        self.scoreScience += 1
        return self.scoreScience
    
    def updateTechnologyScore(self):
        self.scoreTechnology += 1
        return self.scoreTechnology
    
    def updateEnglishScore(self):
        self.scoreEnglish += 1
        return self.scoreEnglish
    
    def updateArtScore(self):
        self.scoreArt += 1
        return self.scoreArt
    
    def updateMathScore(self):
        self.scoreMath += 1
        return self.scoreMath
    
    def updateTotalScore(self):
        self.scoreTotal += 1
        return self.scoreTotal
    
    def resetAllScores(self):
        self.scoreScience = 0
        self.scoreTechnology = 0
        self.scoreEnglish = 0
        self.scoreArt = 0
        self.scoreMath = 0
        self.scoreTotal = 0
        return self.scoreScience, self.scoreTechnology, self.scoreEnglish, self.scoreArt, self.scoreMath, self.scoreTotal

def mainMenu():
    """
    The main menu of the game
    """
    os.system('cls' if os.name == 'nt' else 'clear') # Clear the terminal screen
    print("Welcome to Steam Test!")
    print("Please select an option from the menu below:")
    print("1 - Begin Test")
    print("2 - View Leaderboard")
    print("3 - How to Play")
    print("4 - About STEAM")
    print("5 - Exit") 

def main():
    """
    run all program functions, starting with the main menu. Plays the game.
    """
    subject_scores = SubjectScore(0,0,0,0,0,0)
    mainMenu()
    while True:
        try:
            choice = int(input("Please enter your choice: "))
            if choice == 1:
                os.system('cls' if os.name == 'nt' else 'clear')# Clear the terminal screen
                print("You have chosen to begin the test.")
                if __name__ == "__main__": #this expression executes when the file runs as a script but not as a module. Real Python. “What Does If __name__ == ‘__main__’ Do in Python?” Realpython.com, Real Python, 21 Sept. 2022, realpython.com/if-name-main-python/. Accessed 28 Sept. 2023.
                    print("Let's Start with Science!\n")
                    print(f"---------Question 1 of 10---------\n")
                    amount = 10
                    category = 17 #Category 17 is Science
                    topic = "Science"
                    difficulty = "&difficulty=easy"
                    startQuestionNumber() #startQuestionNumber is a function that sets the question number to 1
                    subject_scores.resetAllScores()
                    playQuiz(amount, category, subject_scores)
                if __name__ == "__main__": #
                    print("Now on to Technology!\n")
                    amount = 10
                    category = 30 #Category 30 is Technology
                    startQuestionNumber()
                    playQuiz(amount, category, subject_scores)
                if __name__ == "__main__": #
                    print("Now on to English!\n")
                    amount = 10
                    category = 10 #Category 10 is Books
                    startQuestionNumber()
                    playQuiz(amount, category, subject_scores)
                if __name__ == "__main__": #
                    print("Now on to Art!\n")
                    amount = 10
                    category = 25 #Category 25 is Art
                    startQuestionNumber()
                    playQuiz(amount, category, subject_scores)
                if __name__ == "__main__": #
                    print("Now on to Math!\n")
                    amount = 10 
                    category = 19 #Category 19 is Math
                    startQuestionNumber() 
                    playQuiz(amount, category, subject_scores)
                if __name__ == "__main__": 
                    mainMenu()

                
            elif choice == 2:
                print("You have chosen to view the leaderboard.")
                
            elif choice == 3:
                print("You have chosen to view the instructions.")
                
            elif choice == 4:
                print("You have chosen to view information about STEAM.")
                
            elif choice == 5:
                print("You have chosen to exit the program.")
                
            else:
                print("Please enter a number between 1 and 5.")
        except ValueError:
            print("Please enter a number between 1 and 5.")

def getTriviaQuestions(amount: int, category: int) -> list:
    """
    Get trivia questions from the json file
    """
    url = f"https://opentdb.com/api.php?amount=10&category={category}&type=multiple"
    response = requests.get(url)
    response_json = response.json()
    return response_json["results"]

def shuffleAnswerChoices(choices: list) -> list:
    """
    credit to walkthrough: "Quiz App Using API Data - Python Project.” Run That, Run That, 16 May 2023, www.runthat.blog/quiz-app-using-api-data-python-project/. Accessed 24 Sept. 2023.
    """
    random.shuffle(choices)
    return choices

def startQuestionNumber() -> int:
    """
    credit to walkthrough: "Quiz App Using API Data - Python Project.” Run That, Run That, 16 May 2023, www.runthat.blog/quiz-app-using-api-data-python-project/. Accessed 24 Sept. 2023.
    """
    question_number = 1
    return question_number

def trackQuestionNumber(question_number: int) -> int:
    """
    credit to walkthrough: "Quiz App Using API Data - Python Project.” Run That, Run That, 16 May 2023, www.runthat.blog/quiz-app-using-api-data-python-project/. Accessed 24 Sept. 2023.
    """
    question_number += 1
    if question_number > 10:
        question_number = 1
    return question_number

def printAnswerChoices(question_number: int, choices: list) -> None:
    """
    credit to walkthrough: "Quiz App Using API Data - Python Project.” Run That, Run That, 16 May 2023, www.runthat.blog/quiz-app-using-api-data-python-project/. Accessed 24 Sept. 2023.
    """
    for choice_index, choice in enumerate(choices):
        print(f"{choice_index+1}. {html.unescape(choice)}")


def getUserAnswer() -> int:
    """
    Get user input and ensure it's a valid number between 1 and 4. 
    
    Adapted heavily from walkthrough: "Quiz App Using API Data - Python Project.” Run That, Run That, 16 May 2023, www.runthat.blog/quiz-app-using-api-data-python-project/. Accessed 24 Sept. 2023.
    """
    while True:
        user_input = input("Enter the number of your choice: ")
        if not user_input:  # Check if the input is empty
            print("Empty input. Enter a number between 1 and 4")
            continue  # Continue the loop without processing further
        try:
            user_choice = int(user_input)
            if user_choice in range(1, 5): # 1,2,3, or 4
                return user_choice - 1
            else:
                print("Invalid input. Enter a number between 1 and 4")
        except ValueError:
            print("Invalid input with Value error. Enter a number between 1 and 4")


def playQuiz (amount: int, category: int, subject_scores: SubjectScore) -> None:
    """
    credit to walkthrough: "Quiz App Using API Data - Python Project.” Run That, Run That, 16 May 2023, www.runthat.blog/quiz-app-using-api-data-python-project/. Accessed 24 Sept. 2023.
    """
    question_pool = getTriviaQuestions(amount, category)
    question_number = startQuestionNumber()  # Initialize question_number
    for question in question_pool:
        question_text = html.unescape(question["question"])
        print(question_text)
        choices = question ["incorrect_answers"]
        choices.extend([question["correct_answer"]])
        question_number = trackQuestionNumber(question_number)  # Pass question_number as an argument
        shuffled_choices = shuffleAnswerChoices(choices)
        printAnswerChoices(question_number, shuffled_choices)
        user_choice_index = getUserAnswer()
        user_choice_text = shuffled_choices[user_choice_index]
        correct_choice_text = html.unescape(question["correct_answer"])

        os.system('cls' if os.name == 'nt' else 'clear') # Clear the terminal screen

        if user_choice_text == correct_choice_text:
            subject_scores.updateTotalScore()  # Update Total score
            if category == 17:
                subject_scores.updateScienceScore() # Update Science score
            elif category == 30:
                subject_scores.updateTechnologyScore() # Update Technology score
            elif category == 10:
                subject_scores.updateEnglishScore() # Update English score
            elif category == 25:
                subject_scores.updateArtScore()
            elif category == 19:
                subject_scores.updateMathScore()
            print(f"Correct! You answered: {correct_choice_text}\n")
            print("You have earned 1 point!")
            print(f"Your Total score is {subject_scores.scoreTotal} of 50 \n")
            print(f"your score in Science is {subject_scores.scoreScience} of 10")
            print(f"your score in Technology is {subject_scores.scoreTechnology} of 10")
            print(f"your score in English is {subject_scores.scoreEnglish} of 10")
            print(f"your score in Art is {subject_scores.scoreArt} of 10")
            print(f"your score in Math is {subject_scores.scoreMath} of 10")
            print(f"---------Question {question_number} of 10---------\n")
            
        else:
            print(f"Incorrect. The correct answer is {correct_choice_text}\n")
            print(f"Your Total score is {subject_scores.scoreTotal}\n")
            print(f"your score in Science is {subject_scores.scoreScience} of 10")
            print(f"your score in Technology is {subject_scores.scoreTechnology} of 10")
            print(f"your score in English is {subject_scores.scoreEnglish} of 10")
            print(f"your score in Art is {subject_scores.scoreArt} of 10")
            print(f"your score in Math is {subject_scores.scoreMath} of 10")
            print(f"--------Question {question_number} of 10---------\n")

    


main()