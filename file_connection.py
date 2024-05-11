import json


def get_articles():
    with open('articles.json', 'r', encoding='utf-8') as json_file:
        s = json.load(json_file)
    return s


def save_article(name, text):
    with open("articles.json", "r", encoding="utf-8") as json_file:
        articles = json.load(file)
    articles[name] = text


    with open("articles.json", "w", encoding="utf-8") as json_file:
        json.dump(articles, file, ensure_ascii=False)


def delete_article(name):
    with open("articles.json", "r", encoding="utf-8") as json_file:
        articles = json.load(json_file)


    del articles[name]
    with open("articles.json", "w", encoding="utf-8") as json_file:
        json.dump(articles, file, ensure_ascii=False)
