class Vacancy:
    __slots__ = ["__name", "__salary_from", "__salary_to", "__pk"]

    def __init__(self, pk: int, name: str, salary_from: int, salary_to: int) -> None:
        self.__name = name
        self.__pk = pk
        self.__salary_from = self.__validate_salary(salary_from)
        self.__salary_to = self.__validate_salary(salary_to)

    @property
    def pk(self):
        return self.__pk

    def __str__(self) -> str:
        return f"Vacancy: {self.__name}, Salary: {self.__salary_from} - {self.__salary_to}"

    def __repr__(self) -> str:
        return f"Vacancy: {self.__name}, Salary: {self.__salary_from} - {self.__salary_to}"

    @staticmethod
    def __validate_salary(salary: int) -> int:
        return 0 if salary < 0 else salary

    def __lt__(self, other):
        return self.__salary_from < other.__salary_from

    def __gt__(self, other):
        return self.__salary_from > other.__salary_from

    @classmethod
    def create_vacancy(cls, vacancy_data):
        if isinstance(vacancy_data, str):
            vacancy_data = cls.parse_string_to_dict(vacancy_data)
        return cls(
            pk=int(vacancy_data["pk"]),
            name=vacancy_data["name"],
            salary_from=int(vacancy_data["salary_from"]),
            salary_to=int(vacancy_data["salary_to"]),
        )

    @staticmethod
    def parse_string_to_dict(data: str) -> dict:
        result = {}
        items = data.split(',')
        for item in items:
            key, value = item.split('=')
            if key.strip() in {"salary_from", "salary_to", "pk"}:
                result[key.strip()] = int(value.strip())
            else:
                result[key.strip()] = value.strip()
        return result

    def to_dict(self) -> dict:
        return {
            "pk": self.__pk,
            "salary_from": self.__salary_from,
            "salary_to": self.__salary_to,
        }
