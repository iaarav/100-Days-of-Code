import requests
from bs4 import BeautifulSoup
from spotipy import SpotifyOAuth, Spotify
from pprint import pprint

CLIENT_ID = "YOUR ID"
CLIENT_SECRET = "YOUR SECRET"

sp = Spotify(
    oauth_manager=SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri="http://127.0.0.1:5000",
        scope="playlist-modify-private",
        cache_path="token.txt",
        show_dialog=True
    )
)

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:")
URL = f"https://www.billboard.com/charts/hot-100/{date}"

content = requests.get(URL).text
soup = BeautifulSoup(content, "html.parser")

songNames = [t.text.strip() for t in soup.select("li ul li h3")]
year = date.split("-")[0]

print(songNames)

songUrls = []

for song in songNames:
    result = sp.search(q=f"track:{song} year:{year}", type="track")

    try:
        url = result["tracks"]["items"][0]["uri"]
        songUrls.append(url)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(
    user=sp.current_user()["id"],
    name=f"{date} BILLBOARD top 100",
    public=False,
    collaborative=False,
    description="This is the billboard top 100 for the said date."
)

sp.playlist_add_items(playlist_id=playlist["id"], items=songUrls)