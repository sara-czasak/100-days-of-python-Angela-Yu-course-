from bs4 import BeautifulSoup


with open('website.html','r') as f:
    content = f.read()


# Provide markup and parser
soup = BeautifulSoup(content, 'html.parser')

# .string gets the content of the tag
title = soup.title.string

# find all tags
a = soup.find_all('a')
p = soup.find_all('p')

# for tag in a:
#     # get value of any of the attributes, in this case href
#     print(tag.get('href'))


# get tag by id
# heading = soup.find('h1', id='name')


# get tag by class (class is class_ not to clash with object class creation
# section_heading = soup.find('h3', class_='heading')
#
#
# company_url = soup.select_one(selector='p a')
#
# name = soup.select_one(selector='#name')
#
# heading1 = soup.select('.heading')
#
# print(heading1)