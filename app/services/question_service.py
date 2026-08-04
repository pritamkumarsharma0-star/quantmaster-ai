import json
import random
from pathlib import Path

QUESTIONS_FILE = (
    Path(__file__).resolve().parent.parent
    / "questions"
    / "simplification.json"
)


def load_questions():
    with open(QUESTIONS_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def get_random_question():
    questions = load_questions()
    return random.choice(questions)


def get_question_by_id(question_id):
    questions = load_questions()

    for question in questions:
        if question["id"] == question_id:
            return question

    return None