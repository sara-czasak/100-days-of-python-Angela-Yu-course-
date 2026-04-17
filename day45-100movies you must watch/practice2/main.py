from bs4 import BeautifulSoup
import requests


soup_ingredients = requests.get('https://news.ycombinator.com/news').text
soup = BeautifulSoup(soup_ingredients, 'html.parser')


articles = soup.select('.titleline')
article_titles = [i.getText() for i in articles]


scores = soup.select('.score')
score = [i.text.replace(' points', '') for i in scores]
index = score.index(max(score))
print(index)


# max_score_title = article_titles[index]
# print(max_score_title)

# # print(article_titles)
# print(articles[0])
