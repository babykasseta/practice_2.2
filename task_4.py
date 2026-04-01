import requests

# функция для получения информации о пользователе
def get_user():
    username = input("Введите username GitHub: ")
    url = f"https://api.github.com/users/{username}"

    response = requests.get(url)
    if response.status_code != 200:
        print("Пользователь не найден")
        return

    data = response.json()

    # выводим нужные поля
    print("Имя пользователя:", data["login"])
    print("Ссылка на профиль:", data["html_url"])
    print("Репозитории:", data["public_repos"])
    print("Подписчики:", data["followers"])
    print("Подписки:", data["following"])


# функция для получения всех репозиториев пользователя
def get_repos():
    username = input("Введите username GitHub: ")
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)

    if response.status_code != 200:
        print("Пользователь не найден")
        return

    repos = response.json()

    for repo in repos:
        print("Название:", repo["name"])
        print("Ссылка:", repo["html_url"])
        print("Звёзды:", repo["stargazers_count"])
        print("Язык:", repo["language"])
        print("Видимость:", repo.get("visibility", "public"))
        print("Ветка по умолчанию:", repo["default_branch"])
        print("-" * 30)


#функция для поиска репозиториев по названию
def search_repos():
    query = input("Введите название репозитория для поиска: ")
    url = f"https://api.github.com/search/repositories?q={query}"
    response = requests.get(url)

    if response.status_code != 200:
        print("Ошибка поиска")
        return

    results = response.json()["items"]

    for repo in results[:5]:
        print("Название:", repo["name"])
        print("Ссылка:", repo["html_url"])
        print("Автор:", repo["owner"]["login"])
        print("Звёзды:", repo["stargazers_count"])
        print("Язык:", repo["language"])
        print("-" * 30)


# главное меню
def main():
    while True:
        print("\nМеню:")
        print("1 - Просмотреть профиль пользователя")
        print("2 - Показать репозитории пользователя")
        print("3 - Поиск репозиториев по названию")
        print("0 - Выход")

        choice = input("Выбор: ")

        if choice == "1":
            get_user()
        elif choice == "2":
            get_repos()
        elif choice == "3":
            search_repos()
        elif choice == "0":
            print("Выход из программы")
            break
        else:
            print("Неверный ввод. Попробуйте снова.")


if __name__ == "__main__":
    main()