from utils import search, open, clear_file, exit


def user_return():
    """
    Функция для возврата в главное меню или выхода из программы
    :return:
    """
    user_return = input("""\nВернуться в главное меню?
    1 - Да
    2 - Выйти из программы
    """)
    if user_return == '1':
        main()
    else:
        exit()


def main():
    """
    Основная функция для вызова главного меню и навигации по программе
    :return:
    """
    user_choice = input("""Что вы хотите выполнить:
    1 - Выполнить поиск вакансий на платформах HeadHunter и SuperJob?
    2 - Вывести список найденных вакансий на экран?
    3 - Очистить файл Json?
    4 - Выйти из программы
    Ваш выбор: """)

    if user_choice == '1':
        search()
        user_return()

    elif user_choice == '2':
        open()
        user_return()

    elif user_choice == '3':
        clear_file()
        user_return()

    elif user_choice == '4':
        exit()


if __name__ == '__main__':
    main()
