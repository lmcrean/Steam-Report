import requests
import json
from pprint import pprint


url = "https://opentdb.com/api.php?amount=10&category=17&difficulty=easy&type=multiple"
response = requests.get(url)
pprint(response.json())
with open('trivia_science.json', 'w') as f:
    json.dump(response.json(), f, indent=4)

url = "https://opentdb.com/api.php?amount=10&category=30&difficulty=easy&type=multiple"
response = requests.get(url)
pprint(response.json())
with open('trivia_tech.json', 'w') as f:
    json.dump(response.json(), f, indent=4)

url = "https://opentdb.com/api.php?amount=10&category=10&difficulty=easy&type=multiple"
response = requests.get(url)
pprint(response.json())
with open('trivia_english.json', 'w') as f:
    json.dump(response.json(), f, indent=4)

url = "https://opentdb.com/api.php?amount=10&category=25&difficulty=easy&type=multiple"
response = requests.get(url)
pprint(response.json())
with open('trivia_art.json', 'w') as f:
    json.dump(response.json(), f, indent=4)

url = "https://opentdb.com/api.php?amount=10&category=19&difficulty=easy&type=multiple"
response = requests.get(url)
pprint(response.json())
with open('trivia_math.json', 'w') as f:
    json.dump(response.json(), f, indent=4)
