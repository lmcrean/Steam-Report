

def viewLeaderboard()
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

    for row in data[1:]: # Populate PrettyTable with data. 1 means start at index 1, which is the second row. This is because the first row is the header row.
        table.add_row(row)

    table.sortby = "Score" # Sort the table by the Total column, in ascending order
    table.reversesort = True # Reverse the order of the sort, so it's descending

    print(table) # Print the PrettyTable

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
 
