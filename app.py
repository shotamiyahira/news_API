import requests
import time

response_id = requests.get(
    "https://hacker-news.firebaseio.com/v0/topstories.json")

id_list = response_id.json()

for post_id in id_list:
    response_news = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{post_id}.json")
    news_data = response_news.json()

    dic = {"title": news_data["title"], "link": news_data["url"]}
    print(dic)
    time.sleep(1)
    if post_id == id_list[4]:
        break
