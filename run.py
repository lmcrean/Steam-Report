# Google API imported with thanks to Code Institute Tutorial 'Love Sandwiches' by Anna Greaves.

import json #https://docs.python.org/3/library/json.html
import gspread #https://docs.gspread.org/en/latest/
import requests #https://docs.python-requests.org/en/latest/
import html #https://docs.python.org/3/library/html.html
import random #https://docs.python.org/3/library/random.html
import os #https://docs.python.org/3/library/os.html
import sys
from package_python import subjectquiz
from package_python import quizleaderboard
from package_python import personality
from package_python import finalreport
from google.oauth2.service_account import Credentials
from pprint import pprint
from prettytable import PrettyTable
x = PrettyTable()

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
    username_str = input("Enter your username here: ") # ask the user for their username
    if validate_name(username_str): 
            print("Data is valid!")
    mainMenu()
    while True:
        try:
            choice = int(input("Please enter your choice: "))
            if choice == 1:
                subjectQuiz()
                
            elif choice == 2:
                viewLeaderboard()
                
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

main()