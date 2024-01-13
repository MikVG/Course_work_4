from abc import ABC, abstractmethod
import json


class File_Saver(ABC):
    """
    Абстрактный класс для работы с файлом JSON
    """

    @abstractmethod
    def add_vacancy(self, vacancies_list):
        """
        метод для добавления вакансии в файл
        :param vacancies_list:
        :return:
        """
        pass

    @abstractmethod
    def open(self):
        """
        метод для получения вакансий из файла
        :return:
        """
        pass

    @abstractmethod
    def clear_file(self):
        """
        метод для очистки файла
        :return:
        """
        pass


class JSONSaver(File_Saver):
    """
    Класс для работы с файлом JSON
    """

    def __init__(self):
        """
        метод для инициализации экземпляра класса
        """
        pass

    def add_vacancy(self, vacancies_list):
        """
        метод для записи вакансий в файл, если файл отсутствует, то он будет создан
        :param vacancies_list:
        :return: None
        """
        with open('Vacancy_list.json', 'w', encoding='UTF-8') as file:
            json.dump(vacancies_list, file, indent=2, ensure_ascii=False)

    def open(self):
        """
        метод для чтения файла JSON и возвращения списка вакансий
        :return: список вакансий
        """
        with open('Vacancy_list.json', 'r', encoding='UTF-8') as file:
            vacancy_list = json.load(file)
            return vacancy_list

    def clear_file(self):
        """
        метод для очистки содержимого файла
        :return:
        """
        with open('Vacancy_list.json', 'w') as file:
            file.truncate()
