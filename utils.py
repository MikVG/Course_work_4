from class_api import HeadHunterAPI, SuperJobAPI

from class_vacancies import Vacancy

vacan = HeadHunterAPI()
vac = vacan.get_vacancies('python')

#for a in vac:
#    vaca = Vacancy(a['employer'], a['name'], a['link'], a['requirements'], a['salary_from'], a['salary_to'])
#    print(vaca)



#vac_sj = SuperJobAPI()
#vac_s = vac_sj.get_vacancies('python')

#print(vac_s)
