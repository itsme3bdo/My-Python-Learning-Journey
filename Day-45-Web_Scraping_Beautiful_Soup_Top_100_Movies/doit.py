import requests
from bs4 import BeautifulSoup

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2//")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage,"html.parser")
movie_names = soup.find_all(name="h3",class_="title")
movies=[movie.getText() for movie in movie_names]

movies.reverse()
with open("movies.txt","w") as file:
    for movie in movies:
        file.write(f"{movie}\n")

