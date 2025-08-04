mport requests
from bs4 import BeautifulSoup
import os
import dotenv
import spotipy
from flask.cli import load_dotenv
from spotipy import SpotifyOAuth


load_dotenv()

client_id = os.getenv("client_id")
client_secret = os.getenv("client_secret")
token = os.getenv("token")


date_entry  = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:")
url = "https://www.billboard.com/charts/hot-100/"
final = url+date_entry
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
response = requests.get(final,headers=header)
data =  response.text
soup = BeautifulSoup(data,"html.parser")
song_name = soup.select("html body main div div div  ul li ul li h3")

nos=[no.getText().split() for no in song_name]
# band_name = soup.find_all("span", class_="c-label a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only")
result = [' '.join(inner_list) for inner_list in nos]

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                                           client_secret=client_secret,
                                                           redirect_uri="http://example.com",
                                                            scope="playlist-modify-private playlist-modify-public"))

current_user = sp.current_user()
user_id = current_user["id"]
print(f"Logged in as: {current_user['display_name']}")
year=2000
songs=[]
for x in result:
    results = sp.search(q=f'track:{x} year:{year}', type='track')
    try:
        songs.append(results["tracks"]["items"][0]["uri"])
    except IndexError:
        pass

playlist = sp.user_playlist_create(user=user_id, name=f"Billboard Top 100 from {date_entry}", public=False,
                                   description=f"Top 100 songs from {date_entry}")
playlist_id = playlist["id"]
print(playlist_id)
print(songs)
sp.playlist_add_items(playlist_id=playlist_id,items=songs)
