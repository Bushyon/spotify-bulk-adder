import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Set up authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="YOUR_CLIENT_ID", 
    client_secret="YOUR_CLIENT_SECRET", 
    redirect_uri="http://localhost:8080/callback", 
    scope="playlist-modify-private"))
# Create a new playlist
# playlist_name = "My New Playlist"
# sp.user_playlist_create(user="YOUR_USERNAME", name=playlist_name, public=False)

# Find the URIs of the songs you want to add
# List of song names
song_names = [
    "Song 1",
    "Song 2",
    "Song 3",
    "Song 4"
]

# Initialize a list of song IDs
song_ids = []

# Search and get the IDs of the songs
for song_name in song_names:
    results = sp.search(q=song_name, type='track', limit=1)
    if results['tracks']['items']:
        song_ids.append(results['tracks']['items'][0]['uri'])

# Add the songs to the playlist
playlist_id = "PUBLIC_PLAYLIST_ID"  # Replace with the ID of your playlist. Example value in brackets: https://open.spotify.com/playlist/[xxxxxxxxxxxxxxxx]?si=xxxxxxxxxxxxxxx
sp.playlist_add_items(playlist_id, song_ids)

# Print the IDs of the added songs
print("IDs of the added songs:")
for song_id in song_ids:
    print(song_id)
