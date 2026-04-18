from bs4 import BeautifulSoup
import requests


soup_ingredients = requests.get('https://appbrewery.github.io/news.ycombinator.com/').text
soup = BeautifulSoup(soup_ingredients, 'html.parser')

article_tags = soup.find_all(class_='storylink')
aticle_upvotes = soup.find_all(name='span', class_='score')

article_tag_texts = [i.text for i in article_tags]
article_upvotes_all = [i.text.replace(' points', '') for i in aticle_upvotes]
article_links = [i.get('href') for i in article_tags]


max_voted_article_index = article_upvotes_all.index(max(article_upvotes_all))
max_article = article_tag_texts[max_voted_article_index]


print(f"The article with the most votes is {max_article} with {article_upvotes_all[max_voted_article_index]} points. Link to article: {article_links[max_voted_article_index]}")