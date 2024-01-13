import json

class Vacancy:
    """
    Класс для работы с вакансиями
    """

    def __init__(self, employer=None, name=None, link=None, requirements=None, salary_from=None, salary_to=None):
        """
        метод для инициализации экземпляра класса
        :param employer:
        :param name:
        :param link:
        :param requirements:
        :param salary_from:
        :param salary_to:
        """
        self.employer = employer
        self.name = name
        self.link = link
        self.requirements = requirements
        self.salary_from = salary_from
        self.salary_to = salary_to

    def __str__(self):
        """
        Метод для возврата пользовательской информации по вакансии
        :return:
        """
        return f"""
        Работодатель: {self.employer}
        Вакансия: {self.name}
        Требования: {self.requirements}
        Зарплата от: {self.salary_from}, до: {self.salary_to}
        Ссылка  на вакансию: {self.link}"""
