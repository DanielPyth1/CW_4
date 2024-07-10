from pathlib import Path

PATH_VACANCIES = Path(__file__).parent.joinpath("vacancies.json")

PATH_LOG = Path(__file__).parent.joinpath("log.txt")

HH_VACANCIES_URL = "https://api.hh.ru/vacancies"
HH_HEADERS = {"User-Agent": "oociso@ya.ru"}
COUNT_HH = 100

BASES_ID_SJ = 2996
SECRET_KEY_SJ = "v3.r.111847284.4352b84a837eb770efe1e81582e6a49a021cac26.f32f2ba64ad2dd647ad8173eef63ed25154ee812"
SJ_VACANCIES_URL = "https://api.superjob.ru/2.0/vacancies/"
SJ_HEADERS = {"X-Api-App-Id": SECRET_KEY_SJ}
COUNT_SJ = 100

currency_change = {
    "AUD": 0.01749,
    "AZN": 0.01909,
    "GBP": 0.00922,
    "AMD": 4.6977,
    "BYR": 0.03391957668,
    "BR": 0.03391957668,
    "Br": 0.03391957668,
    "BYN": 0.03815,
    "BGN": 0.0206,
    "BRL": 0.0512547,
    "HUF": 3.78179067789,
    "VND": 250.5154355,
    "HKD": 0.081277,
    "GEL": 0.0279867,
    "DKK": 0.0729847,
    "AED": 0.04283,
    "USD": 0.01166,
    "EUR": 0.01088,
    "EGP": 0.3216675,
    "INR": 0.9721,
    "IDR": 160.3155009,
    "KZT": 5.5218,
    "CAD": 0.01595,
    "QAR": 0.0379001785,
    "KGS": 0.9706,
    "CNY": 0.0847,
    "MDL": 0.188905,
    "NZD": 0.02,
    "NOK": 0.1246,
    "PLN": 0.0448887,
    "RON": 0.04863387,
    "XDR": 0.00790822,
    "SGD": 0.0142292,
    "TJS": 0.114122,
    "THB": 0.376282,
    "TRY": 0.38161,
    "TMT": 0.03644248,
    "UZS": 126.923848,
    "SO'M": 0.007873,
    "UAH": 0.4718,
    "CZK": 0.2393226,
    "SEK": 0.116402375,
    "CHF": 0.01048,
    "RSD": 1.14505958,
    "ZAR": 0.1962558,
    "KRW": 11.71,
    "JPY": 1.8762
}
