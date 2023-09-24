import requests
from pprint import pprint
import json

categories_url= "https://opentdb.com/api_category.php"
response = requests.get(categories_url)

pprint(response.json())
with open('categories.json', 'w') as f:
    json.dump(response.json(), f, indent=4)