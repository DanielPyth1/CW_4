from utils import users_work


def main():
    """Запускаем программу для работы с пользователем"""

    text_search = str(input("Введите слово или фразу для поиска: "))
    # Ищем вакансии.
    # Сохраняем в файл.
    # Выводим без сортировки
    users_work(text_search)


if __name__ == "__main__":
    main()
