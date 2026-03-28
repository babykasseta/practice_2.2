import requests


def get_status(code):
    if code == 200:
        return "доступен"
    elif code == 403:
        return "вход запрещен"
    elif code == 404:
        return "не найден"
    elif code >= 500:
        return "ошибка сервера"
    else:
        return "неизвестный статус"


def check_url(url):
    try:
        response = requests.get(url, timeout=10)
        code = response.status_code
        status = get_status(code)
        print(f"{url} – {status} – {code}")
    except:
        print(f"{url} – не доступен – ошибка соединения")


def main():
    urls = [
        "https://github.com/",
        "https://www.binance.com/en",
        "https://tomtit.tomsk.ru/",
        "https://jsonplaceholder.typicode.com/",
        "https://moodle.tomtit-tomsk.ru/"
    ]

    for url in urls:
        check_url(url)


if __name__ == "__main__":
    main()