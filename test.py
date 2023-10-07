# Google API imported with thanks to Code Institute Tutorial 'Love Sandwiches' by Anna Greaves.

import json #https://docs.python.org/3/library/json.html
import gspread #https://docs.gspread.org/en/latest/
import requests #https://docs.python-requests.org/en/latest/
import html #https://docs.python.org/3/library/html.html
import random #https://docs.python.org/3/library/random.html
import os #https://docs.python.org/3/library/os.html
import sys
# from package_python import personality
# from package_python import finalreport
from google.oauth2.service_account import Credentials
from pprint import pprint
from prettytable import PrettyTable
x = PrettyTable()

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

subject_scores = SubjectScore(0,0,0,0,0,0)


def viewLeaderboard():
    print("You have chosen to view the leaderboard.")
    print("This is a work in progress.")
    print("1 - submit high score")
    print("2 - view leaderboard")
    choice = int(input("Please enter your choice: "))
    if choice == 1:
        leaderboardMain(subject_scores)
    elif choice == 2:
        get_high_score_leaderboard()
    else:
        print("Please enter a number between 1 and 2.")

def get_user_data(subject_scores: SubjectScore) -> None:
    """
    Gets the score and username from user and returns the username.
    """

    while True: # True
        
        username_str = input("Enter your username here: ") # ask the user for their username

        #place high score data into user_data_string variable
        user_data_string = f"{username_str},{subject_scores.scoreTotal},{subject_scores.scoreScience},{subject_scores.scoreTechnology},{subject_scores.scoreEnglish},{subject_scores.scoreArt},{subject_scores.scoreMath}" 

        user_data = user_data_string.split(",") # split the user_data string into a list of strings at each comma. This will create a list of strings. The first item in the list will be the username, and the rest of the items will be the scores.

        print(f"User Data: {user_data}\n") # print the user_data list

        break # break out of the while loop if data is valid
    print("Data is ready to be uploaded to Google Sheets.\n")
    return user_data # return the user_data list


def update_worksheet(data, worksheet):
    """
    Receives a list of strings and integers to be inserted into a worksheet.
    Update the worksheet with the data provided.
    """
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

    worksheet = SHEET.worksheet('score')  # Replace 'Sheet1' with your worksheet name.
    
    data = worksheet.get_all_values() # Read data from Google Sheet

    table = PrettyTable() # Create a PrettyTable object

    table.field_names = data[0] # Set the field names based on the first row of data (assuming it's the header row)

    all_user_info = []

    for row in data[1:]: # Populate PrettyTable with data. 1 means start at index 1, which is the second row. This is because the first row is the header row.
        table.add_row(row)
        # print(table.field_names)
        # print(row)
        userinfo = dict(zip(table.field_names,row))
        all_user_info.append(userinfo)

    print(all_user_info)

    sortedByScience = sorted(all_user_info, key = lambda d: d['S'], reverse=True)

    print()
    print("Sorted by Science Score")
    #“How to Sort a List of Dictionaries by a Value of the Dictionary in Python?” Stack Overflow, 2023, stackoverflow.com/questions/72899/how-to-sort-a-list-of-dictionaries-by-a-value-of-the-dictionary-in-python. Accessed 5 Oct. 2023.
    #“Sort a List of Objects in Python | FavTutor.” FavTutor, 2022, favtutor.com/blogs/sort-list-of-objects-python. Accessed 5 Oct. 2023.



    # table.sortby = "Score" # Sort the table by the Total column, in ascending order
    # table.reversesort = True # Reverse the order of the sort, so it's descending

    # print(table) # Print the PrettyTable

    #TODO: 1 insert dummy data into the Rank column from a string

    return 

def leaderboardMain(subject_scores): #leaderboardmain() uses the subject_scores variable
    """
    Run all program functions
    """
    print("Welcome to the leaderboard!")
    # subject_scores = SubjectScore(0,0,0,0,0,0) # create a SubjectScore object and store it in a variable called subject_scores
    data = get_user_data(subject_scores)  # call the get_user_data function and store the returned data in a variable called data
    print(f"Data provided: {data}\n")
    user_data = data  # convert the data provided by the user into integers. num is a variable that represents each item in the list data. 
    print(f"User Data:{user_data}") 
    update_worksheet(user_data, "score")  # call the update_worksheet function with user_data as a list
    get_high_score_leaderboard()  # call the get_high_score_leaderboard function and store the returned data in a variable called score_columns


get_high_score_leaderboard()