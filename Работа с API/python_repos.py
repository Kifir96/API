import requests

# Создание вызова API и сохранение ответа
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Статус: {r.status_code}")

# Сохранение ответа API в переменной
response_dict = r.json()
print(f"Всего репозиториев: {response_dict['total_count']}")

# Анализ информации о репозиториях
repo_dicts = response_dict['items']
print(f"Кол-во возвращенных репозиториев: {len(repo_dicts)}")

# Анализ первого репозитория
# repo_dict = repo_dicts[0]
# print(f"\nКлючей: {len(repo_dict)}")
# for key in sorted(repo_dict.keys()):
#     print(key)


print('\nИнформация о каждом репозитории:')
for repo_dict in repo_dicts:
    print(f"Name: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Description: {repo_dict['description']}")