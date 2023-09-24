# Google API imported with thanks to Code Institute Tutorial 'Love Sandwiches' by Anna Greaves.

import json 
import gspread
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
    run all program functions, starting with the main menu.
    """
    mainMenu()
    

main()