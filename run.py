#run.py

import json #https://docs.python.org/3/library/json.html
import gspread #https://docs.gspread.org/en/latest/
import requests #https://docs.python-requests.org/en/latest/
import html #https://docs.python.org/3/library/html.html
import random #https://docs.python.org/3/library/random.html
import os #https://docs.python.org/3/library/os.html
import sys; print(sys.executable)
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
    mainMenu()
    while True:
        try:
            choice = int(input("Please enter your choice: "))
            if choice == 1:
                """redirects to personality quiz, which will then redirect to subject quiz"""
                start_personality_quiz()
                print("\nThank you for completing the quiz! Your responses:") # Display the user's answers
                subject_scores = SubjectScore(0,0,0,0,0,0)
                leaderboardMain(subject_scores, username_str)
                
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









#TODO: fix error with extra question being asked


def ask_question(question_index): 
    """
    question_index is a parameter. 
    
    “Python Function Arguments.” W3schools.com, 2023, www.w3schools.com/python/gloss_python_function_arguments.asp#:~:text=A%20parameter%20is%20the%20variable,function%20when%20it%20is%20called. Accessed 5 Oct. 2023.
    """
    os.system('cls' if os.name == 'nt' else 'clear')# Clear the terminal screen
    question = quiz_data["questions"][question_index]
    print(f"Question {question_index + 1}:")
    print(question["statement"])

    while True:
        response = input("Please enter a number from 1 to 9 (1 = Strongly Disagree, 5 = Neutral, 9 = Strongly Agree): ")

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
    """displays personality results in percentage, with option to render full results"""
    os.system('cls' if os.name == 'nt' else 'clear')# Clear the terminal screen
    print("\nTrait Scores in Percentage:")
    for trait, score in trait_scores.items():
        print(f"{trait}: {convert_score_to_percentage(score)}%")

    print("\nPress 1 to continue on to the subject quiz.")

    if input() == "1":
        print("You have chosen to continue on to the subject quiz.")
        start_subject_quiz()
    else:
        print("Invalid answer. Please enter a number between 1 and 2.")















# FIX: leads back to question 1 of personality quiz

def subjectQuiz():
    subject_scores = SubjectScore(0,0,0,0,0,0)
    os.system('cls' if os.name == 'nt' else 'clear')# Clear the terminal screen
    print("We are now beginning the multiple choice test.")
    print("Let's Start with Science!\n")
    print(f"---------Question 1 of 10---------\n")
    amount = 10
    category = 17 #Category 17 is Science
    topic = "Science"
    difficulty = "&difficulty=easy"
    startQuestionNumber() #startQuestionNumber is a function that sets the question number to 1
    subject_scores.resetAllScores()
    playQuiz(amount, category, subject_scores)
    
    print("Now on to Technology!\n")
    amount = 10
    category = 30 #Category 30 is Technology
    startQuestionNumber()
    playQuiz(amount, category, subject_scores)
    
    print("Now on to English!\n")
    amount = 10
    category = 10 #Category 10 is Books
    startQuestionNumber()
    playQuiz(amount, category, subject_scores)
    
    print("Now on to Art!\n")
    amount = 10
    category = 25 #Category 25 is Art
    startQuestionNumber()
    playQuiz(amount, category, subject_scores)
    
    print("Now on to Math!\n")
    amount = 10 
    category = 19 #Category 19 is Math
    startQuestionNumber() 
    playQuiz(amount, category, subject_scores)
    
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
        
    print("You have completed the test!")
    leaderboardMain(subject_scores, username_str)

def get_user_data(subject_scores: SubjectScore, username_str) -> None:
    """
    Gets the score and username from user and returns the username.
    """

    while True: # True

        print("gather user data")
        
        print(f"Username: {username_str}\n") # print the username
        
        #place high score data into user_data_string variable
        user_data_string = f"{username_str},{subject_scores.scoreTotal},{subject_scores.scoreScience},{subject_scores.scoreTechnology},{subject_scores.scoreEnglish},{subject_scores.scoreArt},{subject_scores.scoreMath}" 

        user_data = user_data_string.split(",") # split the user_data string into a list of strings at each comma. This will create a list of strings. The first item in the list will be the username, and the rest of the items will be the scores.

        print(f"User Data: {user_data}\n") # print the user_data list


        if validate_name(user_data): # if validate_name(user_data) == True:
            print("Data is valid!")
            break # break out of the while loop if data is valid
    print("Data is ready to be uploaded to Google Sheets.\n")
    return user_data # return the user_data list
  
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

def update_worksheet(data, worksheet):
    """
    Receives a list of strings and integers to be inserted into a worksheet.
    Update the worksheet with the data provided.
    """
    from run import SHEET
    print(f"Updating {worksheet} worksheet...\n")
    worksheet_to_update = SHEET.worksheet(worksheet) # access the relevant worksheet
    print(f"Data to be inserted: {data}\n")
    worksheet_to_update.append_row(data) # append the test user values provided as a new row at the bottom of the relevant worksheet
    print(f"{worksheet} worksheet updated successfully.\n")

def get_high_score_leaderboard():
    """
    Collects columns of data from score worksheet, collecting the last 5 entries for each sandwich and returns the data as a list of lists.

    “Prettytable.” PyPI, 11 Sept. 2023, pypi.org/project/prettytable/. Accessed 1 Oct. 2023.
    """
    from run import SHEET

    worksheet = SHEET.worksheet('score')  # Replace 'Sheet1' with your worksheet name.
    
    data = worksheet.get_all_values() # Read data from Google Sheet

    table = PrettyTable() # Create a PrettyTable object

    table.field_names = data[0] # Set the field names based on the first row of data (assuming it's the header row)

    for row in data[1:]: # Populate PrettyTable with data. 1 means start at index 1, which is the second row. This is because the first row is the header row.
        table.add_row(row)

    table.sortby = "Score" # Sort the table by the Total column, in ascending order
    table.reversesort = True # Reverse the order of the sort, so it's descending

    print(table) # Print the PrettyTable

    #TODO: 1 insert dummy data into the Rank column from a string

    return 

def leaderboardMain(subject_scores, username_str): #leaderboardmain() uses the subject_scores variable
    """
    Run all program functions
    """
    print("Welcome to the leaderboard!")
    # subject_scores = SubjectScore(0,0,0,0,0,0) # create a SubjectScore object and store it in a variable called subject_scores
    data = get_user_data(subject_scores, username_str)  # call the get_user_data function and store the returned data in a variable called data
    print(f"Data provided: {data}\n")
    user_data = data  # convert the data provided by the user into integers. num is a variable that represents each item in the list data. 
    print(f"User Data:{user_data}") 
    update_worksheet(user_data, "score")  # call the update_worksheet function with user_data as a list
    get_high_score_leaderboard()  # call the get_high_score_leaderboard function and store the returned data in a variable called score_columns
 

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