"""
    CONCEPT: Modify the static data.py file to pull in trivia questions from an API, instead of hard-coded data from Day 17 Quiz
    --API Resource: Open Trivia Database - https://opentdb.com/
    -- Our 10 random question URL from Open Trivia Database - https://opentdb.com/api.php?amount=10&type=boolean
"""
import random
import requests

opentdb_categories = [
    {
        "category": "General",
        "category_id": 9
    },
    {
        "category": "television",
        "category_id": 14
    },
    {
        "category": "board games",
        "category_id": 16
    },
    {
        "category": "history",
        "category_id": 23
    },
    {
        "category": "computer science",
        "category_id": 18
    }
]


random_category = random.choice(opentdb_categories)
random_category_id = random_category["category_id"]

##random_category = random.choice(random.randint(1,len(opentdb_categories))[opentdb_categories]["category_id"])
#print(random_category)
parameters = {
    "amount": 10,
    "type": "boolean",
    "category": random_category_id,
    "difficulty": "medium"
}
# get the response from the API with 10 JSON objects; response will return a LIST of DICTIONARY (JSON) objects
response = requests.get("https://opentdb.com/api.php", params=parameters, verify=False) # have to use verify=False to bypass the SSL self-signed certification error
response.raise_for_status()

# data is the list of JSON objects
data = response.json()

# get just the DICTIONARY LIST; with its key:value pairs
question_data = data["results"]

# question_data = [
#     {
#         "category": "Science: Computers",
#         "type": "boolean",
#         "difficulty": "medium",
#         "question": "The HTML5 standard was published in 2014.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "category": "Science: Computers",
#         "type": "boolean",
#         "difficulty": "medium",
#         "question": "The first computer bug was formed by faulty wires.",
#         "correct_answer": "False",
#         "incorrect_answers": [
#             "True"
#         ]
#     },
#     {
#         "category": "Science: Computers",
#         "type": "boolean",
#         "difficulty": "medium",
#         "question": "FLAC stands for 'Free Lossless Audio Condenser'.",
#         "correct_answer": "False",
#         "incorrect_answers": [
#             "True"
#         ]
#     },
#     {
#         "category": "Science: Computers",
#         "type": "boolean",
#         "difficulty": "medium",
#         "question": "All program codes have to be compiled into an executable file in order to be run. This file can then be executed on any machine.",
#         "correct_answer": "False",
#         "incorrect_answers": [
#             "True"
#         ]
#     },
#     {
#         "category": "Science: Computers",
#         "type": "boolean",
#         "difficulty": "easy",
#         "question": "Linus Torvalds created Linux and Git.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "category": "Science: Computers",
#         "type": "boolean",
#         "difficulty": "easy",
#         "question": "The programming language 'Python' is based off a modified version of 'JavaScript'",
#         "correct_answer": "False",
#         "incorrect_answers": [
#             "True"
#         ]
#     },
#     {
#         "category": "Science: Computers",
#         "type": "boolean",
#         "difficulty": "medium",
#         "question": "AMD created the first consumer 64-bit processor.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "category": "Science: Computers",
#         "type": "boolean",
#         "difficulty": "easy",
#         "question": "'HTML' stands for Hypertext Markup Language.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "category": "Science: Computers",
#         "type": "boolean",
#         "difficulty": "easy",
#         "question": "In most programming languages, the operator ++ is equivalent to the statement '+= 1'.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "category": "Science: Computers",
#         "type": "boolean",
#         "difficulty": "hard",
#         "question": "The IBM PC used an Intel 8008 microprocessor clocked at 4.77 MHz and 8 kilobytes of memory.",
#         "correct_answer": "False",
#         "incorrect_answers": [
#             "True"
#         ]
#     }
# ]
