import logging

HH_URL = "https://api.hh.ru/vacancies"

FORMAT = '%(asctime)s %(message)s'

logging.basicConfig(level=logging.INFO, filename="py_log.log", filemode="a", format=FORMAT)
