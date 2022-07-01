import requests
import time

res = requests.get('https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty')
# print(res.text)
# print(type(res.json()))

dic = res.json()
print(dic)

for i in range(0, 50):
    news_id = dic[i]
    contents = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{news_id}.json?print=pretty")
    data = contents.json()
    print("'title': '", data.get("title"), "', 'Link':", data.get("url", None))
    time.sleep(1)