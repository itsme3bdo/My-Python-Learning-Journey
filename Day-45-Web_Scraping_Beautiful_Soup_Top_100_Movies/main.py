from operator import index

from bs4 import BeautifulSoup
import requests

response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")
yc_webpage = response.text

soup  = BeautifulSoup(yc_webpage,"html.parser")
articles = soup.select(".storylink")
article_texts  = []
article_links  = []
# article_text  = soup.find(name="a",class_="storylink")

for article_tag  in articles:
    text =  article_tag.getText()
    link = article_tag.get("href")
    article_texts.append(text)
    article_links.append(link)
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span",class_="score")]

print(article_links)
print(article_texts)
print(article_upvotes)
highest = max(article_upvotes)
first =  article_upvotes.index(highest)
print(article_texts[first])
print(article_links[first])
print(highest)


# with open("website.html") as file:
#     contents = file.read()
# # print(contents)
#
# soup = BeautifulSoup(contents, "lxml")
#
# # print(soup.prettify())
# # print(soup.title)
# # print(soup.a)
# # print(soup.title.name)
# # print(soup.tittle.string)
#
# all_anchor_tags = soup.find_all(name="a")
# for tag in all_anchor_tags:
#     # print(tag.getText())
#     print(tag.get("href"))  #to get value of attributes
#
# heading  = soup.find(name="h1",id="name") #get specific element
#
# section_heading  = soup.find(name="h3",class_="heading")# find all to get all items
# print(section_heading.getText())  #getText to get the text inside
#
# company_url = soup.select_one(selector="p a") #select_one selects the first item,  select selects all items || matching criteria
# print(company_url)
#
# name = soup.select_one(selector="#name")
# print(name)
#
# headings = soup.select(".heading")  #basically use  similar style to css
# print(headings)
