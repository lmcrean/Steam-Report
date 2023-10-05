import json
import random

with open("personality_statements.json", "r") as file: # Load the questions from the JSON file. R = read.
    quiz_data = json.load(file) #“Json.load in Python.” GeeksforGeeks, GeeksforGeeks, 12 Mar. 2020, www.geeksforgeeks.org/json-load-in-python/. Accessed 5 Oct. 2023.

# Initialize variables including trait scores.
user_answers = [] 
trait_scores = {"Openness": 0, "Conscientiousness": 0, "Extraversion": 0, "Agreeableness": 0, "Neuroticism": 0}
question_index = 0

random.shuffle(quiz_data["questions"]) # Shuffle the questions. “Python Random Shuffle() Method.” W3schools.com, 2023, www.w3schools.com/python/ref_random_shuffle.asp. Accessed 5 Oct. 2023.

def ask_question(question_index): #question_index is a parameter. “Python Function Arguments.” W3schools.com, 2023, www.w3schools.com/python/gloss_python_function_arguments.asp#:~:text=A%20parameter%20is%20the%20variable,function%20when%20it%20is%20called. Accessed 5 Oct. 2023.
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


# Loop through the questions and ask them one by one
while question_index < len(quiz_data["questions"]): #“Python Len() Function.” W3schools.com, 2023, www.w3schools.com/python/ref_func_len.asp. Accessed 5 Oct. 2023. Len() function returns the number of items in an object.
    ask_question(question_index)
    question_index += 1


print("\nThank you for completing the quiz! Your responses:") # Display the user's answers

for i, answer in enumerate(user_answers): #enumerate function adds a counter to an iterable. “Python Enumerate() Function.” W3schools.com, 2023, www.w3schools.com/python/ref_func_enumerate.asp. Accessed 5 Oct. 2023. An iterable is an object that can return its members one at a time.
    question = quiz_data["questions"][i]
    print(f"Question {i + 1} (Trait: {question['trait']}): {answer}")

# Display the calculated trait scores
print("\nTrait Scores:")
for trait, score in trait_scores.items():
    print(f"{trait}: {score}")
