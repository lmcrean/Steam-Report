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

def get_user_data():
    """
    Gets the score and username from user and returns the username.
    """

    while True: # True
        username_str = input("Enter your username here: ") # score is an integer

        user_data = username_str

        if validate_name(username_str): # if validate_name(user_data) == True:
            print("Data is valid!")
            break # break out of the while loop if data is valid

    return user_data
  
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
    print(f"Updating {worksheet} worksheet...\n")
    worksheet_to_update = SHEET.worksheet(worksheet) # access the relevant worksheet
    worksheet_to_update.append_row(data) # append the data provided as a new row at the bottom of the relevant worksheet
    print(f"{worksheet} worksheet updated successfully.\n")

def get_high_score_leaderboard():
    """
    Collects columns of data from score worksheet, collecting the last 5 entries for each sandwich and returns the data as a list of lists.
    """
    score = SHEET.worksheet("score") # access the score worksheet

    # column = score.col_values(3) # get all values from column 3 (index 2), which is the cheese sandwich column. This will return a list of all values in the column.
    # print(column)

    columns = []
    for ind in range(1, 7): # range starts at 1 because the first column is the date column, which we don't need. range ends at 7 because there are 6 columns of data. 
        column = score.col_values(ind) # get all values from each column
        columns.append(column[-5:]) # append the last 5 values from each column to the columns list. -5: is the index of the last 5 items in a list. This number is chosen because the last 5 rows of data in the score worksheet are the most recent data.

    # pprint(columns) # pretty print the columns list
    return columns


def main():
    """
    Run all program functions
    """
    data = get_user_data() # call the get_user_data function and store the returned data in a variable called data
    user_data = data # convert the data provided by the user into integers. num is a variable that represents each item in the list data. 
    update_worksheet(user_data, "score") # call the update_worksheet function and pass in the user_data list and the name of the worksheet as arguments. This will add the user_data list as a new row in the score worksheet.
    get_high_score_leaderboard() # call the get_high_score_leaderboard function and store the returned data in a variable called score_columns

main() # call the main function to run the program. Must be below the function definition.

