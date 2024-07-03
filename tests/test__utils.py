import pytest
from src.vacancy import Vacancy
from src.utils import get_vacancies_instances, sort_vacancies, convert_salary, filter_by_salary

@pytest.fixture
def sample_vacancies():
    return [
        {"pk": 1, "name": "Engineer", "salary_from": 50000, "salary_to": 80000},
        {"pk": 2, "name": "Manager", "salary_from": 60000, "salary_to": 90000},
        {"pk": 3, "name": "Developer", "salary_from": 70000, "salary_to": 100000},
    ]

@pytest.fixture
def sample_currency_conversion():
    return {
        "USD": 0.013,
    }

def test_get_vacancies_instances(sample_vacancies):
    vacancies = get_vacancies_instances(sample_vacancies)
    assert len(vacancies) == 3
    assert all(isinstance(vacancy, Vacancy) for vacancy in vacancies)

def test_sort_vacancies(sample_vacancies):
    vacancies = get_vacancies_instances(sample_vacancies)
    sorted_vacancies = sort_vacancies(vacancies)
    assert len(sorted_vacancies) == 3
    assert sorted_vacancies[0].pk == 3
    assert sorted_vacancies[-1].pk == 1

def test_convert_salary(sample_vacancies, sample_currency_conversion):
    vacancies = get_vacancies_instances(sample_vacancies)
    converted_vacancies = convert_salary(vacancies, sample_currency_conversion)
    assert len(converted_vacancies) == 3
    assert converted_vacancies[0].salary_from == pytest.approx(650)
    assert converted_vacancies[1].salary_to == pytest.approx(1170)

def test_filter_by_salary(sample_vacancies):
    vacancies = get_vacancies_instances(sample_vacancies)
    filtered_vacancies = filter_by_salary(vacancies, salary_from=60000, salary_to=90000)
    assert len(filtered_vacancies) == 2
    assert all(vacancy.salary_from >= 60000 and vacancy.salary_to <= 90000 for vacancy in filtered_vacancies)
