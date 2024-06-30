import pytest

from src.exceptions import HhAPIException


def test__get_response_data(hh_api):
    with pytest.raises(HhAPIException):
        hh_api.get_response_data()
