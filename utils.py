import re


def get_student_by_pk(data: list, pk: int) -> dict:
    """
     Получает словарь с данными студента по его pk
    :param data: students.json
    :param pk: номер студента
    :return: Возвращает словарь конкретного студента
    """
    for d in data:
        if d['pk'] == pk:
            return d
    return {}


def get_profession_by_title(data: list, title: str) -> dict:
    """
    Получает словарь с инфо о профе по названию
    :param data: professions.json
    :param title: специальность
    :return: Список языков программирования относящиеся к специальности
    """
    for d in data:
        if d['title'] == title:
            return d["skills"]
    return {}


def check_fitness(student: dict, professions: dict) -> dict:
    """
    получает студента и профессию, возвращяет словарь знает не знает языки
    :param student: студента
    :param professions: профессию
    :return: возвращяет словарь знает не знает языки
    """
    skills = set(student["skills"])
    profession = set(professions)
    has = list(skills.intersection(profession))
    lacks = list(profession.difference(skills))
    fit_percent = int(len(has) / (len(profession) / 100))
    return {"full_name": student["full_name"], "has": has, "lacks": lacks, "fit_percent": fit_percent}


def print_student(student: dict) -> None:
    """
    Получает словарь студента и печатает
    :param student: словарь студента
    """
    print(f"Студент {student['full_name']}")
    check_login(student['login'])
    print(f"Знает {', '.join(student['skills'])}")


def print_fitness(check_fitness: dict) -> None:
    """
     Получает словарь знает не знает языки и печатает
    :param check_fitness: словарь знает не знает языки
    """
    print(f"Пригодность {check_fitness['fit_percent']}%")
    print(f"{check_fitness['full_name']} знает {', '.join(check_fitness['has'])}")
    print(f"{check_fitness['full_name']} не знает  {', '.join(check_fitness['lacks'])}")


def check_login(s: str) -> None:
    """
     функция с помощью регулярного выражения проверяет логин на корректность.
    :param логин:

    """
    rez = re.findall(r'^[a-z0-9](?=.*[0-9])(?=.*[ a-z])(?=.*[A-Z])(?=.*[@#$%^&-+=()]).{1,}[^@#$%^&-+=()]$', s)
    if len(rez) > 0:
        print(f'{s} правильный логин')
    else:
        print(f'{s} не правильный логин')
