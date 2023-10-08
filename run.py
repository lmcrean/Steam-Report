#run.py

import json #https://docs.python.org/3/library/json.html
import gspread #https://docs.gspread.org/en/latest/
import requests #https://docs.python-requests.org/en/latest/
import html #https://docs.python.org/3/library/html.html
import random #https://docs.python.org/3/library/random.html
import os #https://docs.python.org/3/library/os.html
import sys; print(sys.executable)
from termcolor import colored, cprint
import subprocess
subprocess.check_call([sys.executable, "-m", "pip", "install", "prettytable"])
os.system('cls' if os.name == 'nt' else 'clear') # Clear the terminal screen
from google.oauth2.service_account import Credentials
from pprint import pprint
from prettytable import PrettyTable
x = PrettyTable()

SCOPE = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive.file',
    'https://www.googleapis.com/auth/drive'
]

# Google API imported with thanks to Code Institute Tutorial 'Love Sandwiches' by Anna Greaves
CREDS = Credentials.from_service_account_file('creds.json') # creds.json is a file that is not pushed to github 
SCOPED_CREDS = CREDS.with_scopes(SCOPE) #creds.with_scopes is a method that takes in the scope variable. The scope variable is a list of API's that we want to access.
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS) # gspread.authorize is a method that takes in the SCOPED_CREDS variable. This variable is the credentials we created to access the API's.
SHEET = GSPREAD_CLIENT.open('Steam_Test') # name of the spreadsheet

# For personality test, initialize variables including trait scores.
with open("personality_statements.json", "r") as file: # Load the questions from the JSON file. R = read.
    quiz_data = json.load(file) #“Json.load in Python.” GeeksforGeeks, GeeksforGeeks, 12 Mar. 2020, www.geeksforgeeks.org/json-load-in-python/. Accessed 5 Oct. 2023.
user_answers = [] 
trait_scores = {"Openness": 0, "Conscientiousness": 0, "Extraversion": 0, "Agreeableness": 0, "Neuroticism": 0}


# For subject test, initialize variables including subject scores.
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
    print("We're going to test your personality and run a quiz to help with your career choices. At the end of the test you'll get a customized personality report.\n")

    print("Please select an option from the menu below:")
    print("1 - Begin Personality Quiz (Testing phase)")
    print("2 - View STEAM Leaderboard (Testing phase)")
    print("3 - How to Play")
    print("4 - About STEAM")
    print("5 - Exit") 

def main():
    """
    run all program functions, starting with the main menu. Plays the game.
    """
    print("Welcome to Steam Test!")
    print("We're going to test your personality and run a quiz to help with your career choices. At the end of the test you'll get a customized personality report.\n")
    username_str = input("Enter your username here: ") # ask the user for their username
    if validate_name(username_str): 
            print("Data is valid!")
    while True:
        try:
            mainMenu()
            choice = int(input("Please enter your choice: "))
            if choice == 1:
                """redirects to personality quiz, which will then redirect to subject quiz"""
                start_personality_quiz()
                print("\nThank you for completing the quiz! Your responses:") # Display the user's answers
                subject_scores = SubjectScore(0,0,0,0,0,0)
                dataHandling(subject_scores, username_str)
                
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


def validate_name(values):
    """
    The name cannot be more than 9 characters long.
    """
    try:
        if len(values) > 9:
            raise ValueError(
                f"Invalid name: {values}. The name cannot be more than 9 characters long. You provided {len(values)} characters.\n"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False  # return False if errors are raised.
    
    return True # return True if noerrors are raised. This means that the function will return True if the try block is successful. If unsuccessful, the except block will run and return False. For example, if the user en ters 5 numbers instead of 6, the except block will run and return False.


# ------------------ Overall Structure of Programme ------------------
# The programme will begin with the main menu, which will allow the user to go through the personality quiz, the subject quiz and leaderboard, and finally onto a personality report.

def start_personality_quiz():
    random.shuffle(quiz_data["questions"]) # Shuffle the questions. “Python Random Shuffle() Method.” W3schools.com, 2023, www.w3schools.com/python/ref_random_shuffle.asp. Accessed 5 Oct. 2023.
    question_index = 0
    print(len(quiz_data["questions"]))
    print(f"question_index: {question_index}")
    ask_question(question_index)
    while question_index < len(quiz_data["questions"]): #“Python Len() Function.” W3schools.com, 2023, www.w3schools.com/python/ref_func_len.asp. Accessed 5 Oct. 2023. Len() function returns the number of items in an object. While the question index is less than the number of questions in the quiz_data dictionary, the loop will continue. Once the question index is equal to the number of questions in the quiz_data dictionary, the loop will stop.
        ask_question(question_index)
        question_index += 1
    personalityResults()

def start_subject_quiz():
    subjectQuiz()

def start_personality_report():
    personalityReport()














def ask_question(question_index): 
    """
    Ask the user a question about their personality and get their response.

    The question_index indicates the question number in the quiz_data dictionary.
    
    “Python Function Arguments.” W3schools.com, 2023, www.w3schools.com/python/gloss_python_function_arguments.asp#:~:text=A%20parameter%20is%20the%20variable,function%20when%20it%20is%20called. Accessed 5 Oct. 2023.
    """
    os.system('cls' if os.name == 'nt' else 'clear')# Clear the terminal screen
    question = quiz_data["questions"][question_index]
    print(f"Question {question_index + 1}:")
    print(question["statement"])

    while True:
        response = input("Please enter a number from 1 to 9 \n (1 = Strongly Disagree, 5 = Neutral, 9 = Strongly Agree): ")

        try:
            response = int(response) # Convert the user's response to an integer
            if 1 <= response <= 9:
                user_answers.append(response) # Add the response to the user's answers
                trait_scores[question["trait"]] += response  # Add the response to the corresponding trait score
                break  # Exit the loop when a valid response is provided
            else:
                print("Invalid response. Please enter a number between 1 and 9.")
        except ValueError:
            print("Invalid response. Please enter a number between 1 and 9.")

def convert_score_to_percentage(score):
    """
    Convert a personality trait score between 5 and 45 to a percentage.

    The trait score should be between 5 and 45.
    
    Returns The percentage equivalent of the trait score.
    """
    if 5 <= score <= 45:
        percentage = ((score - 5) / 40) * 100
        return round(percentage, 1) #“Python Round() Function.” W3schools.com, 2023, www.w3schools.com/python/ref_func_round.asp. Accessed 5 Oct. 2023.
    else:
        return "Invalid score. It should be between 5 and 45."


def personalityResults():
    """displays personality results, with option to render full results"""
    os.system('cls' if os.name == 'nt' else 'clear')# Clear the terminal screen
    print("\nTrait Scores in Percentage:")
    for trait, score in trait_scores.items():
        print(f"{trait}: {convert_score_to_percentage(score)}%")

    print("press any key to continue")
    input()












# ------------------ Subject Quiz Section ------------------
# In this section, the user will be asked 10 questions from each subject area with 4 multiple choice answers to choose from. The user will be given a score out of 10 for each subject area, and a total score out of 50.


def subjectQuiz():
    subject_scores = SubjectScore(0,0,0,0,0,0)
    os.system('cls' if os.name == 'nt' else 'clear')# Clear the terminal screen
    print("We are now beginning the multiple choice test.")
    print("Let's Start with Science!\n")
    print(f"---------Question 1 of 10---------\n")
    amount = 10
    category = 17 #Category 17 is Science
    startQuestionNumber() #startQuestionNumber is a function that sets the question number to 1
    subject_scores.resetAllScores()
    topic = "Science"
    playQuiz(amount, category, subject_scores, topic)
    
    print("Now on to Technology!\n")
    amount = 10
    category = 30 #Category 30 is Technology
    startQuestionNumber()
    topic = "Technology"
    playQuiz(amount, category, subject_scores, topic)
    
    print("Now on to English!\n")
    amount = 10
    category = 10 #Category 10 is Books
    startQuestionNumber()
    topic = "English"
    playQuiz(amount, category, subject_scores, topic)
    
    print("Now on to Art!\n")
    amount = 10
    category = 25 #Category 25 is Art
    startQuestionNumber()
    topic = "Art"
    playQuiz(amount, category, subject_scores, topic)
    
    print("Now on to Math!\n")
    amount = 10 
    category = 19 #Category 19 is Math
    startQuestionNumber() 
    topic = "Math"
    playQuiz(amount, category, subject_scores, topic)
    
    #clear the terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')# Clear the terminal screen


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
    Starts the question number at 1
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

def playQuiz (amount: int, category: int, subject_scores: SubjectScore, username_str) -> None:
    """
    credit to walkthrough: "Quiz App Using API Data - Python Project.” Run That, Run That, 16 May 2023, www.runthat.blog/quiz-app-using-api-data-python-project/. Accessed 24 Sept. 2023.
    """
    print("You have chosen to begin the multiple choice quiz.")
    question_pool = getTriviaQuestions(amount, category) # Get the questions from the API
    question_number = startQuestionNumber()  # Initialize question_number
    for question in question_pool: # Loop through the questions
        question_text = html.unescape(question["question"]) # Get the question text
        print(question_text) # Print the question
        choices = question ["incorrect_answers"] # Get the incorrect answers
        choices.extend([question["correct_answer"]]) # Add the correct answer to the choices list
        question_number = trackQuestionNumber(question_number)  # Pass question_number as an argument
        shuffled_choices = shuffleAnswerChoices(choices) # Shuffle the choices
        printAnswerChoices(question_number, shuffled_choices) # Print the choices
        user_choice_index = getUserAnswer() # Get the user's answer
        user_choice_text = shuffled_choices[user_choice_index] # Get the user's choice text
        correct_choice_text = html.unescape(question["correct_answer"]) # Get the correct choice text

        os.system('cls' if os.name == 'nt' else 'clear') # Clear the terminal screen

        if user_choice_text == correct_choice_text:
            subject_scores.updateTotalScore()  # Update Total score
            if category == 17:
                subject_scores.updateScienceScore() # Update Science score
                topic = "Science"
            elif category == 30:
                subject_scores.updateTechnologyScore() # Update Technology score
                topic = "Technology"
            elif category == 10:
                subject_scores.updateEnglishScore() # Update English score
                topic = "English"
            elif category == 25:
                subject_scores.updateArtScore()
                topic = "Art"
            elif category == 19:
                subject_scores.updateMathScore()
                topic = "Math"
            print(f"Correct! You answered: {correct_choice_text}\n")
            print("You have earned 1 point!")
            print(f"---------Section: {topic}---------\n")
            print(f"---------Question {question_number} of 10---------\n")
            
        else:
            print(f"Incorrect. The correct answer is {correct_choice_text}\n")
            print(f"---------Section: {topic}---------\n")
            print(f"--------Question {question_number} of 10---------\n")
        
    print("You have completed the test!")
    dataHandling(subject_scores, username_str)


 

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
    Starts the question number at 1
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


def playQuiz (amount: int, category: int, subject_scores: SubjectScore, topic) -> None:
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

        if user_choice_text == correct_choice_text: # If the user's choice is correct....
            subject_scores.updateTotalScore()  # Update Total score
            if category == 17:
                subject_scores.updateScienceScore() # Update Science score
            elif category == 30:
                subject_scores.updateTechnologyScore() # Update Technology score
            elif category == 10:
                subject_scores.updateEnglishScore() # Update English score
            elif category == 25:
                subject_scores.updateArtScore() # Update Art score
            elif category == 19:
                subject_scores.updateMathScore() # Update Math score
            print(f"Correct! You answered: {correct_choice_text}\n")
            print("You have earned 1 point!")
            print(f"Your Total score is {subject_scores.scoreTotal} of 50 \n")
            print(f"--------Topic: {topic}---------\n")
            print(f"---------Question {question_number} of 10---------\n")
            
        else: #if the user's choice is incorrect, don't update the score...
            print(f"Incorrect. The correct answer is {correct_choice_text}\n")
            print(f"Your Total score is {subject_scores.scoreTotal}\n")
            print(f"--------Topic: {topic}---------\n")
            print(f"--------Question {question_number} of 10---------\n")















# ------------------ Data Handling Section ------------------
# In this section, the user's data from the quiz will be uploaded to Google Sheets, being appended to the bottom of a worksheet.
# This section is heavily adapted from the Code Institute Love Sandwiches project by Anna Greaves

def dataHandling(subject_scores, username_str): #dataHandling() uses the subject_scores variable
    """
    Run all program functions
    """
    data = getLocalDataFromUser(subject_scores, username_str)  # call the getLocalDataFromUser function and store the returned data in a variable called data
    user_data = data  # convert the data provided by the user into integers. num is a variable that represents each item in the list data. 
    pushToAPICloud(user_data, "score")  # call the pushToAPICloud function with user_data as a list
    get_high_score_leaderboard()  # call the get_high_score_leaderboard function and store the returned data in a variable called score_columns

def getLocalDataFromUser(subject_scores: SubjectScore, username_str) -> None:
    """
    Gets the score and username from user and returns the username. After passing this loop, the data is ready to be appended to the worksheet.
    """

    while True: # loop until valid data is provided

        print("gather user data")
        
        print(f"Username: {username_str}\n") # print the username
        
        #place high score data into user_data_string variable
        user_data_string = f"{username_str},{subject_scores.scoreTotal},{subject_scores.scoreScience},{subject_scores.scoreTechnology},{subject_scores.scoreEnglish},{subject_scores.scoreArt},{subject_scores.scoreMath}" 

        user_data = user_data_string.split(",") # split the user_data string into a list of strings at each comma. This will create a list of strings. The first item in the list will be the username, and the rest of the items will be the scores.

        break # break out of the while loop
    return user_data # return the user_data list

def pushToAPICloud(data):
    """
    Receives a list of strings and integers to be inserted into a worksheet.
    Update the worksheet with the data provided.
    """
    worksheet_to_update = SHEET.worksheet('score') # access the relevant worksheet
    worksheet_to_update.append_row(data) # append the test user values provided as a new row at the bottom of the relevant worksheet

def get_high_score_leaderboard():
    """
    Collects columns of data from score worksheet.

    “Prettytable.” PyPI, 11 Sept. 2023, pypi.org/project/prettytable/. Accessed 1 Oct. 2023.
    """
    worksheet = SHEET.worksheet('score')  # Replace 'Sheet1' with your worksheet name.
    data = worksheet.get_all_values() # Read data from Google Sheet
    table = PrettyTable
    table.field_names = data[0] # Set the field names based on the first row of data (assuming it's the header row)
    for row in data[1:]: # Populate PrettyTable with data. 1 means start at index 1, which is the second row. This is because the first row is the header row.
        table.add_row(row)
    table.sortby = "Score" # Sort the table by the Total column, in ascending order
    table.reversesort = True # Reverse the order of the sort, so it's descending
    print(table) # Print the PrettyTable
    print("Above is your subject score, sorted by total score.")
    print("Press any key to continue on to your Personality Report")
    input()
    start_personality_report()

    return 














def personalityReport():
    """
    This personality report summarises the users personality traits and provides a recommendation for a career path.

    It goes through a series of if statements to determine the user's personality type, and then prints the relevant report.

    "your name is X and your personality type is Y, you scored highest in "
    """
    



















main()