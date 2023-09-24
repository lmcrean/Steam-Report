import requests
import json
from pprint import pprint

url = "https://opentdb.com/api.php?amount=30&category=18&type=multiple"
response = requests.get(url)
pprint(response.json())
with open('trivia_tech.json', 'w') as f:
    json.dump(response.json(), f, indent=4)

