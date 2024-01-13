from abc import ABC, abstractmethod
import json


class File_Saver(ABC):

    def add_vacancy(self, vacancies_list):
        pass

    def open(self):
        pass

    def clear_file(self):
        pass


class JSONSaver(File_Saver):

    def __init__(self):
        pass

    def add_vacancy(self, vacancies_list):
        with open('Vacancy_list.json', 'w', encoding='UTF-8') as file:
            json.dump(vacancies_list, file, indent=2, ensure_ascii=False)

    def open(self):
        with open('Vacancy_list.json', 'r', encoding='UTF-8') as file:
            vacancy_list = json.load(file)
            return vacancy_list

    def clear_file(self):
        with open('Vacancy_list.json', 'w') as file:
            file.truncate()
