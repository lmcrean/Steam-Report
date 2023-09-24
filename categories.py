#credit to: https://opentdb.com/api_config.php and walktthrough: "Quiz App Using API Data - Python Project.” Run That, Run That, 16 May 2023, www.runthat.blog/quiz-app-using-api-data-python-project/. Accessed 24 Sept. 2023.

import requests
from pprint import pprint
import json

categories_url= "https://opentdb.com/api_category.php"
response = requests.get(categories_url)

pprint(response.json())
with open('categories.json', 'w') as f:
    json.dump(response.json(), f, indent=4)