import requests
import json


def get_data():
    url = "https://www.cbr-xml-daily.ru/daily_json.js"
    try:
        response = requests.get(url)
        return response.json()
    except:
        print("Ошибка при получении данных")
        return {"Valute": {}}


def show_all(data):
    print("\nКурсы валют:")
    for code, val in data["Valute"].items():
        print(code, "-", val["Value"])
    print()


def show_one(data):
    code = input("Введите код валюты: ").upper()

    if code in data["Valute"]:
        print(code, "-", data["Valute"][code]["Value"])
    else:
        print("Валюта не найдена")
    print()


def create_group(groups):
    name = input("Введите название группы: ")

    if name in groups:
        print("Такая группа уже существует\n")
    else:
        groups[name] = []
        print("Группа создана\n")


def show_groups(groups):
    if not groups:
        print("Групп нет\n")
        return

    print("\nСписок групп:")
    for name, currencies in groups.items():
        if currencies:
            print(name + ":", ", ".join(currencies))
        else:
            print(name + ": пусто")
    print()


def edit_group(groups, data):
    name = input("Введите название группы: ")

    if name not in groups:
        print("Группа не найдена\n")
        return

    print("1 - Добавить валюту")
    print("2 - Удалить валюту")

    choice = input("Выбор: ")

    if choice == "1":
        cur = input("Введите код валюты: ").upper()

        if cur not in data["Valute"]:
            print("Такой валюты нет\n")
        elif cur in groups[name]:
            print("Валюта уже есть в группе\n")
        else:
            groups[name].append(cur)
            print("Добавлено\n")

    elif choice == "2":
        cur = input("Введите код валюты: ").upper()

        if cur in groups[name]:
            groups[name].remove(cur)
            print("Удалено\n")
        else:
            print("Такой валюты нет в группе\n")
    else:
        print("Неверный выбор\n")


def save_groups(groups):
    try:
        with open("save.json", "w", encoding="utf-8") as f:
            json.dump(groups, f, ensure_ascii=False, indent=4)
    except:
        print("Ошибка при сохранении")


def load_groups():
    try:
        with open("save.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return {}

#меню
def main():
    data = get_data()
    groups = load_groups()

    while True:
        print("Меню:")
        print("1 - Показать все валюты")
        print("2 - Найти валюту")
        print("3 - Создать группу")
        print("4 - Показать группы")
        print("5 - Изменить группу")
        print("0 - Выход")

        choice = input("Выбор: ")

        if choice == "1":
            show_all(data)

        elif choice == "2":
            show_one(data)

        elif choice == "3":
            create_group(groups)

        elif choice == "4":
            show_groups(groups)

        elif choice == "5":
            edit_group(groups, data)

        elif choice == "0":
            save_groups(groups)
            print("Выход из программы")
            break

        else:
            print("Неверный ввод\n")


if __name__ == "__main__":
    main()