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

username_str = "Betty56"

def generate_comparison_data_main():
    """
    [x] calculate user's highest steam score
    [x] calculate user's highest ocean score
    [x] calculate user's relative rank from highest STEAM score e.g. "you came 3rd in science"
    [ ] calculate user's percentage of highest score in OCEAN. e.g. "our data suggests you were in the top 13% of Openness"
    [x] suggest a career based on the user's highest STEAM score
    [z] suggest what kind of environment the user would thrive in based on their highest OCEAN score
    """
    highest_category = calculateHighestSTEAMScore()
    calculateSTEAMRank(highest_category)
    highest_category = calculateHighestOCEANScore()
    calculateOCEANPercentage(highest_category)
    assignOCEAN_STEAM_feedback(highest_category)

def calculateHighestSTEAMScore():
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

def calculateHighestOCEANScore():
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

def calculateSTEAMRank(highest_category):
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

def calculateOCEANPercentage(highest_category):
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
    

generate_comparison_data_main()