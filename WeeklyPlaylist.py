import spotipy
from spotipy.oauth2 import SpotifyOAuth
import datetime
import schedule
import time

today = datetime.date.today()
sunday = today + datetime.timedelta(days=(6 - today.weekday() + 7) % 7)

scope = 'playlist-modify-private'
playlist_name = 'Descubrimiento Semanal'
client_id = 'Your Client Id' #insert your client id, you can find it in spotify for developers... sadly the site isn't working at the time i made this
sp = spotipy.Spotify(auth_manager = SpotifyOAuth(scope=scope))

def create_new_playlist():
    new_playlist_name = f"{playlist_name} {today.strftime('%b%d')}-{sunday.strftime('%b%d')}"
    new_playlist = sp.user_playlist_create(user='mi user', name=new_playlist_name)

    results = sp.search(q = 'Descubirmiento Semanal', type = 'playlist')
    playlist_id = results['playlists']['items'][0]['id']

    tracks = sp.playlist_tracks(playlist_id)
    track_uris = [track['track']['uri'] for track in tracks['items']]
    sp.playlist_add_items(new_playlist['id'], track_uris)

def schedule_playlist_creation():

    create_new_playlist()
    schedule.every().monday.at('10:30').do(create_new_playlist)

    while True:
        schedule.run_pending()
        time.sleep(60)

schedule_playlist_creation()







