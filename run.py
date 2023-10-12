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
subprocess.check_call([sys.executable, "-m", "pip", "install", "termcolor"])
os.system('cls' if os.name == 'nt' else 'clear') # Clear the terminal screen
from google.oauth2.service_account import Credentials
from pprint import pprint
from prettytable import PrettyTable
from termcolor import colored, cprint
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
    username_str = input("Please note that your data will be collected from this test. To protect your privacy, please DO NOT provide your real name and instead provide an anonymous PSEUDONYM e.g. Birdy34, Koala25, Croc76 \n \n Enter your username here: ") # ask the user for their username
    if validate_name(username_str): 
            print("Data is valid!")
    while True:
        try:
            mainMenu()
            choice = int(input("Please enter your choice: "))
            if choice == 1:
                """redirects to personality quiz, which will then redirect to subject quiz"""
                start_personality_quiz(username_str)
                
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















# ------------------ Overall Structure of Quiz ------------------
# The user to go through the personality quiz, the subject quiz and leaderboard, and finally onto a personality report.

def start_personality_quiz(username_str):
    personality_quiz() #start the personality quiz
    print("\n$$$ end of quiz") 
    personalityResults(trait_scores) #once the while loop is complete, the personality results will be displayed.
    start_subject_quiz(username_str, trait_scores)

def start_subject_quiz(username_str, trait_scores):
    subject_scores = SubjectScore(0,0,0,0,0,0)
    subjectQuiz(subject_scores) #start the subject quiz
    print("\n$$$ end of subject quiz") # Display the user's answers
    start_data_handling(username_str, trait_scores, subject_scores)

def start_data_handling(username_str, trait_scores, subject_scores):
    dataHandling(username_str, trait_scores, subject_scores) # Upload the user's data to Google Sheets
    start_personality_report(username_str, trait_scores, subject_scores)

def start_personality_report(username_str, trait_scores, subject_scores):
    personalityReport(username_str, trait_scores, subject_scores) # Display the user's answers

# ------------------ ------------------------ ------------------









# ------------------ Personality Quiz Section ------------------
# This section goes through the personality quiz, which is based on the OCEAN personality test. The user will be asked 10 questions, and their answers will be used to determine their personality type.

def personality_quiz():
    random.shuffle(quiz_data["questions"]) # Shuffle the questions. “Python Random Shuffle() Method.” W3schools.com, 2023, www.w3schools.com/python/ref_random_shuffle.asp. Accessed 5 Oct. 2023.
    question_index = 0
    print(len(quiz_data["questions"]))
    print(f"question_index: {question_index}")
    ask_question(question_index)
    while question_index < len(quiz_data["questions"]): #“Python Len() Function.” W3schools.com, 2023, www.w3schools.com/python/ref_func_len.asp. Accessed 5 Oct. 2023. Len() function returns the number of items in an object. While the question index is less than the number of questions in the quiz_data dictionary, the loop will continue. Once the question index is equal to the number of questions in the quiz_data dictionary, the loop will stop.
        ask_question(question_index)
        question_index += 1
    
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


def personalityResults(trait_scores):
    """displays personality results, with option to render full results"""
    os.system('cls' if os.name == 'nt' else 'clear')# Clear the terminal screen
    print("\nTrait Scores in Percentage:")
    for trait, score in trait_scores.items():
        print(f"{trait}: {convert_score_to_percentage(score)}%")

    print("press any key to continue on to the subject quiz")
    input()

    












# ------------------ Subject Quiz Section ------------------
# In this section, the user will be asked 10 questions from each subject area with 4 multiple choice answers to choose from. The user will be given a score out of 10 for each subject area, and a total score out of 50.


def subjectQuiz(subject_scores):
    os.system('cls' if os.name == 'nt' else 'clear')# Clear the terminal screen
    print("We are now beginning the multiple choice test.")
    print("Let's Start with Science!\n")
    print(f"---------Question 1 of 10---------\n")
    amount = 10
    category = 17 #Category 17 is Science
    startQuestionNumber() #startQuestionNumber is a function that sets the question number to 1
    subject_scores.resetAllScores()
    topic = "Science"
    playQuiz(amount, category, subject_scores, topic) #
    
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

def playQuiz (amount: int, category: int, subject_scores: SubjectScore, topic) -> None:
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
                topic = "Science"
                subject_scores.updateScienceScore() # Update Science score
            elif category == 30:
                topic = "Technology"
                subject_scores.updateTechnologyScore() # Update Technology score
            elif category == 10:
                topic = "English"
                subject_scores.updateEnglishScore() # Update English score
                
            elif category == 25:
                topic = "Art"
                subject_scores.updateArtScore()
            elif category == 19:
                topic = "Math"
                subject_scores.updateMathScore()
                
            print(f"Correct! You answered: {correct_choice_text}\n")
            print("You have earned 1 point!")
            
            print(f"---------Question {question_number} of 10---------\n")
            
        else:
            if category == 17:
                topic = "Science"
            elif category == 30:
                topic = "Technology"
            elif category == 10:
                topic = "English"
            elif category == 25:
                topic = "Art"
            elif category == 19:
                topic = "Math"
            
            print(f"Incorrect. The correct answer is {correct_choice_text}\n")
            print(f"---------Section: {topic}---------")
            print(f"--------Question {question_number} of 10---------\n")
        
    print("$$$ End of function")


 

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















# ------------------ Data Handling Section ------------------
# In this section, the user's data from the quiz will be uploaded to Google Sheets, being appended to the bottom of a worksheet.
# This section is heavily adapted from the Code Institute Love Sandwiches project by Anna Greaves

def dataHandling(username_str, subject_scores, trait_scores): #dataHandling() uses the subject_scores variable
    """
    Run all program functions
    """
    data_OCEAN = getLocalDataFromUser_OCEAN(username_str, trait_scores)  # call the getLocalDataFromUser_STEAM function and store the returned data in a variable called data
    user_data_OCEAN = data_OCEAN  # convert the data provided by the user into integers. num is a variable that represents each item in the list data. 

    data_STEAM = getLocalDataFromUser_STEAM(username_str, subject_scores)  # call the getLocalDataFromUser_STEAM function and store the returned data in a variable called data
    user_data_STEAM = data_STEAM  # convert the data provided by the user into integers. num is a variable that represents each item in the list data. 
    

    print("$$$ getlocaldatafromuser functions have passed")
    print(type(user_data_OCEAN))  # This will print the type of user_data_OCEAN
    print(type(user_data_STEAM))  # This will print the type of user_data_STEAM
    input()
    pushToAPICloud(user_data_STEAM, "score", user_data_OCEAN, "personality")  # call the pushToAPICloud function with user_data as a list
    get_high_score_leaderboard()  # call the get_high_score_leaderboard function and store the returned data in a variable called score_columns

def getLocalDataFromUser_STEAM(username_str, subject_scores: SubjectScore) -> None:
    """
    Gets the score and username from user and returns the username. After passing this loop, the data is ready to be appended to the worksheet.
    """

    while True: # loop until valid data is provided
        user_data_string_STEAM = f"{username_str},{subject_scores.scoreTotal},{subject_scores.scoreScience},{subject_scores.scoreTechnology},{subject_scores.scoreEnglish},{subject_scores.scoreArt},{subject_scores.scoreMath}" #place high score data into user_data_string_STEAM variable
        user_data_STEAM = user_data_string_STEAM.split(",") # split the user_data string into a list of strings at each comma. This will create a list of strings. The first item in the list will be the username, and the rest of the items will be the scores.
        break # break out of the while loop
    return user_data_STEAM # return the user_data list

def getLocalDataFromUser_OCEAN(username_str, trait_scores) -> None:
    """
    Gets the score and username from user and returns the username. After passing this loop, the data is ready to be appended to the worksheet.
    """
    print(type(trait_scores))  # This will print the type of trait_scores
    print(trait_scores)  # This will print the value of trait_scores

    print("$$$ getLocalDataFromUser_OCEAN debug1")
    input()

    trait_scores_Openness_string = str(trait_scores["Openness"]) # convert the trait_scores["Openness"] value to a string
    trait_scores_Conscientiousness_string = str(trait_scores["Conscientiousness"]) # convert the trait_scores["Conscientiousness"] value to a string
    trait_scores_Extraversion_string = str(trait_scores["Extraversion"]) # convert the trait_scores["Extraversion"] value to a string
    trait_scores_Agreeableness_string = str(trait_scores["Agreeableness"]) # convert the trait_scores["Agreeableness"] value to a string
    trait_scores_Neuroticism_string = str(trait_scores["Neuroticism"]) # convert the trait_scores["Neuroticism"] value to a string

    print(type(trait_scores))  # This will print the type of trait_scores
    print(trait_scores)  # This will print the value of trait_scores

    print("$$$ getLocalDataFromUser_OCEAN debug2")
    input()
    
    while True: # loop until valid data is provided
        user_data_string_OCEAN = f"{username_str},{trait_scores_Openness_string},{trait_scores_Conscientiousness_string},{trait_scores_Extraversion_string},{trait_scores_Agreeableness_string},{trait_scores_Neuroticism_string}" #place high score data into user_data_string_OCEAN variable
        user_data_OCEAN = user_data_string_OCEAN.split(",")
        break # break out of the while loop

    print("$$$ getLocalDataFromUser_OCEAN debug3")
    input()
    return user_data_OCEAN # return the user_data list

def pushToAPICloud(data_STEAM, data_OCEAN):
    """
    Receives a list of strings and integers to be inserted into a worksheet.
    Update the worksheet with the data provided.
    """
    worksheet_to_update = SHEET.worksheet('score') # access the relevant worksheet
    worksheet_to_update.append_row(data_STEAM) # append the test user values provided as a new row at the bottom of the relevant worksheet
    worksheet_to_update = SHEET.worksheet('personality') # access the relevant worksheet
    worksheet_to_update.append_row(data_OCEAN) # append the test user values provided as a new row at the bottom

def get_high_score_leaderboard():
    """
    Prints highscore leaderboard from worksheet. Collects columns of data_STEAM from score worksheet.

    “Prettytable.” PyPI, 11 Sept. 2023, pypi.org/project/prettytable/. Accessed 1 Oct. 2023.
    """
    worksheet = SHEET.worksheet('score')  # Replace 'Sheet1' with your worksheet name.
    data_STEAM = worksheet.get_all_values() # Read data from Google Sheet
    table = PrettyTable
    table.field_names = data_STEAM[0] # Set the field names based on the first row of data (assuming it's the header row)
    for row in data_STEAM[1:]: # Populate PrettyTable with data. 1 means start at index 1, which is the second row. This is because the first row is the header row.
        table.add_row(row)
    table.sortby = "Score" # Sort the table by the Total column, in ascending order
    table.reversesort = True # Reverse the order of the sort, so it's descending
    print(table) # Print the PrettyTable
    
    print("Above is your subject score, sorted by total score.")
    print("Press any key to continue on to your Personality Report")
    input()
    os.system('cls' if os.name == 'nt' else 'clear') # Clear the terminal screen

    return 













def personalityReport(username_str, trait_scores, subject_scores):
    """
    This personality report summarises the users personality traits and provides a recommendation for a career path.

    It goes through a series of if statements to determine the user's personality type, and then prints the relevant report.

    1. Retrieve the tables from OCEAN and STEAM
    2. Process the data, identify the individual user's highest score in what category. 
    3. Identify the OCEAN top % and STEAM rank.
    4. Print the report with the collected variables.
    5. Offer to Restart the programme.
    """ 
    os.system('cls' if os.name == 'nt' else 'clear') # Clear the terminal screen
    print("Welcome to your final personality report!")
    print("We're going to look at your personality traits and recommend a career path for you.")
    print("Press any key to continue")
    input()
    os.system('cls' if os.name == 'nt' else 'clear') # Clear the terminal screen
    generate_comparison_data_main()
    
def generate_comparison_data_main():
    """
    [x] calculate user's highest steam score
    [x] calculate user's highest ocean score
    [x] calculate user's relative rank from highest STEAM score e.g. "you came 3rd in science"
    [x] calculate user's percentage of highest score in OCEAN. e.g. "our data suggests you were in the top 13% of Openness"
    [x] suggest a career based on the user's highest STEAM score
    [x] suggest what kind of environment the user would thrive in based on their highest OCEAN score
    """
    highest_category = calculateHighestSTEAMScore()
    calculateSTEAMRank(highest_category)
    highest_category = calculateHighestOCEANScore()
    calculateOCEANPercentage(highest_category)
    assignOCEAN_STEAM_feedback(highest_category)

def calculateHighestSTEAMScore(username_str):
    worksheet = SHEET.worksheet('score')  # Access worksheet
    data = worksheet.get_all_values()  # Read data
    table = PrettyTable()  # Create PrettyTable object
    table.field_names = data[0]  # Set field names
    all_user_info = []
    for row in data[1:]:  # Populate table and collect user info
        table.add_row(row)
        userinfo = dict(zip(table.field_names, row))
        all_user_info.append(userinfo)
    localuser_data = next((item for item in all_user_info if item["Username"] == username_str), None)    # Filter out the data for username
    if localuser_data:
        # Extract STEAM scores and find the highest category
        steam_categories = ["S", "T", "E", "A", "M"]
        highest_score = -1
        highest_category = ""
        for category in steam_categories:
            score = int(localuser_data[category])
            if score > highest_score:
                highest_score = score
                highest_category = category
            if highest_category == "S":
                highest_category = "Science"
            elif highest_category == "T":
                highest_category = "Technology"
            elif highest_category == "E":
                highest_category = "English"
            elif highest_category == "A":
                highest_category = "Art"
            elif highest_category == "M":
                highest_category = "Maths"
        
        
    else:
        print(f"Username {username_str} not found")

    return highest_category

    #“How to Sort a List of Dictionaries by a Value of the Dictionary in Python?” Stack Overflow, 2023, stackoverflow.com/questions/72899/how-to-sort-a-list-of-dictionaries-by-a-value-of-the-dictionary-in-python. Accessed 5 Oct. 2023.
    #“Sort a List of Objects in Python | FavTutor.” FavTutor, 2022, favtutor.com/blogs/sort-list-of-objects-python. Accessed 5 Oct. 2023.

def calculateHighestOCEANScore(username_str):
    worksheet = SHEET.worksheet('personality')  # Access 'personality' worksheet
    data = worksheet.get_all_values()  # Read data
    table = PrettyTable()  # Create PrettyTable object
    table.field_names = data[0]  # Set field names
    all_user_info = []

    for row in data[1:]:  # Populate table and collect user info
        table.add_row(row)
        userinfo = dict(zip(table.field_names, row))
        all_user_info.append(userinfo)

    # Filter out the data for the specific username
    localuser_data = next((item for item in all_user_info if item["Username"] == username_str), None)

    if localuser_data:
        # Extract OCEAN scores and find the highest category
        ocean_categories = ["O", "C", "E", "A", "N"]
        highest_score = -1
        highest_category = ""

        for category in ocean_categories:
            score = int(localuser_data[category])
            if score > highest_score:
                highest_score = score
                highest_category = category
            if highest_category == "O":
                highest_category = "Openness"
            elif highest_category == "C":
                highest_category = "Conscientiousness"
            elif highest_category == "E":
                highest_category = "Extraversion"
            elif highest_category == "A":
                highest_category = "Agreeableness"
            elif highest_category == "N":
                highest_category = "Neuroticism"

    else:
        print(f"Username {username_str} not found")
    
    return highest_category

def calculateSTEAMRank(highest_category, username_str):
    worksheet = SHEET.worksheet('score')  # Access worksheet
    data = worksheet.get_all_values()  # Read data
    all_user_info = [dict(zip(data[0], row)) for row in data[1:]]  # Populate user info

    # Mapping from full category name to worksheet column abbreviation
    category_mapping = {
        "Science": "S",
        "Technology": "T",
        "English": "E",
        "Art": "A",
        "Maths": "M"
    }
    category_abbr = category_mapping[highest_category]
    scores = [int(userinfo[category_abbr]) for userinfo in all_user_info]# Collect scores of all users in the highest STEAM category
    scores.sort(reverse=True)  # Sort scores in descending order
    localuser_data = next((item for item in all_user_info if item["Username"] == username_str), None) # Get the user's score in the highest category
    if localuser_data:
        user_score = int(localuser_data[category_abbr])
    else:
        print(f"Username {username_str} not found")
        return
    # Find the user's rank
    user_rank = scores.index(user_score) + 1  # +1 to convert from 0-based to 1-based indexing
    ordinal_suffixes = {1: 'st', 2: 'nd', 3: 'rd'}
    # I'm checking for 10-20 because those are the digits that
    # don't follow the normal counting scheme.
    if 10 <= user_rank % 100 <= 20:
        ordinal_suffix = 'th'
    else:
        ordinal_suffix = ordinal_suffixes.get(user_rank % 10, 'th') # the second parameter is a default.
    print(f"You came {user_rank}{ordinal_suffix} in {highest_category}")

def calculateOCEANPercentage(highest_category, username_str):
    worksheet = SHEET.worksheet('personality')  # Access 'personality' worksheet
    data = worksheet.get_all_values()  # Read data
    all_user_info = [dict(zip(data[0], row)) for row in data[1:]]  # Populate user info
    category_mapping = {# Mapping from full category name to worksheet column abbreviation
        "Openness": "O",
        "Conscientiousness": "C",
        "Extraversion": "E",
        "Agreeableness": "A",
        "Neuroticism": "N"
    }
    category_abbr = category_mapping[highest_category]
    scores = [int(userinfo[category_abbr]) for userinfo in all_user_info]# Collect scores of all users in the highest OCEAN category
    scores.sort(reverse=True)  # Sort scores in descending order
    localuser_data = next((item for item in all_user_info if item["Username"] == username_str), None) # Get the user's score in the highest category
    if localuser_data:
        user_score = int(localuser_data[category_abbr]) 
    else:
        print(f"Username {username_str} not found")
        return
    user_index = scores.index(user_score)# Find the user's index in the sorted list
    percentage_rank = (1 - (user_index / len(scores))) * 100 # Calculate the user's percentage rank
    print(f"Our data suggests you were in the top {percentage_rank:.2f}% of {highest_category}")

def assignOCEAN_STEAM_feedback(highest_category):
    with open('finalreport_feedback_database.json', 'r') as file:
        feedback_database = json.load(file) # Call the previously defined functions to get the highest STEAM and OCEAN categories. for JSON file .load see “Json.load in Python.” GeeksforGeeks, GeeksforGeeks, 12 Mar. 2020, www.geeksforgeeks.org/json-load-in-python/. Accessed 8 Oct. 2023.
    highest_STEAM_category = calculateHighestSTEAMScore()
    highest_OCEAN_category = calculateHighestOCEANScore()
    print(f"Your highest STEAM category is {highest_STEAM_category}")
    print(f"Your highest OCEAN category is {highest_OCEAN_category}")
    print(f"Based on your results, we suggest you consider a career in {highest_STEAM_category}")
    print("Here is some feedback based on your results:")
    combined_ID = f"{highest_STEAM_category} and {highest_OCEAN_category}" # Combine the two categories to create a unique ID for the feedback. This is because the feedback is stored in a dictionary, and the dictionary keys must be unique.
    feedback = feedback_database.get(combined_ID, {}).get('feedback', 'Feedback not found') # Retrieve the relevant feedback from the database, for .get see “Python Dictionary get() Method.” W3Schools, www.w3schools.com/python/ref_dictionary_get.asp. Accessed 8 Oct. 2023.
    print(feedback)  # Print the feedback or return it as needed
    





















main()