import json

class Vacancy:

    def __init__(self, employer=None, name=None, link=None, requirements=None, salary_from=None, salary_to=None):
        self.employer = employer
        self.name = name
        self.link = link
        self.requirements = requirements
        self.salary_from = salary_from
        self.salary_to = salary_to

    def __str__(self):
        return f"""
        Работодатель: {self.employer}
        Вакансия: {self.name}
        Требования: {self.requirements}
        Зарплата от: {self.salary_from}, до: {self.salary_to}
        Ссылка  на вакансию: {self.link}"""

    def add_vacancy(self, vacancies):
        print(vacancies)

        vacancies_list = []
        vacancies_all = []

        for vacancy in vacancies:

            if vacancy['salary'] is not None and vacancy['salary']['currency'] == 'RUR':
                vacancies_list.append([
                    vacancy['employer']['name'],
                    vacancy['name'],
                    vacancy['alternate_url'],
                    vacancy['snippet']['requirement'],
                    vacancy['salary']['from'],
                    vacancy['salary']['to']
                ])

        for vacancy in vacancies_list:
            vacancy_dict = {
                'employer': vacancy[0],
                'name': vacancy[1],
                'link': vacancy[2],
                'requirement': vacancy[3],
                'salary_from': vacancy[4],
                'salary_to': vacancy[5]
            }

            if vacancy_dict['salary_from'] is None:
                vacancy_dict['salary_from'] = 0
            elif vacancy_dict['salary_to'] is None:
                vacancy_dict['salary_to'] = vacancy_dict['salary_from']

            vacancies_all.append(vacancy_dict)

        return vacancies_all
