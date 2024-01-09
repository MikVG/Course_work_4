from abc import ABC, abstractmethod
import json


class File_Saver(ABC):

    def add(self):
        pass


class Json_Saver(File_Saver):

    def __init__(self):
        pass

    def add(self, vacancy, vacancies_list):
        with open(f'{vacancy}_hh_json.json', 'w', encoding='UTF-8') as file:
            json.dump(vacancies_list, file, indent=2, ensure_ascii=False)

