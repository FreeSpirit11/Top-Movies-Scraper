from bs4 import BeautifulSoup
import requests

URL="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response=requests.get(URL)
response.raise_for_status()
website_html = response.text

soup=BeautifulSoup(website_html, "html.parser")
all_movies = soup.find_all(name="h3", class_="title")

movies=[movie.getText() for movie in all_movies]
movies.reverse()

with open("movies.txt", "w", encoding="UTF-8") as file:
    for movie in movies:
        file.write(f"{movie}\n")
