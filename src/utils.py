from src.vacancy import Vacancy


def get_vacancies_instances(vacancies: list[dict]) -> list[Vacancy]:
    """

    :param vacancies:
    :return:
    """
    return [Vacancy.create_vacancy(vacancy) for vacancy in vacancies]


def sort_vacancies(vacancies: list[Vacancy]) -> list[Vacancy]:
    return sorted(vacancies, reverse=True)


def convert_salary(vacancies_data: list[Vacancy], response_salary_currency: list[dict]) -> list[Vacancy]:
    for vacancy in vacancies_data:
        currency_coef = response_salary_currency.get(vacancy.currency)
        vacancy.salary_from = vacancy.salary_from * currency_coef
    return vacancies_data
