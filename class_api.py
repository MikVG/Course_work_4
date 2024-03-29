from abc import ABC, abstractmethod
import os
from dotenv import load_dotenv
import requests
from config import URL_HH, URL_SJ

load_dotenv()


class JobPortal(ABC):
    """
    Абстрактный класс для работы с API сайтов вакансий
    """

    @abstractmethod
    def get_vacancies(self, vacancy):
        """
        Получение информации о вакансиях через API
        :param vacancy:
        :return: None
        """
        pass


class HeadHunterAPI(JobPortal):
    """
    Класс для работы с API сайта Head Hunter
    """

    def __init__(self):
        """
        метод для инициализации класса HeadHunterAPI
        """
        pass

    def get_vacancies(self, vacancy):
        """
        метод для получения списка вакансий сайта Head Hunter
        :param vacancy:
        :return:
        """
        for num in range(2):
            params = {'text': vacancy, 'areas': 113, 'per_page': 20, 'page': num}
            response = requests.get(URL_HH, params=params)
            data = response.json()['items']

            vacancies_list = []
            vacancies_all = []

            for vacancy in range(len(data)):
                if data[vacancy]['salary'] is not None and data[vacancy]['salary']['currency'] == 'RUR':
                    try:
                        vacancies_list.append([
                            data[vacancy]['employer']['name'],
                            data[vacancy]['name'],
                            data[vacancy]['alternate_url'],
                            data[vacancy]['snippet']['requirement'],
                            data[vacancy]['salary']['from'],
                            data[vacancy]['salary']['to']])
                    except KeyError:
                        continue

        for vacancy in vacancies_list:
            vacancy_dict = {
                'employer': vacancy[0],
                'name': vacancy[1],
                'link': vacancy[2],
                'requirements': vacancy[3],
                'salary_from': vacancy[4],
                'salary_to': vacancy[5]
            }

            if vacancy_dict['salary_from'] is None:
                vacancy_dict['salary_from'] = 0
            elif vacancy_dict['salary_to'] is None:
                vacancy_dict['salary_to'] = vacancy_dict['salary_from']

            vacancies_all.append(vacancy_dict)

        return vacancies_all


class SuperJobAPI(JobPortal):
    """
    Класс для работы с API сайта Super Job
    """

    def __init__(self):
        """
        метод для инициализации класса SuperJobAPI
        """
        pass

    def get_vacancies(self, vacancy):
        """
        метод для получения списка вакансий сайта Super Job
        :param vacancy:
        :return:
        """

        vacancies_list = []
        vacancies_all = []

        API_KEY = os.getenv('API_KEY_SJ')
        header = {"X-Api-App-Id": API_KEY}

        for num in range(2):
            params = {"keyword": vacancy, "per_page": 1000, "area": 113, "page": num}
            response = requests.get(URL_SJ, params=params, headers=header)
            vacancies = response.json()['objects']

            for vacancy in vacancies:
                if vacancy['currency'] == 'rub':
                    try:
                        vacancies_list.append([
                            vacancy['client']['title'],
                            vacancy['profession'],
                            vacancy['client']['link'],
                            vacancy['candidat'],
                            vacancy['payment_from'],
                            vacancy['payment_to']])
                    except KeyError:
                        continue

        for vacancy in vacancies_list:
            vacancy_dict = {
                'employer': vacancy[0],
                'name': vacancy[1],
                'link': vacancy[2],
                'requirements': vacancy[3],
                'salary_from': vacancy[4],
                'salary_to': vacancy[5]
            }

            if vacancy_dict['salary_from'] is None:
                vacancy_dict['salary_from'] = 0
            elif vacancy_dict['salary_to'] is None:
                vacancy_dict['salary_to'] = vacancy_dict['salary_from']

            vacancies_all.append(vacancy_dict)

        return vacancies_all
