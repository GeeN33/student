from functions import load_students, load_professions
from utils import get_student_by_pk, get_profession_by_title,check_fitness,print_student,print_fitness

def main():
    """ функция main здесь происходит ввод вывод пользователем """
    student_data = load_students()
    professions_data = load_professions()
    pk = int(input('Введите номер студента \n'))
    student = get_student_by_pk(student_data, pk)
    if len(student) == 0:
        print('У нас нет такого студента')
        return quit()

    print_student(student)
    title = input(f"Выберите специальность для оценки студента {student['full_name']}\n")
    professions = get_profession_by_title(professions_data, title)
    if len(professions) == 0:
        print('У нас нет такой специальности')
        return quit()

    print_fitness(check_fitness(student, professions))




main()


