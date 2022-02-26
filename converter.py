from ytmusicapi import YTMusic
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

sp_client_id = "" # create spotify web app and fill
sp_client_secret = ""

client_credentials_manager = SpotifyClientCredentials(client_id=sp_client_id, client_secret=sp_client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

yt = YTMusic("headers_auth.json")

sp_playlist_id = "" # spotify playlist id 
yt_playlist_id = "" # youtube playlist id

sp_pl = sp.playlist_tracks(sp_playlist_id)
yt_pl = yt.get_playlist(yt_playlist_id)

yt_pl_l = []

for i in yt_pl["tracks"]:
    yt_pl_l.append(i)

yt.remove_playlist_items(yt_playlist_id, yt_pl_l)

sp_pl_l = []

for i in sp_pl["items"]:
    sp_pl_l.append(i["track"]["name"] + " - " + i["track"]["artists"][0]["name"])

yt_search = []

for i in sp_pl_l:
    yt_vid_id = yt.search(query=i, filter="songs", limit=1, ignore_spelling=True)
    yt_search.append(yt_vid_id[0]["videoId"])

yt.add_playlist_items(yt_playlist_id, yt_search, duplicates=True)
