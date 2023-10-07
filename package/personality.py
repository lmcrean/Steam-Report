import json #https://docs.python.org/3/library/json.html
import gspread #https://docs.gspread.org/en/latest/
import requests #https://docs.python-requests.org/en/latest/
import html #https://docs.python.org/3/library/html.html
import random #https://docs.python.org/3/library/random.html
import os #https://docs.python.org/3/library/os.html
import sys
import controller
from google.oauth2.service_account import Credentials
from run import trait_scores, user_answers, quiz_data
from pprint import pprint
from prettytable import PrettyTable
x = PrettyTable()

def ask_question(question_index): 
    """
    question_index is a parameter. “Python Function Arguments.” W3schools.com, 2023, www.w3schools.com/python/gloss_python_function_arguments.asp#:~:text=A%20parameter%20is%20the%20variable,function%20when%20it%20is%20called. Accessed 5 Oct. 2023.
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


print("\nThank you for completing the quiz! Your responses:") # Display the user's answers


def convert_score_to_percentage(score):
    """
    Convert a personality trait score between 5 and 45 to a percentage.

    The trait score should be between 5 and 45.
    
    Returns The percentage equivalent of the trait score.
    """
    if 5 <= score <= 45:
        percentage = ((score - 5) / 40) * 100
        return round(percentage, 1) #“Python Round() Function.” W3schools.com, 2023, www.w3schools.com/python/ref_func_round.asp. Accessed 5 Oct. 2023.
        personalityResults(score)
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
        controller.start_subject_quiz()
    else:
        print("Invalid answer. Please enter a number between 1 and 2.")

#commented out - enables a breakdown of scores.
# for trait, score in trait_scores.items():
#     print(f"{trait}: {score}") # Display the calculated trait scores

# for i, answer in enumerate(user_answers): #enumerate function adds a counter to an iterable. “Python Enumerate() Function.” W3schools.com, 2023, www.w3schools.com/python/ref_func_enumerate.asp. Accessed 5 Oct. 2023. An iterable is an object that can return its members one at a time.
#     question = quiz_data["questions"][i] #CURRENTLY
#     print(f"Question {i + 1} (Trait: {question['trait']}): {answer}") #ERROR doesn't print whole list only 25