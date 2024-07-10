from src.my_json import WorkJson
from src.vacancy import SortVacancies, PerformanceVacancies


def users_work(data_search):
    """Функция для работы с пользователем"""

    work_js = WorkJson()
    work_js.sav_json(work_js.preparation_data_api(data_search))

    while True:
        all_vacancy_list = work_js.get_vacancies()
        if len(all_vacancy_list) != 0:
            try:
                choice_action = int(input("""Программа может :
                    0 - вывести список по умолчанию
                    1 - сортировать по заработной плате (сначала "большие"),
                    2 - сортировать по городу,
                    3 - сортировать по дате размещения (сначала "свежие")
                    4 - удалять вакансии по ID
                    5 - добавить вакансию
                    6 - показать вакансии только с сайта SJ.ru
                    7 - показать вакансии только с сайта HH.ru
                    8 - показать топ вакансий 
                    9 - выход из программы 

                    Выберите действие (цифра от 0 до 9) и нажмите "Enter": """))

                if choice_action == 0:
                    answer_vacancy_list = all_vacancy_list

                elif choice_action == 1:
                    sort_data = SortVacancies()
                    actual_vacancy_list = [line for line in all_vacancy_list if isinstance(line['salary_from'], int)]
                    answer_vacancy_list = sort_data.sort_vacancies('salary_from', actual_vacancy_list)

                elif choice_action == 2:
                    sort_data = SortVacancies()
                    answer_vacancy_list = sort_data.sort_vacancies('town', all_vacancy_list, False)

                elif choice_action == 3:
                    sort_data = SortVacancies()
                    answer_vacancy_list = sort_data.sort_vacancies('date_publishedt', all_vacancy_list)

                elif choice_action == 4:
                    user_id = int(input("\nВведите id для удаления: "))
                    work_js.del_vacancies(user_id)
                    answer_vacancy_list = work_js.get_vacancies()

                elif choice_action == 5:
                    work_js.add_vacancies(work_js.preparation_data_user())
                    answer_vacancy_list = work_js.get_vacancies()
                    print("Вакансия добавлена.")

                elif choice_action == 6:
                    answer_vacancy_list = [line for line in all_vacancy_list if "superjob.ru" in line['url']]

                elif choice_action == 7:
                    answer_vacancy_list = [line for line in all_vacancy_list if "hh.ru" in line['url']]

                elif choice_action == 8:
                    try:
                        user_vacancies = int(input("\nВведите количество вакансий в топ списке: "))
                        sort_data = SortVacancies()
                        actual_vacancy_list = [line for line in all_vacancy_list if
                                               isinstance(line['salary_from'], int)][
                                              :user_vacancies]
                        answer_vacancy_list = sort_data.sort_vacancies('salary_from', actual_vacancy_list)
                    except ValueError:
                        print("Не верный ввод, вводимые данные должны быть целым числом от 1 до 100. "
                              "Попробуйте ещё раз")


                elif choice_action == 9:
                    print("Программа завершена.")
                    break
                else:
                    print("Операцию на этот номер пока не назначили. Попробуйте ещё раз")
                    continue

                print_result(answer_vacancy_list)

            except ValueError:
                print("Не верный ввод, вводимые данные должны быть целым числом. Попробуйте ещё раз")
                continue
        else:
            print("Поиск не дал результатов. Попробуйте запустить программу снова с более точным запросом.")
            break


def print_result(vacancy_list):
    '''Выводит результат запроса пользователя на экран'''
    for line_vacancy in vacancy_list:
        print(PerformanceVacancies(line_vacancy).__str__())
