from src.vacancy import Vacancy


def get_vacancies_instances(vacancies: list[dict]) -> list[Vacancy]:
    """
    Преобразует список словарей вакансий в список экземпляров класса Vacancy.
    :param vacancies: Список словарей вакансий
    :return: Список экземпляров класса Vacancy
    """
    return [Vacancy.create_vacancy(vacancy) for vacancy in vacancies]


def sort_vacancies(vacancies: list[Vacancy]) -> list[Vacancy]:
    """
    Сортирует список вакансий по убыванию зарплаты.
    :param vacancies: Список экземпляров класса Vacancy
    :return: Отсортированный список вакансий
    """
    return sorted(vacancies, reverse=True)


def convert_salary(vacancies_data: list[Vacancy], response_salary_currency: dict) -> list[Vacancy]:
    """
    Конвертирует зарплату вакансий в указанную валюту.
    :param vacancies_data: Список экземпляров класса Vacancy
    :param response_salary_currency: Словарь с коэффициентами конверсии валют
    :return: Список вакансий с конвертированными зарплатами
    """
    for vacancy in vacancies_data:
        currency_coef = response_salary_currency.get(vacancy.currency)
        if currency_coef:
            vacancy.salary_from = vacancy.salary_from * currency_coef
            vacancy.salary_to = vacancy.salary_to * currency_coef
    return vacancies_data


def filter_by_salary(vacancies: list[Vacancy], salary_from: int, salary_to: int) -> list[Vacancy]:
    """
    Фильтрует список вакансий по диапазону зарплат.
    :param vacancies: Список экземпляров класса Vacancy
    :param salary_from: Минимальная зарплата
    :param salary_to: Максимальная зарплата
    :return: Отфильтрованный список вакансий
    """
    return [vacancy for vacancy in vacancies if salary_from <= vacancy.salary_from <= salary_to]

