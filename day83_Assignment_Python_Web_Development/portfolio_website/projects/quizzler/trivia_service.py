import random
import requests

from .question_model import Question


OPENTDB_URL = "https://opentdb.com/api.php"


TRIVIA_CATEGORIES = [
    {
        "category": "General Knowledge",
        "category_id": 9
    },
    {
        "category": "Television",
        "category_id": 14
    },
    {
        "category": "Board Games",
        "category_id": 16
    },
    {
        "category": "History",
        "category_id": 23
    },
    {
        "category": "Computer Science",
        "category_id": 18
    }
]


def get_questions():

    category = random.choice(TRIVIA_CATEGORIES)

    parameters = {
        "amount": 10,
        "type": "boolean",
        "category": category["category_id"],
        "difficulty": "medium"
    }

    response = requests.get(
        OPENTDB_URL,
        params=parameters,
        timeout=10
    )

    response.raise_for_status()

    data = response.json()

    question_bank = []

    for question in data["results"]:

        new_question = Question(
            question["question"],
            question["correct_answer"]
        )

        question_bank.append(new_question)

    return question_bank, category["category"]