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

def main():
    """
    Run all program functions
    """
    sales_data = get_sales_data()
    sales_data = validate_data(sales_data)
    update_worksheet(sales_data)


def getUserName():
    """
    Get the user's name
    """

    while True: # True
        user_name = input("Please enter your name: ")

        new_score_data = data_str.split(",")

        if validate_data(sales_data): # if validate_data(sales_data) == True:
            print("User name is valid!")
            break # break out of the while loop if data is valid

    return sales_data

def validate_data(values):
    """
    Inside the try, converts all string values into integers.
    Raises ValueError if strings cannot be converted into int, or if there aren't exactly 6 values.
    """
    try:
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 values required, you provided {len(values)}"
            )
    except ValueError as e:
            print(f"Invalid data: {e}, please try again.\n")
            return False # return False if errors are raised.
    
    return True # return True if no errors are raised. This means that the function will return True if the try block is successful. If unsuccessful, the except block will run and return False. For example, if the user enters 5 numbers instead of 6, the except block will run and return False.

def update_worksheet(data, worksheet):
    """
    Receives a list of integers to be inserted into a worksheet.
    Update the relevant worksheet with the data provided.
    """
    print(f"Updating {worksheet} worksheet...\n")
    worksheet_to_update = SHEET.worksheet(worksheet) # access the relevant worksheet
    worksheet_to_update.append_row(data) # append the data provided as a new row at the bottom of the relevant worksheet
    print(f"{worksheet} worksheet updated successfully.\n")

def calculate_surplus_data(sales_row):
    """
    Compare sales with stock and calculate the surplus for each item type.
    The surplus is defined as the sales figure subtracted from the stock:
    - Positive surplus indicates waste
    - Negative surplus indicates extra made when stock was sold out.
    """
    print("Calculating surplus data...\n")
    stock = SHEET.worksheet("stock").get_all_values() # access the stock worksheet and get all values
    stock_row = stock[-1] # get the last row of data from the stock worksheet. -1 is the index of the last item in a list. This number is chosen because the last row of data in the stock worksheet is the most recent data.

    surplus_data = [] # create an empty list called surplus_data


    for stock, sales in zip(stock_row, sales_row):
        surplus = int(stock) - sales
        surplus_data.append(surplus) # append the surplus value to the surplus_data list
        print(f"Surplus for item: {surplus}\n")
    print(surplus_data)

def get_last_5_entries_sales():
    """
    Collects columns of data from sales worksheet, collecting the last 5 entries for each sandwich and returns the data as a list of lists.
    """
    sales = SHEET.worksheet("sales") # access the sales worksheet

    # column = sales.col_values(3) # get all values from column 3 (index 2), which is the cheese sandwich column. This will return a list of all values in the column.
    # print(column)

    columns = []
    for ind in range(1, 7): # range starts at 1 because the first column is the date column, which we don't need. range ends at 7 because there are 6 columns of data. 
        column = sales.col_values(ind) # get all values from each column
        columns.append(column[-5:]) # append the last 5 values from each column to the columns list. -5: is the index of the last 5 items in a list. This number is chosen because the last 5 rows of data in the sales worksheet are the most recent data.

    # pprint(columns) # pretty print the columns list
    return columns

def calculate_stock_data(data):
    """
    Calculate the average stock for each item type, adding 10%. It's a good idea to add 10% to the average stock to ensure that there is enough stock for the next market.
    """
    print("Calculating stock data...\n")
    new_stock_data = [] # create an empty list called new_stock_data

    for column in data:
        int_column = [int(num) for num in column] # convert the data provided by the user into integers. num is a variable that represents each item in the list data. int() converts the data into integers.
        average = sum(int_column) / len(int_column) # calculate the average of each column. len() returns the number of items in a list.
        stock_num = average * 1.1 # add 10% to the average
        new_stock_data.append(round(stock_num)) # round the stock_num to the nearest whole number and append the value to the new_stock_data list. round() rounds a number to the nearest whole number.

    return new_stock_data

def main():
    """
    Run all program functions
    """
    data = get_sales_data() # call the get_sales_data function and store the returned data in a variable called data
    sales_data = [int(num) for num in data] # convert the data provided by the user into integers. num is a variable that represents each item in the list data. 
    update_worksheet(sales_data, "sales") # call the update_worksheet function and pass in the sales_data list and the name of the worksheet as arguments. This will add the sales_data list as a new row in the sales worksheet.
    new_surplus_data = calculate_surplus_data(sales_data) # call the calculate_surplus_data function and pass in the sales_data list as an argument. This will calculate the surplus data for each item type and store the returned data in a variable called new_surplus_data.
    update_worksheet(new_surplus_data, "surplus") # call the update_worksheet function and pass in the new_surplus_data list and the name of the worksheet as arguments. This will add the new_surplus_data list as a new row in the surplus worksheet.
    sales_columns = get_last_5_entries_sales() # call the get_last_5_entries_sales function and store the returned data in a variable called sales_columns
    stock_data = calculate_stock_data(sales_columns) # call the calculate_stock_data function and pass in the sales_columns list as an argument. This will calculate the stock data for each sandwich and store the returned data in a variable called stock_data.
    update_worksheet(stock_data, "stock") # call the update_worksheet function and pass in the stock_data list and the name of the worksheet as arguments. This will add the stock_data list as a new row in the stock worksheet.

print("Welcome to Love Sandwiches Data Automation")

main() # call the main function to run the program. Must be below the function definition.
