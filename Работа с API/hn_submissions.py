from operator import itemgetter

import requests
from plotly.graph_objs import Bar
from plotly import offline

# Вызов API и сохранение ответа
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Статус: {r.status_code}")

# Обработка информации о каждой статье
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:8]:
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    # Построение словаря для каждой статьи
    submission_dict = {
        'title': response_dict['title'],
        'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict['descendants'],
        'heading': response_dict['by'],
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                          reverse=True)

titles, links, comments, headings = [], [], [], []
for submission_dict in submission_dicts:
    link = f"<a href='{submission_dict['hn_link']}'" \
           f">{submission_dict['title']}</a>"
    titles.append(submission_dict['title'])
    links.append(link)
    comments.append(submission_dict['comments'])
    headings.append(submission_dict['heading'])
#     print(f"\nTitle: {submission_dict['title']}")
#     print(f"Discussion link: {submission_dict['hn_link']}")
#     print(f"Comments: {submission_dict['comments']}")

# Построение визуализации
data = [{
    'type': 'bar',
    'x': links,
    'y': comments,
    'hovertext': headings,
    'marker': {
        'color': 'rgb(0, 240, 55)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
}]
my_layout = {
    'title': 'Статьи',
    'titlefont': {'size': 28},
    'xaxis': {
        'title': 'Статьи',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': 'Комментарии',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14}
    },
}
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='статьи.html')



