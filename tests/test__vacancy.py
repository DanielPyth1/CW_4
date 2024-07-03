import pytest
from src.vacancy import Vacancy


def test_create_vacancy():
    vacancy_data = {
        "pk": 1,
        "name": "Software Engineer",
        "salary_from": 50000,
        "salary_to": 100000
    }
    vacancy = Vacancy.create_vacancy(vacancy_data)

    assert vacancy.pk == 1
    assert vacancy._Vacancy__name == "Software Engineer"
    assert vacancy._Vacancy__salary_from == 50000
    assert vacancy._Vacancy__salary_to == 100000


def test_create_vacancy_from_string():
    vacancy_str = "pk=2,name=Data Scientist,salary_from=60000,salary_to=120000"
    vacancy = Vacancy.create_vacancy(vacancy_str)

    assert vacancy.pk == 2
    assert vacancy._Vacancy__name == "Data Scientist"
    assert vacancy._Vacancy__salary_from == 60000
    assert vacancy._Vacancy__salary_to == 120000


def test_to_dict():
    vacancy_data = {
        "pk": 3,
        "name": "Product Manager",
        "salary_from": 70000,
        "salary_to": 130000
    }
    vacancy = Vacancy.create_vacancy(vacancy_data)

    vacancy_dict = vacancy.to_dict()

    assert vacancy_dict == {
        "pk": 3,
        "salary_from": 70000,
        "salary_to": 130000
    }


def test_salary_validation():
    vacancy_data = {
        "pk": 4,
        "name": "HR Specialist",
        "salary_from": -5000,
        "salary_to": 20000
    }
    vacancy = Vacancy.create_vacancy(vacancy_data)

    assert vacancy._Vacancy__salary_from == 0
    assert vacancy._Vacancy__salary_to == 20000


def test_comparison_operators():
    vacancy_data_1 = {
        "pk": 5,
        "name": "Frontend Developer",
        "salary_from": 50000,
        "salary_to": 90000
    }
    vacancy_data_2 = {
        "pk": 6,
        "name": "Backend Developer",
        "salary_from": 60000,
        "salary_to": 110000
    }
    vacancy1 = Vacancy.create_vacancy(vacancy_data_1)
    vacancy2 = Vacancy.create_vacancy(vacancy_data_2)

    assert vacancy1 < vacancy2
    assert vacancy2 > vacancy1


def test_str_repr():
    vacancy_data = {
        "pk": 7,
        "name": "DevOps Engineer",
        "salary_from": 80000,
        "salary_to": 150000
    }
    vacancy = Vacancy.create_vacancy(vacancy_data)

    assert str(vacancy) == "Vacancy: DevOps Engineer, Salary: 80000 - 150000"
    assert repr(vacancy) == "Vacancy: DevOps Engineer, Salary: 80000 - 150000"


# Запустить тесты с помощью pytest
if __name__ == "__main__":
    pytest.main()
