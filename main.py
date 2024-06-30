import logging

from src.api import HhAPI
from src.exceptions import APIException
from src.utils import get_vacancies_instances

logger = logging.getLogger(__name__)


def main():
    hh = HhAPI()
    hh.text = input("Введите текст:")
    try:
        data = hh.get_response_data()
    except APIException as e:
        logger.exception(f"Ошибка обращения к HHAPI. {e}")
        print("Сервис временно недоступен. Обратитесь позже")
    instances = get_vacancies_instances(data)


if __name__ == "__main__":
    main()
