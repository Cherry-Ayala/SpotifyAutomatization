import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_id ='no la tengo'
client_secret='no lo tengo'
redirect_uri='solo si uso client credentials flow'

client_credentials_manager = SpotifyClientCredentials (client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

playlist_name = 'Descubrimiento Semanal'
results = sp.search(q = 'Descubirmiento Semanal', type = 'playlist')
playlist_id = results['playlists']['items'][0]['id']

import datetime
new_playlist_name = f"{playlist_name} ({datetime.date.today()})"
new_playlist = sp.user_playlist_create(user='mi user', name=new_playlist_name)

tracks = sp.playlist_tracks(playlist_id)
track_uris = [track['track']['uri'] for track in tracks['items']]
sp.playlist_add_items(new_playlist['id'], track_uris)