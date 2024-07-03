import json
import pytest
from pathlib import Path
from src.saver import JsonSaver
from src.vacancy import Vacancy


@pytest.fixture
def json_file_path(tmp_path):
    json_data = [
        {"pk": 1, "name": "Engineer", "salary_from": 50000, "salary_to": 80000},
        {"pk": 2, "name": "Manager", "salary_from": 60000, "salary_to": 90000},
        {"pk": 3, "name": "Developer", "salary_from": 70000, "salary_to": 100000},
    ]
    json_file = tmp_path / "test_data.json"
    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(json_data, f)
    return json_file


def test_write_data(json_file_path):
    json_saver = JsonSaver(json_file_path)

    vacancies_to_write = [
        Vacancy(4, "Designer", 55000, 85000),
        Vacancy(5, "Analyst", 65000, 95000)
    ]

    json_saver.write_data(vacancies_to_write)

    with open(json_file_path, "r", encoding="utf-8") as f:
        updated_data = json.load(f)

    assert len(updated_data) == 5
    assert any(vacancy["name"] == "Designer" for vacancy in updated_data)
    assert any(vacancy["name"] == "Analyst" for vacancy in updated_data)


def test_delete_data(json_file_path):
    json_saver = JsonSaver(json_file_path)

    query = {
        "salary_from": 60000,
        "salary_to": 90000
    }

    json_saver.delete_data(query)

    with open(json_file_path, "r", encoding="utf-8") as f:
        updated_data = json.load(f)

    assert len(updated_data) == 1
    assert all(vacancy["salary_from"] < query["salary_from"] or vacancy["salary_to"] > query["salary_to"] for vacancy in
               updated_data)
