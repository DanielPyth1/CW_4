import json
from abc import ABC, abstractmethod
from pathlib import Path

from src.utils import get_vacancies_instances, filter_by_salary
from src.vacancy import Vacancy


class Saver(ABC):

    @abstractmethod
    def load_data(self):
        raise NotImplementedError()

    @abstractmethod
    def write_data(self, data) -> None:
        raise NotImplementedError()

    @abstractmethod
    def delete_data(self, query: dict) -> None:
        raise NotImplementedError()


class JsonSaver(Saver):

    def __init__(self, path: Path = Path("data")):
        self.__path = path

    def load_data(self) -> list[dict]:
        with open(self.__path, encoding="utf-8") as f:
            return json.load(f)

    def write_data(self, vacancies: list[Vacancy]) -> None:
        old_data = self.load_data()
        old_instances = get_vacancies_instances(old_data)
        old_ids = [instance.pk for instance in old_instances]

        data_for_write = [vacancy.to_dict() for vacancy in vacancies if vacancy.pk not in old_ids]
        data_for_write.extend(old_data)
        self.__save_data(data_for_write)

    def delete_data(self, query: dict) -> None:
        old_data = self.load_data()
        old_instances = get_vacancies_instances(old_data)
        filtered_instances = filter_by_salary(
            old_instances, salary_from=query["salary_from"],
            salary_to=query["salary_to"]
        )
        data_for_write = [vacancy.to_dict() for vacancy in filtered_instances]
        self.__save_data(data_for_write)

    def __save_data(self, data_for_write):
        with open(self.__path, "w", encoding="utf-8") as f:
            json.dump(data_for_write, f, ensure_ascii=False, indent=4)

