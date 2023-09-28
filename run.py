# Google API imported with thanks to Code Institute Tutorial 'Love Sandwiches' by Anna Greaves.

import json 
import gspread
import requests
import html
import random
import os #https://docs.python.org/3/library/os.html
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

def mainMenu():
    """
    The main menu of the game
    """
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
    mainMenu()
    while True:
        try:
            choice = int(input("Please enter your choice: "))
            if choice == 1:
                print("You have chosen to begin the test.")
                if __name__ == "__main__": #this expression executes when the file runs as a script but not as a module. Real Python. “What Does If __name__ == ‘__main__’ Do in Python?” Realpython.com, Real Python, 21 Sept. 2022, realpython.com/if-name-main-python/. Accessed 28 Sept. 2023.
                    print("Let's Start with Science!\n")
                    amount = 10
                    category = 17
                    playQuiz(amount,category)
                if __name__ == "__main__": #
                    print("Now on to Technology!\n")
                    amount = 10
                    category = 30
                    playQuiz(amount,category)
                if __name__ == "__main__": #
                    print("Now on to English!\n")
                    amount = 10
                    category = 10
                    playQuiz(amount,category)
                if __name__ == "__main__": #
                    print("Now on to Art!\n")
                    amount = 10
                    category = 25
                    playQuiz(amount,category)
                if __name__ == "__main__": #
                    print("Now on to Math!\n")
                    amount = 10
                    category = 19
                    playQuiz(amount,category)
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
    url = f"https://opentdb.com/api.php?amount=10&category={category}&difficulty=easy&type=multiple"
    response = requests.get(url)
    response_json = response.json()
    return response_json["results"]

def shuffleAnswerChoices(choices: list) -> list:
    """
    credit to walkthrough: "Quiz App Using API Data - Python Project.” Run That, Run That, 16 May 2023, www.runthat.blog/quiz-app-using-api-data-python-project/. Accessed 24 Sept. 2023.
    """
    random.shuffle(choices)
    return choices

def printAnswerChoices(choices: list) -> None:
    """
    credit to walkthrough: "Quiz App Using API Data - Python Project.” Run That, Run That, 16 May 2023, www.runthat.blog/quiz-app-using-api-data-python-project/. Accessed 24 Sept. 2023.
    """
    for choice_index, choice in enumerate(choices):
        print(f"{choice_index+1}. {html.unescape(choice)}")

def getUserAnswer() -> int:
    """
    credit to walkthrough: "Quiz App Using API Data - Python Project.” Run That, Run That, 16 May 2023, www.runthat.blog/quiz-app-using-api-data-python-project/. Accessed 24 Sept. 2023.
    """
    while True:
        user_choice = int(input("Enter the number of your choice: "))
        if user_choice in range(1, 5): # 1,2,3 or 4
            return user_choice - 1
        else:
            print("Invalid input. Enter a number between 1 and 4")

def playQuiz (amount: int, category: int) -> None: 
    """
    credit to walkthrough: "Quiz App Using API Data - Python Project.” Run That, Run That, 16 May 2023, www.runthat.blog/quiz-app-using-api-data-python-project/. Accessed 24 Sept. 2023.
    """
    question_pool = getTriviaQuestions(amount, category)
    for question in question_pool:
        question_text = html.unescape(question["question"])
        print(question_text)
        choices = question ["incorrect_answers"]
        choices.extend([question["correct_answer"]])
        shuffled_choices = shuffleAnswerChoices(choices)
        printAnswerChoices(shuffled_choices)
        user_choice_index = getUserAnswer()
        user_choice_text = shuffled_choices[user_choice_index]
        correct_choice_text = html.unescape(question["correct_answer"])

        # Clear the terminal screen
        os.system('cls' if os.name == 'nt' else 'clear')

        if user_choice_text == correct_choice_text:
            print(f"Correct! You answered: {correct_choice_text}\n")
        else:
            print(f"Incorrect. The correct answer is {correct_choice_text}\n")

        



main()