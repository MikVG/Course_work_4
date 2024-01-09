from class_api import HeadHunterAPI, SuperJobAPI

from class_vacancies import Vacancy

vacan = HeadHunterAPI()
vac = vacan.get_vacancies('python')

#print(vac)

get_vac = Vacancy()
qwe = get_vac.add_vacancy(vac)

# vac_sj = SuperJobAPI()
# vac_s = vac_sj.get_vacancies('python')
#
# print(vac_s)
