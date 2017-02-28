import json
import codecs
from bs4 import BeautifulSoup

html_article = codecs.open("article.html").read()
soup = BeautifulSoup(html_article, 'html.parser')
html_code = str(soup.find_all("div", class_="article_long")[0])
s = soup.find('script')