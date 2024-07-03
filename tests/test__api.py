import pytest
from src.api import HhAPI, API
from src.exceptions import HhAPIException


@pytest.fixture
def hh_api_instance():
    return HhAPI()


def test_hh_api_url_property(hh_api_instance):
    assert hh_api_instance.url == "https://api.hh.ru/vacancies/api"


def test_hh_api_set_text(hh_api_instance):
    hh_api_instance.text = "Engineer"
    assert hh_api_instance.text == "Engineer"


def test_hh_api_set_empty_text_raises_exception(hh_api_instance):
    with pytest.raises(HhAPIException):
        hh_api_instance.text = ""


def test_hh_api_get_response(hh_api_instance):
    hh_api_instance.text = "Engineer"
    response_data = hh_api_instance.get_response_data()
    assert isinstance(response_data, list)
    assert len(response_data) > 0
    assert "id" in response_data[0]
    assert "name" in response_data[0]


def test_hh_api_get_response_without_text_raises_exception(hh_api_instance):
    with pytest.raises(HhAPIException):
        hh_api_instance.get_response_data()


def test_hh_api_get_response_invalid_url_raises_exception(hh_api_instance):
    hh_api_instance.text = "Engineer"
    hh_api_instance.url = "https://api.hh.ru/vacancies/api"

    with pytest.raises(HhAPIException):
        hh_api_instance.get_response_data()


def test_hh_api_get_response_http_error_raises_exception(hh_api_instance):
    hh_api_instance.text = "Engineer"
    hh_api_instance.url = "https://api.hh.ru/vacancies/404"

    with pytest.raises(HhAPIException):
        hh_api_instance.get_response_data()

