from bs4 import BeautifulSoup


with open('website.html','r') as f:
    content = f.read()


# Provide markup and parser
soup = BeautifulSoup(content, 'html.parser')

