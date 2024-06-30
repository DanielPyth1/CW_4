class Vacancy:
    __slots__ = ["__name", "__salary_from", "__pk"]

    def __init__(self, pk: int, name: str, salary_from: str) -> None:
        self.__name = name
        self.__pk = pk
        self.__salary_from = self.__validate_salary(salary_from)

    @property
    def pk(self):
        return self.__pk

    def __str__(self) -> str:
        return f"Vacancy: {self.__name}, Salary: {self.__salary_from}"

    def __repr__(self) -> str:
        return f"Vacancy: {self.__name}, Salary: {self.__salary_from}"

    @staticmethod
    def __validate_salary(salary: int) -> int:
        return 0 if salary < 0 else salary

    def __lt__(self, other):
        return self.__salary_from < other.__salary_from

    def __gt__(self, other):
        return self.__salary_from > other.__salary_from

    @classmethod
    def create_vacancy(cls, vacancy_data: dict):
        cls(
            pk=vacancy_data["pk"],
            name=vacancy_data["name"],
            salary_from=vacancy_data["salary_from"],
        )


    def to_dict(self) -> dict:
        return {
            "pk": self.__pk,
            "salary_from": self.__salary_from,
        }



