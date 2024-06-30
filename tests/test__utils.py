from src.utils import get_vacancies_instances
from src.vacancy import Vacancy


def test__get_vacancies_instances(vacancy_dict: dict, vacancy: Vacancy):
    assert get_vacancies_instances(vacancy_dict) == [vacancy]


def test__sort_vacancies(vacancy_dict: dict, vacancy: Vacancy, sort_vacancies: list[Vacancy]):
    assert sort_vacancies == [
        Vacancy(pk=35, name="fkfkfkff", salary_from=5587),
        Vacancy(pk=39, name="hjkkgk", salary_from=1755)
    ]

