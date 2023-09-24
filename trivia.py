import requests
import json
from pprint import pprint


url = "https://opentdb.com/api.php?amount=50&category=17&difficulty=easy&type=multiple"
response = requests.get(url)
pprint(response.json())
with open('trivia.json', 'w') as f:
    json.dump(response.json(), f, indent=4)
