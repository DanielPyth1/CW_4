import pytest

from src.api import HhAPI
from src.vacancy import Vacancy


@pytest.fixture
def vacancy():
    return Vacancy(
        pk=35,
        name="fkfkfkff",
        salary_from="0"
    )


@pytest.fixture
def list_vacancy():
    return [
        Vacancy(
            pk=35,
            name="fkfkfkff",
            salary_from="5587"
        ),
        Vacancy(
            pk=39,
            name="hjkkgk",
            salary_from="1755"
        )
    ]


@pytest.fixture
def vacancy_dict():
    return {
        "pk": 4567876543,
        "name": "ktkotkkgtork",
        "salary_from": "0"
    }


@pytest.fixture
def hh_api():
    return HhAPI()