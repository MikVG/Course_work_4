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
        print(vacancy)
        """
        метод для получения списка вакансий сайта Head Hunter
        :param vacancy:
        :return:
        """
        params = {'text': vacancy, 'areas': 113, 'per_page': 3, 'page': 1}
        response = requests.get(URL_HH, params=params)
        data = response.json()['items']
        return data


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
        API_KEY = os.getenv('API_KEY_SJ')
        header = {"X-Api-App-Id": API_KEY}

        params = {"keyword": vacancy, "page": "1"}
        response = requests.get(URL_SJ, params=params, headers=header)
        vacancies = response.json()['objects']
        return vacancies
