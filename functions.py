import json


def load_students() -> list:
    """
    Загружает список студентов из файла
    :return:
    """
    with open("students.json", "r") as read_file:
        return json.load(read_file)


def load_professions() -> list:
    """
    Загружает список профессий из файла
    :return:
    """
    with open("professions.json", "r") as read_file:
        return json.load(read_file)
