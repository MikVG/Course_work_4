from abc import ABC, abstractmethod
import json


class File_Saver(ABC):

    def add_vacancy(self, vacancy, vacancies_list, platform):
        pass


class JSONSaver(File_Saver):

    def __init__(self):
        pass

    def add_vacancy(self, vacancy, vacancies_list, platform):
        with open(f'{vacancy}_{platform}_json.json', 'w', encoding='UTF-8') as file:
            json.dump(vacancies_list, file, indent=2, ensure_ascii=False)

