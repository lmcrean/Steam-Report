from google.oauth2.service_account import Credentials
from pprint import pprint
import os
import sys
import subprocess
import json
import gspread
import requests
import html
import random


def install_libraries():
    subprocess.check_call(
        [sys.executable, "-m", "pip", "install", "prettytable"]
    )
    subprocess.check_call(
        [sys.executable, "-m", "pip", "install", "termcolor"]
    )


def import_libraries():
    global PrettyTable, colored, cprint
    from prettytable import PrettyTable
    from termcolor import colored, cprint
    os.system('cls' if os.name == 'nt' else 'clear')


install_libraries()
import_libraries()


x = PrettyTable()

SCOPE = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive.file',
    'https://www.googleapis.com/auth/drive'
]

"""
Adapted from gspread tutorial 'Love Sandwiches' by Anna Greaves/ Code Institute
creds.json is a file that is not pushed to github.
creds.with_scopes is a method that takes in the scope variable.
The SCOPE variable is a list of API's that we want to access.
gspread.authorize is a method that takes in the SCOPED_CREDS variable.
This variable is the credentials we created to access the API's.
"""
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Steam_Test')  # name of the spreadsheet


"""
For personality test, initialize variables including trait scores.
“Json.load in Python.” GeeksforGeeks, GeeksforGeeks, 12 Mar. 2020,
www.geeksforgeeks.org/json-load-in-python/. Accessed 5 Oct. 2023.
"""
with open("personality_statements.json", "r") as file:  # r = read.
    quiz_data = json.load(file)  # Load the questions from the JSON file.
user_answers = []
trait_scores = {
    "Openness": 0,
    "Conscientiousness": 0,
    "Extraversion": 0,
    "Agreeableness": 0,
    "Neuroticism": 0
}


# For subject test, initialize variables including subject scores.
class SubjectScore:
    """
    Update the score in the local variable,
    adding 1 point for each correct answer.
    """
    def __init__(
            self,
            scoreScience,
            scoreTechnology,
            scoreEnglish,
            scoreArt,
            scoreMath,
            scoreTotal):
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
        return (
            self.scoreScience,
            self.scoreTechnology,
            self.scoreEnglish,
            self.scoreArt,
            self.scoreMath,
            self.scoreTotal
        )


def mainMenu():
    """
    The main menu of the game
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    cprint("Welcome to your Steam Report!", 'white', 'on_blue', attrs=['bold'])
    print("We're going to test your personality and run a quiz to help with")
    print("your career choices. To do this you will take an OCEAN Personality Test,")
    print("and test your knowledge on the STEAM subjects.\n")
    print("At the end of the test you'll get a customized personality report.\n")

    cprint("Please select an option from the menu below:", 'yellow')
    cprint("1 - Start", 'light_green', attrs=['bold'])
    print("2 - About the OCEAN Personality Test")
    print("3 - About the STEAM Subjects")
    print("4 - How to Play")
    print("5 - How it works")



def main():
    """
    run all program functions, starting with the main menu. Plays the game.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    cprint("Welcome to your Steam Report!", 'white', 'on_blue', attrs=['bold'])
    print("We're going to test your personality and run a quiz to help with")
    print("your career choices. To do this you will take an OCEAN Personality Test,")
    print("and test your knowledge on the STEAM subjects.\n")
    print("At the end of the test you'll get a customized personality report.\n")
    print("Please note that your data will be collected from this test.")
    cprint("To protect your privacy, please DO NOT provide your real name.", 'red')
    cprint("instead provide an anonymous PSEUDONYM", 'light_green')
    cprint("e.g. Birdy34, Koala25, Croc76 \n\n", 'light_green')
    # ask the user for their username
    username_str = input("Enter your username here: ")
    validate_name(username_str)
    os.system('cls' if os.name == 'nt' else 'clear')
    cprint("Username is Valid!", 'white', 'on_blue', attrs=['bold'])
    usernamemsg = "Your username is: " + username_str
    cprint(f"{usernamemsg}", attrs=['bold'])
    print("Please confirm this is not your real name.\n")
    cprint("1 - confirm", 'light_green', attrs=['bold'])
    print("2 - input again")
    choice = int(input("Please enter your choice: "))
    if choice == 1:
        mainMenu()
    elif choice == 2:
        main()
    else:
        print("Please enter a number between 1 and 2.")
    while True:
        try:
            mainMenu()
            choice = int(input("Please enter your choice: "))
            if choice == 1:
                """
                redirects to personality quiz,
                which will then redirect to subject quiz
                """
                print(username_str, "main")
                start_personality_quiz(username_str)
            elif choice == 2:
                os.system('cls' if os.name == 'nt' else 'clear')
                cprint("About the OCEAN Personality Test.",
                       'white', 'on_blue', attrs=['bold'])
                print("The OCEAN Test measures the Big 5 personality traits:")
                print("Openness, Conscientiousness, Extraversion, Agreeableness,")
                print("and Neuroticism. These traits are key in various work")
                print("settings, affecting teamwork, stress management, and more.\n")
                print("press any key to go back to the menu")
                input()
            elif choice == 3:
                os.system('cls' if os.name == 'nt' else 'clear')
                cprint("About the STEAM Subject Quiz.",
                      'white', 'on_blue', attrs=['bold'])
                print("The STEAM Quiz covers Science, Technology, English,")
                print("Art, and Math, which correspond to a broad range of careers.")
                print("This helps in identifying your strengths for career choices.")
                print("\npress any key to go back to the menu")
                input()
            elif choice == 4:
                os.system('cls' if os.name == 'nt' else 'clear')
                cprint("How to Play",
                      'white', 'on_blue', attrs=['bold'])
                print("Follow on-screen instructions for each quiz.")
                print("For the Personality Quiz, you'll choose options from 1-9.")
                print("For the STEAM Quiz, you'll choose options from 1-4.")
                print("\npress any key to go back to the menu")
                input()
            elif choice == 5:
                os.system('cls' if os.name == 'nt' else 'clear')
                cprint("How it Works:",
                       'white', 'on_blue', attrs=['bold'])
                print("The test identifies your strongest areas in both")
                print("OCEAN and STEAM, and uses these to make career")
                print("recommendations tailored to your strengths.")
                table = PrettyTable()
                table.field_names = [" ", "S", "T", "E", "A", "M"]
                table.add_row(["O", " ", " ", " ", " ", " "])
                table.add_row(["C", " ", " ", " ", " ", " "])
                table.add_row(["E", " ", " ", " ", " ", ":)"])
                table.add_row(["A", " ", " ", " ", " ", " "])
                table.add_row(["N", " ", " ", " ", " ", " "])
                print(table)
                print("For example, if your strongest areas are")
                print("Extraversion and Maths, then your career choices")
                print("will be tailored to these areas.")
                print("\npress any key to go back to the menu")
                input()
            else:
                print("Please enter a number between 1 and 5.")
        except ValueError:
            print("Please enter a number between 1 and 5.")


def validate_name(username_str):
    """
    The name cannot be more than 9 characters long.
    """
    if len(username_str) > 9:
        print(
            f"Invalid name: {username_str}.\n"
            "The name cannot be more than 9 characters long.\n"
            "Please enter a name that is less than 9 characters long.\n"
            "For example, Birdy34, Koala25, Croc76\n"
            "press any key to try again\n"
        )
        input()
        main()
        
    elif len(username_str) < 3:
        print(
            f"Invalid name: {username_str}.\n"
            "The name cannot be less than 3 characters.\n"
            "Please enter a name that is more than 3 characters long.\n"
            "For example, Birdy34, Koala25, Croc76\n"
            "press any key to try again\n"
        )
        input()
        main()
    else:
        cprint("Username is valid!\n", 'green')
        username_str = username_str
    return username_str  # return True if noerrors are raised.
    # The function will return True if the try block is successful.
    # If unsuccessful, the except block will run and return False.
    # For example, if the user enters 10 chracaters instead of 9,
    # the except block will run and return False.

# ------------------ Overall Structure of Quiz ------------------


"""
The user to go through the personality quiz,
the subject quiz and leaderboard,
then finally onto a personality report.
"""


def start_personality_quiz(username_str):
    """
    This function starts the personality quiz.
    username_str is carried through the function to the end.
    results are stored in trait_scores.
    At the end it is redirected to the subject quiz.
    """
    personality_quiz()  # start the personality quiz
    personalityResults(trait_scores)  # display the user's answers
    start_subject_quiz(username_str, trait_scores)


def start_subject_quiz(username_str, trait_scores):
    """
    This function starts the subject quiz.
    username_str and trait_scores are carried through
    the function to the end.
    results of quiz are stored in subject_scores.
    At the end it is redirected to the data handling section.
    """
    # initialize subject scores
    subject_scores = SubjectScore(0, 0, 0, 0, 0, 0)
    subjectQuiz(subject_scores)  # start the subject quiz
    start_data_handling(username_str, trait_scores, subject_scores)


def start_data_handling(username_str, trait_scores, subject_scores):
    """
    begins data handling section.
    username_str, trait_scores and subject_scores are carried
    through the parameters. The data is stored in the google sheet API.
    At the end it is redirected to the personality report.
    """
    dataHandling(username_str, trait_scores, subject_scores)
    start_personality_report(username_str, trait_scores, subject_scores)


def start_personality_report(username_str, trait_scores, subject_scores):
    """
    displays a final report, indicating best option.
    username_str, trait_scores and subject_scores are carried through.
    the final report
    """
    personalityReport(username_str, trait_scores, subject_scores)
    # Display the user's answers

# ------------------ ------------------------ ------------------

# ------------------ Personality Quiz Section ------------------


"""This section goes through the personality quiz,
which is based on the OCEAN personality test.
The user will be asked 10 questions,
and their answers will be used to determine their personality type."""


def personality_quiz():
    """
    This function starts the personality quiz.
    The user will be asked 25 questions, which are shuffled randomly.
    """
    random.shuffle(quiz_data["questions"])  # Shuffle the questions.
    # “Python Random Shuffle() Method.” W3schools.com, 2023,
    # www.w3schools.com/python/ref_random_shuffle.asp.
    # Accessed 5 Oct. 2023.
    question_index = 0
    ask_question(question_index)
    while question_index < len(quiz_data["questions"]) - 1:
        # “Python Len() Function.” W3schools.com, 2023,
        # www.w3schools.com/python/ref_func_len.asp.
        # Accessed 5 Oct. 2023.
        # Len() function returns the number of
        # items in an object. While the question index is less than
        # the number of questions in the quiz_data dictionary,
        # the loop will continue. Once the question index is equal to
        # the number of questions in the quiz_data dictionary,
        # the loop will stop.
        question_index += 1  # adds one to the question index,
        # so that the next question is asked.
        # “Python Increment and Decrement Operators.”
        # W3schools.com, 2023,
        # www.w3schools.com/python/python_operators.asp. Accessed 5 Oct. 2023.
        ask_question(question_index)


def ask_question(question_index):
    """
    Ask the user a question about their personality
    and get their response.

    The question_index indicates the question number in the
    quiz_data dictionary.

    “Python Function Arguments.” W3schools.com, 2023,
    www.w3schools.com/python/gloss_python_function_arguments.
    asp#:~:text=A%20parameter%20is%20the%20variable,
    function%20when%20it%20is%20called. Accessed 5 Oct. 2023.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    cprint("OCEAN Personality Test", 'white', 'on_blue', attrs=['bold'])
    question = quiz_data["questions"][question_index]
    print(f"Question {question_index + 1}:")
    cprint(question["statement"], attrs=['bold'])

    while True:
        red_option = colored("1 = Strongly Disagree", 'light_red')
        amber_option = colored("5 = Neutral", 'light_yellow')
        green_option = colored("9 = Strongly Agree", 'light_green')

        response = input(
            f"Please enter a number from 1 to 9."
            f"\n({red_option}, {amber_option}, {green_option}):\n"
        )
        try:
            response = int(response)  # Convert to an integer
            if 1 <= response <= 9:
                user_answers.append(response)  # Add the response to
                # ...the user's answers
                trait_scores[question["trait"]] += response  # Add the response
                # ...to the corresponding trait score
                break  # Exit the loop when a valid response is provided
            else:
                print(
                    "Invalid response."
                    "Please enter a number between 1 and 9."
                    )
        except ValueError:
            print(
                "Invalid response."
                "Please enter a number between 1 and 9."
                )


def convert_score_to_percentage(score):
    """
    Convert a personality trait score between 5 and 45 to a percentage.
    The trait score should be between 5 and 45.
    Returns The percentage equivalent of the trait score.
    """
    if 5 <= score <= 45:
        percentage = ((score - 5) / 40) * 100
        return round(percentage, 1)  # “Python Round() Function.”
        # W3schools.com, 2023, www.w3schools.com/python/ref_func_round.asp.
        # Accessed 5 Oct. 2023.
    else:
        return "Invalid score. It should be between 5 and 45."


def personalityResults(trait_scores):
    """displays personality results, with option to render full results"""
    os.system('cls' if os.name == 'nt' else 'clear')
    cprint("OCEAN Personality Test Results", 'white', 'on_blue', attrs=['bold'])
    print("\nTrait Scores in Percentage:")
    for trait, score in trait_scores.items():
        print(f"{trait}: {convert_score_to_percentage(score)}%")
    highest_trait = max(trait_scores, key=trait_scores.get)
    cprint("\nyou scored highest in: " + highest_trait, 'green', attrs=['bold'])
    print("\npress any key to continue on to the subject quiz")
    input()

# ------------------ Subject Quiz Section ------------------


"""
In this section, the user will be asked 10 questions from each subject area
with 4 multiple choice answers to choose from. The user will be given a score
out of 10 for each subject area, and a total score out of 50.
"""


def subjectQuiz(subject_scores):
    os.system('cls' if os.name == 'nt' else 'clear')
    topic = "Science"
    amount = 10
    category = 17  # Category 17 is Science
    startQuestionNumber()  # sets the question number to 1
    subject_scores.resetAllScores()
    playQuiz(amount, category, subject_scores, topic)
    topic = "Technology"  # next topic
    amount = 10
    category = 30  # Category 30 is Technology
    startQuestionNumber()
    playQuiz(amount, category, subject_scores, topic)
    topic = "English"  # next topic
    amount = 10
    category = 10  # Category 10 is Books
    startQuestionNumber()
    playQuiz(amount, category, subject_scores, topic)
    topic = "Art"  # next topic
    amount = 10
    category = 25  # Category 25 is Art
    startQuestionNumber()
    playQuiz(amount, category, subject_scores, topic)
    topic = "Math"  # next topic
    amount = 10
    category = 19  # Category 19 is Math
    startQuestionNumber()
    playQuiz(amount, category, subject_scores, topic)
    finalSTEAMScore(subject_scores)
    os.system('cls' if os.name == 'nt' else 'clear')


def getTriviaQuestions(amount: int, category: int) -> list:
    """
    Get trivia questions from the json file
    """
    url = (
        "https://opentdb.com/api.php?"
        f"amount=10&category={category}&type=multiple"
    )
    response = requests.get(url)
    response_json = response.json()
    return response_json["results"]


def shuffleAnswerChoices(choices: list) -> list:
    """
    credit to walkthrough: "Quiz App Using API Data - Python Project.”
    Run That, 16 May 2023,
    www.runthat.blog/quiz-app-using-api-data-python-project/.
    Accessed 24 Sept. 2023.
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
    credit to walkthrough: "Quiz App Using API Data - Python Project.”
    Run That, 16 May 2023,
    www.runthat.blog/quiz-app-using-api-data-python-project/.
    Accessed 24 Sept. 2023.
    """
    question_number += 1
    if question_number > 10:
        question_number = 1
    return question_number


def printAnswerChoices(question_number: int, choices: list) -> None:
    """
    credit to walkthrough: "Quiz App Using API Data - Python Project.”
    Run That, 16 May 2023,
    www.runthat.blog/quiz-app-using-api-data-python-project/.
    Accessed 24 Sept. 2023.
    """
    for choice_index, choice in enumerate(choices):
        print(f"{choice_index+1}. {html.unescape(choice)}")


def getUserAnswer() -> int:
    """
    Get user input and ensure it's a valid number between 1 and 4.

    Adapted heavily from walkthrough:
    credit to walkthrough: "Quiz App Using API Data - Python Project.”
    Run That, 16 May 2023,
    www.runthat.blog/quiz-app-using-api-data-python-project/.
    Accessed 24 Sept. 2023.
    """
    while True:
        user_input = input("Enter the number of your choice: ")
        if not user_input:  # Check if the input is empty
            print("Empty input. Enter a number between 1 and 4")
            continue  # Continue the loop without processing further
        try:
            user_choice = int(user_input)
            if user_choice in range(1, 5):  # 1,2,3, or 4
                return user_choice - 1
            else:
                print("Invalid input. Enter a number between 1 and 4")
        except ValueError:
            print("Invalid input with Value error.")
            print("Enter a number between 1 and 4")


def playQuiz(
        amount: int,
        category: int,
        subject_scores: SubjectScore,
        topic: str) -> None:
    """
    Adapted heavily from walkthrough:
    "Quiz App Using API Data - Python Project.”
    Run That, 16 May 2023,
    www.runthat.blog/quiz-app-using-api-data-python-project/.
    Accessed 24 Sept. 2023.
    """
    
    question_pool = getTriviaQuestions(amount, category)  # Get the questions
    question_number = startQuestionNumber()  # Initialize question_number
    for question in question_pool:  # Loop through the questions
        cprint("STEAM Quiz", 'white', 'on_blue', attrs=['bold'])
        sectiontext= f"---------Section: {topic}---------"
        cprint(f"{sectiontext}", 'yellow', attrs=['bold'])
        print(f"---------Question {question_number} of 10---------")
        if topic == "Science":
            print(f"         Topic score: {subject_scores.scoreScience}\n")
        elif topic == "Technology":
            print(f"         Topic score: {subject_scores.scoreTechnology}\n")
        elif topic == "English":
            print(f"         Topic score: {subject_scores.scoreEnglish}\n")
        elif topic == "Art":
            print(f"         Topic score: {subject_scores.scoreArt}\n")
        elif topic == "Math":
            print(f"         Topic score: {subject_scores.scoreMath}\n")
        # Get the question text:
        question_text = html.unescape(question["question"])
        cprint(question_text, attrs=['bold']) # Print the question
        choices = question["incorrect_answers"]  # Get the incorrect answers
        # Add the correct answer to the choices list:
        choices.extend([question["correct_answer"]])
        question_number = trackQuestionNumber(question_number)  # Next question
        shuffled_choices = shuffleAnswerChoices(choices)  # Shuffle the choices
        printAnswerChoices(question_number, shuffled_choices)  # Print choices
        user_choice_index = getUserAnswer()  # Get the user's answer
        # Get the user's choice text:
        user_choice_text = shuffled_choices[user_choice_index]
        # Get the correct choice text:
        correct_choice_text = html.unescape(question["correct_answer"])
        os.system('cls' if os.name == 'nt' else 'clear')
        if user_choice_text == correct_choice_text:  # If user was correct...
            subject_scores.updateTotalScore()
            # Update Total score
            if category == 17:
                topic = "Science"
                subject_scores.updateScienceScore()
                # Update Science score
            elif category == 30:
                topic = "Technology"
                subject_scores.updateTechnologyScore()
                # Update Technology score
            elif category == 10:
                topic = "English"
                subject_scores.updateEnglishScore()
                # Update English score
            elif category == 25:
                topic = "Art"
                subject_scores.updateArtScore()
            elif category == 19:
                topic = "Math"
                subject_scores.updateMathScore()
            cprint(f"Correct! You answered: {correct_choice_text}", 'green')
            cprint("You have earned 1 point!\n", 'green')
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
            cprint(f"Incorrect. The correct answer is {correct_choice_text}\n", 'red')


def getTriviaQuestions(amount: int, category: int) -> list:
    """
    Get trivia questions from the json file
    """
    url = (
        "https://opentdb.com/api.php?"
        f"amount=10&category={category}&type=multiple"
        )
    response = requests.get(url)
    response_json = response.json()
    return response_json["results"]


def shuffleAnswerChoices(choices: list) -> list:
    """
    credit to walkthrough:
    "Quiz App Using API Data - Python Project.”
    Run That, 16 May 2023,
    www.runthat.blog/quiz-app-using-api-data-python-project/.
    Accessed 24 Sept. 2023.
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
    credit to walkthrough:
    "Quiz App Using API Data - Python Project.”
    Run That, 16 May 2023,
    www.runthat.blog/quiz-app-using-api-data-python-project/.
    Accessed 24 Sept. 2023.
    """
    question_number += 1
    if question_number > 10:
        question_number = 1
    return question_number


def printAnswerChoices(question_number: int, choices: list) -> None:
    """
    credit to walkthrough:
    "Quiz App Using API Data - Python Project.”
    Run That, 16 May 2023,
    www.runthat.blog/quiz-app-using-api-data-python-project/.
    Accessed 24 Sept. 2023.
    """
    for choice_index, choice in enumerate(choices):
        print(f"{choice_index+1}. {html.unescape(choice)}")


def getUserAnswer() -> int:
    """
    Get user input and ensure it's a valid number between 1 and 4.
    Adapted heavily from walkthrough:
    "Quiz App Using API Data - Python Project.”
    Run That, 16 May 2023,
    www.runthat.blog/quiz-app-using-api-data-python-project/.
    Accessed 24 Sept. 2023.
    """
    while True:
        user_input = input("Enter the number of your choice: ")
        if not user_input:  # Check if the input is empty
            print("Empty input. Enter a number between 1 and 4")
            continue  # Continue the loop without processing further
        try:
            user_choice = int(user_input)
            if user_choice in range(1, 5):  # 1,2,3, or 4
                return user_choice - 1
            else:
                print("Invalid input. Enter a number between 1 and 4")
        except ValueError:
            print("Invalid input with Value error.")
            print("Enter a number between 1 and 4")

def finalSTEAMScore(subject_scores):
    """
    Displays the final STEAM score
    """
    cprint("STEAM Quiz Results\n", 'white', 'on_blue', attrs=['bold'])
    print(f"Science: {subject_scores.scoreScience}/10")
    print(f"Technology: {subject_scores.scoreTechnology}/10")
    print(f"English: {subject_scores.scoreEnglish}/10")
    print(f"Art: {subject_scores.scoreArt}/10")
    print(f"Math: {subject_scores.scoreMath}/10 \n")
    print(f"(Total: {subject_scores.scoreTotal}/50) \n")
    # Finding the highest score
    subject_dict = {
        'Science': subject_scores.scoreScience,
        'Technology': subject_scores.scoreTechnology,
        'English': subject_scores.scoreEnglish,
        'Art': subject_scores.scoreArt,
        'Math': subject_scores.scoreMath
    }
    highest_subject = max(subject_dict, key=subject_dict.get)
    highest_msg = f"you scored highest in: {highest_subject}"
    cprint(highest_msg, 'green', attrs=['bold'])
    print("\npress any key to continue on to the final report")
    input()

# ------------------ Data Handling Section ------------------


"""
In this section, the user's data from the quiz will be uploaded to
Google Sheets, being appended to the bottom of a worksheet.
"""


def dataHandling(username_str, trait_scores, subject_scores):
    """
    Run all program functions. The parameters carry unique data from the tests.
    This section retrieves Local data and stores it in local variables.
    """
    data_OCEAN = getLocalDataFromUser_OCEAN(username_str, trait_scores)
    data_STEAM = getLocalDataFromUser_STEAM(username_str, subject_scores)
    # call the pushToAPICloud function with formatted local variables ready:
    pushToAPICloud(data_STEAM, data_OCEAN)
    # call the get_high_score_leaderboard function
    # and store the returned data in a variable called score_columns:
    


def getLocalDataFromUser_STEAM(
        username_str,
        subject_scores: SubjectScore
        ) -> None:
    """
    Gets the score and username from user and returns the username.
    After passing this loop, the data is ready to be appended to the worksheet.
    user_data_string_STEAM compiles the data
    into a single string seperated by commas.
    The first item in the list will be the username,
    and the rest of the items will be the scores.
    """

    while True:  # loop until valid data is provided
        user_data_string_STEAM = (
            f"{username_str},{subject_scores.scoreTotal},"
            f"{subject_scores.scoreScience},{subject_scores.scoreTechnology},"
            f"{subject_scores.scoreEnglish},{subject_scores.scoreArt},"
            f"{subject_scores.scoreMath}"
        )  # place high score data into user_data_string_STEAM variable
        user_data_STEAM = user_data_string_STEAM.split(",")
        break  # break out of the while loop
    return user_data_STEAM  # return the user_data list


def getLocalDataFromUser_OCEAN(username_str, trait_scores) -> None:
    """
    Gets the score and username from user and returns the username.
    After passing this loop, the data is ready to be appended to the worksheet.

    str() is used to convert into a string
    """
    trait_scores_Openness_string = str(trait_scores["Openness"])
    trait_scores_Conscientiousness_string = str(
        trait_scores["Conscientiousness"]
    )  # convert the trait_scores["Conscientiousness"] value to a string
    trait_scores_Extraversion_string = str(
        trait_scores["Extraversion"]
    )  # convert the trait_scores["Extraversion"] value to a string
    trait_scores_Agreeableness_string = str(
        trait_scores["Agreeableness"]
    )  # convert the trait_scores["Agreeableness"] value to a string
    trait_scores_Neuroticism_string = str(
        trait_scores["Neuroticism"]
    )  # convert the trait_scores["Neuroticism"] value to a string
    while True:  # loop until valid data is provided
        user_data_string_OCEAN = (
            f"{username_str},{trait_scores_Openness_string},"
            f"{trait_scores_Conscientiousness_string},"
            f"{trait_scores_Extraversion_string},"
            f"{trait_scores_Agreeableness_string},"
            f"{trait_scores_Neuroticism_string}"
        )  # place high score data into user_data_string_OCEAN variable
        user_data_OCEAN = user_data_string_OCEAN.split(",")
        break  # break out of the while loop
    return user_data_OCEAN  # return the user_data list


def pushToAPICloud(data_STEAM, data_OCEAN):
    """
    Receives a list of strings and integers to be inserted into a worksheet.
    Update the Google Sheets 'score' and 'personality' worksheet
    with the data provided.
    append_row Appends the test user values provided
    as a new row at the bottom of the relevant worksheet.
    """
    worksheet_to_update = SHEET.worksheet('score')
    worksheet_to_update.append_row(data_STEAM)
    worksheet_to_update = SHEET.worksheet('personality')
    worksheet_to_update.append_row(data_OCEAN)


def get_high_score_leaderboard(username_str):
    """
    Prints highscore leaderboard from worksheet.
    Collects columns of data_STEAM from score worksheet.

    “Prettytable.” PyPI, 11 Sept. 2023,
    pypi.org/project/prettytable/. Accessed 1 Oct. 2023.
    """
    cprint("STEAM Quiz Leaderboard", 'white', 'on_blue', attrs=['bold'])
    worksheet = SHEET.worksheet('score')
    data_STEAM = worksheet.get_all_values()  # Get all the data.
    table = PrettyTable()
    # Set the field names based on the first row of data:
    table.field_names = data_STEAM[0]
    for row in data_STEAM[1:]:  # 1 means start at index 1 which is second row.
        # ... This is because the first row is the header row.
        row[1] = int(row[1])  # converts Score string to integer,
        # this was a bug fix added later to help to order correctly
        table.add_row(row)
    table.sortby = "Score"  # Sort the table by the Total column
    # Reverse the order of the sort to descending order:
    table.reversesort = True
    print(table)  # Print the PrettyTable
    print(f"your username is: {username_str}")
    print("Above is your subject score, sorted by total score.")
    print("Press any key to go back the Main Menu")
    input()
    return


def personalityReport(username_str, trait_scores, subject_scores):
    """
    This personality report summarises the users personality traits
    and provides a recommendation for a career path.

    It goes through a series of if statements to determine the user's
    personality type, and then prints the relevant report.

    1. Retrieve the tables from OCEAN and STEAM
    2. Process the data, identify the individual user's highest score
    in what category.
    3. Identify the OCEAN top % and STEAM rank.
    4. Print the report with the collected variables.
    5. Offer to Restart the programme.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    welcomemsg = "Welcome to your final report!"
    cprint(f"{welcomemsg}", 'white', 'on_blue', attrs=['bold'])
    print("\nWe're going to look at your strongest personality traits") 
    print("and subject scores. Based on this data we will career path") 
    print("for you.\n")
    print("Press any key to continue")
    input()
    os.system('cls' if os.name == 'nt' else 'clear')
    generate_comparison_data_main(username_str)


def generate_comparison_data_main(username_str):
    """
    This main branch calls the functions to generate the comparison data for
    the user.
    """
    cprint("Your Final Report", 'white', 'on_blue', attrs=['bold'])
    highest_category = calculateHighestSTEAMScore(username_str)
    calculateSTEAMRank(highest_category, username_str)
    highest_category = calculateHighestOCEANScore(username_str)
    calculateOCEANPercentage(highest_category, username_str)
    assignOCEAN_STEAM_feedback(username_str)


def calculateHighestSTEAMScore(username_str):
    """
    calculates the highest STEAM score for the user and returns the category.
    """
    worksheet = SHEET.worksheet('score')  # Access worksheet
    data = worksheet.get_all_values()  # Read data
    table = PrettyTable()  # Create PrettyTable object
    table.field_names = data[0]  # Set field names
    all_user_info = []
    for row in data[1:]:  # Populate table and collect user info
        table.add_row(row)
        userinfo = dict(zip(table.field_names, row))
        all_user_info.append(userinfo)
    localuser_data = next(
        (item for item in all_user_info if item["Username"] == username_str),
        None
    )  # Filter out the data for username
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

    # “How to Sort a List of Dictionaries by a Value of the Dictionary
    # in Python?” Stack Overflow, 2023,
    # stackoverflow.com/questions/72899/
    # how-to-sort-a-list-of-dictionaries-by-a-value-of-the-dictionary-
    # in-python. Accessed 5 Oct. 2023.
    # “Sort a List of Objects in Python | FavTutor.” FavTutor, 2022,
    # favtutor.com/blogs/sort-list-of-objects-python.
    # Accessed 5 Oct. 2023.


def calculateHighestOCEANScore(username_str):
    """
    calculates the highest OCEAN score for the user and returns the category.
    """
    worksheet = SHEET.worksheet('personality')  # Access the worksheet
    data = worksheet.get_all_values()  # Read data
    table = PrettyTable()  # Create PrettyTable object
    table.field_names = data[0]  # Set field names
    all_user_info = []

    for row in data[1:]:  # Populate table and collect user info
        table.add_row(row)
        userinfo = dict(zip(table.field_names, row))
        all_user_info.append(userinfo)

    # Filter out the data for the specific username
    localuser_data = next(
        (item for item in all_user_info if item["Username"] == username_str),
        None
    )

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
    """
    takes the highest STEAM category and calculates the relative rank of STEAM
    total score for the user and returns the rank. e.g. 1st, 2nd, 3rd, 4th, 5th
    in Science.
    """
    worksheet = SHEET.worksheet('score')  # Access worksheet
    data = worksheet.get_all_values()  # Read data
    # Populate user info:
    all_user_info = [dict(zip(data[0], row)) for row in data[1:]]

    # Mapping from full category name to worksheet column abbreviation
    category_mapping = {
        "Science": "S",
        "Technology": "T",
        "English": "E",
        "Art": "A",
        "Maths": "M"
    }
    category_abbr = category_mapping[highest_category]
    # Collect scores of all users in the highest STEAM category:
    scores = [
        int(userinfo[category_abbr]) for userinfo in all_user_info
    ]
    scores.sort(reverse=True)  # Sort scores in descending order
    # Get the user's score in the highest category:
    localuser_data = next(
        (item for item in all_user_info if item["Username"] == username_str),
        None
    )
    if localuser_data:
        user_score = int(localuser_data[category_abbr])
    else:
        print(f"Username {username_str} not found")
        return
    # Find the user's rank from 1 - N
    # with +1 to convert from 0-based to 1-based indexing:
    user_rank = scores.index(user_score) + 1
    ordinal_suffixes = {1: 'st', 2: 'nd', 3: 'rd'}
    # I'm checking for 10-20 because those are the digits that
    # don't follow the normal counting scheme.
    if 10 <= user_rank % 100 <= 20:
        ordinal_suffix = 'th'
    else:
        ordinal_suffix = ordinal_suffixes.get(user_rank % 10, 'th')
        # the second parameter is a default.
    cprint("First, let's look at your STEAM results:", 'yellow', attrs=['bold'])
    print(f"Your highest STEAM category is {highest_category}")
    print(f"You came {user_rank}{ordinal_suffix} in {highest_category}\n")


def calculateOCEANPercentage(highest_category, username_str):
    """
    Takes the highest OCEAN category and calculates the relative percentage of
    OCEAN total score for the user and returns the percentage. e.g. top 10%
    in Openness.
    """
    worksheet = SHEET.worksheet('personality')  # Access personality worksheet
    data = worksheet.get_all_values()  # Read data
    # Populate user info:
    all_user_info = [dict(zip(data[0], row)) for row in data[1:]]
    category_mapping = {
        # Mapping from full category name to worksheet column abbreviation
        "Openness": "O",
        "Conscientiousness": "C",
        "Extraversion": "E",
        "Agreeableness": "A",
        "Neuroticism": "N"
    }
    category_abbr = category_mapping[highest_category]
    # Collect scores of all users in the highest OCEAN category:
    scores = [int(userinfo[category_abbr]) for userinfo in all_user_info]
    scores.sort(reverse=True)  # Sort scores in descending order
    # Get the user's score in the highest category
    localuser_data = next(
        (item for item in all_user_info if item["Username"] == username_str),
        None
    )
    if localuser_data:
        user_score = int(localuser_data[category_abbr])
    else:
        print(f"Username {username_str} not found")
        return
    # Find the user's index in the sorted list:
    user_index = scores.index(user_score)
    # Calculate the user's percentage rank:
    percentage_rank = (1 - (user_index / len(scores))) * 100
    cprint("Now let's look at your OCEAN results:", 'yellow', attrs=['bold'])
    print(f"Your highest OCEAN category is {highest_category}")
    print(
        f"Our data suggests you were in the top "
        f"{percentage_rank:.2f}% of {highest_category}\n"
    )


def assignOCEAN_STEAM_feedback(username_str):
    """
    assigns feedback based on the highest STEAM and OCEAN categories.
    Retrieves from the JSON database based on highest STEAM and OCEAN
    categories, which are (5x5=)25 possible combinations e.g. Science and
    Openness are highest category for the user, leading to a unique ID of
    Science and Openness. This ID is used to retrieve the feedback from the
    JSON database.
    """
    with open('finalreport_feedback_database.json', 'r') as file:
        feedback_database = json.load(file)  # Call the previously defined
        # functions to get the highest STEAM and OCEAN categories. for JSON
        # file .load see “Json.load in Python.” GeeksforGeeks, GeeksforGeeks,
        # 12 Mar. 2020, www.geeksforgeeks.org/json-load-in-python/.
        # Accessed 8 Oct. 2023.
    highest_STEAM_category = calculateHighestSTEAMScore(username_str)
    highest_OCEAN_category = calculateHighestOCEANScore(username_str)
    
    
    print(
        f"Based on your results, we suggest you consider a career in "
        f"{highest_STEAM_category}"
    )
    print("Here is some feedback based on your results:\n")
    combined_ID = (
        f"{highest_STEAM_category} and {highest_OCEAN_category}"
    )  # Combine the two categories to create a unique ID for the feedback.
    # This is because the feedback is stored in a dictionary, and the
    # dictionary keys must be unique.
    feedback = feedback_database.get(
        combined_ID, {}
    ).get('feedback', 'Feedback not found')
    # Retrieve the relevant feedback from the database,
    # for .get see “Python Dictionary get() Method.” W3Schools,
    # www.w3schools.com/python/ref_dictionary_get.asp. Accessed 8 Oct. 2023.
    cprint(feedback, 'light_green', attrs=['bold'])  # Print the feedback
    print("\npress any key to check your subject knowledge results on the ")
    print("leaderboard")
    input()
    os.system('cls' if os.name == 'nt' else 'clear')
    get_high_score_leaderboard(username_str)


main()
