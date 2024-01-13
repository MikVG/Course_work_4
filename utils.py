from class_api import HeadHunterAPI, SuperJobAPI
from class_file import JSONSaver

from class_vacancies import Vacancy


hh_api = HeadHunterAPI()
superjob_api = SuperJobAPI()

json_saver = JSONSaver()


def search():
    user_vacancy = input("Введите ключевое слово для поиска вакансии: ")

    vacancies = None
    vacancies_all = []

    hh_vacancies = hh_api.get_vacancies(user_vacancy)
    for vacancy in hh_vacancies:
        vacancies_all.append(vacancy)

    superjob_vacancies = superjob_api.get_vacancies(user_vacancy)
    for vacancy in superjob_vacancies:
        vacancies_all.append(vacancy)

    json_saver.add_vacancy(vacancies_all)
    print(f'Поиск вакансий завершен, добавлено {len(vacancies_all)} вакансий в файл Json\n')


def open():
    user_sort = input("""Хотите ли выполнить сортировку вакансий по зарплате?
    1 - Да
    2 - Нет\n""")
    while user_sort not in ['1', '2']:
        user_sort = input("""Хотите ли выполнить сортировку вакансий по зарплате?
        1 - Да
        2 - Нет\n""")

    vacancies = json_saver.open()

    if user_sort == '2':
        for vacancy in vacancies:
           vacancy_on_screen = Vacancy(vacancy['employer'], vacancy['name'], vacancy['link'],
                                       vacancy['requirements'], vacancy['salary_from'], vacancy['salary_to'])
           print(vacancy_on_screen)
    else:
        vacancy_sorted = sorted(vacancies, key=lambda salary: salary['salary_from'], reverse=True)
        for vacancy in vacancy_sorted:
            vacancy_on_screen = Vacancy(vacancy['employer'], vacancy['name'], vacancy['link'],
                                        vacancy['requirements'], vacancy['salary_from'], vacancy['salary_to'])
            print(vacancy_on_screen)


def clear_file():
    json_saver.clear_file()


def exit():
    print("Программа завершила работу!")
