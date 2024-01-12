from class_api import HeadHunterAPI, SuperJobAPI
from class_file import JSONSaver

from class_vacancies import Vacancy

hh_api = HeadHunterAPI()
superjob_api = SuperJobAPI()

json_saver = JSONSaver()

def user_interaction():
    user_vacancy = input("Введите ключевое слово для поиска вакансии: ")
    user_platform = input("""На какой платформе вы хотите выполнить поиск вакансий:
1. HeadHunter
2. SuperJob\n""")
    while user_platform not in ['1', '2']:
        user_platform = input("""На какой платформе вы хотите выполнить поиск вакансий:
1. HeadHunter
2. SuperJob\n""")

    vacancies = None
    if user_platform == '1':
        hh_vacancies = hh_api.get_vacancies(user_vacancy)
        vacancies = hh_vacancies
        json_saver.add_vacancy(user_vacancy, hh_vacancies, platform='HeadHunter')
    elif user_platform == '2':
        superjob_vacancies = superjob_api.get_vacancies(user_vacancy)
        vacancies = superjob_vacancies
        json_saver.add_vacancy(user_vacancy, superjob_vacancies, platform='SuperJob')

    user_sort = input("""Хотите ли выполнить сортировку вакансий по зарплате?
1 - Да
2 - Нет\n""")
    while user_sort not in ['1', '2']:
        user_sort = input("""Хотите ли выполнить сортировку вакансий по зарплате?
        1 - Да
        2 - Нет\n""")

    if user_sort == '2':
        for vacancy in vacancies:
           vacancy_on_screen = Vacancy(vacancy['employer'], vacancy['name'], vacancy['link'], vacancy['requirements'],
                         vacancy['salary_from'], vacancy['salary_to'])
           print(vacancy_on_screen)
    else:
        vacancy_sorted = sorted(vacancies, key=lambda salary: salary['salary_from'], reverse=True)
        for vacancy in vacancy_sorted:
            vacancy_on_screen = Vacancy(vacancy['employer'], vacancy['name'], vacancy['link'],
                                        vacancy['requirements'], vacancy['salary_from'], vacancy['salary_to'])
            print(vacancy_on_screen)

user_interaction()
