# shows acoustic features for tracks for the given artist

# import spotipy
# import spotipy.util as util
# from config import CLIENT_ID, CLIENT_SECRET, PLAYLIST, USER
#
# token = util.oauth2.SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
#
# cache_token = token.get_access_token()
# spotify = spotipy.Spotify(cache_token)
#
# results = spotify.user_playlist_tracks(USER, PLAYLIST, limit=100, offset=0)
import csv
import spotipy
import spotipy.util as util
from unidecode import unidecode
from config import CLIENT_ID, CLIENT_SECRET, PLAYLISTS, USER


def get_playlist_tracks(username, playlist_id):
    results = spotify.user_playlist_tracks(username, playlist_id)
    tracks = results['items']
    while results['next']:
        results = spotify.next(results)
        tracks.extend(results['items'])
    return tracks


token = util.oauth2.SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)

cache_token = token.get_access_token()
print("Connecting. . .")
spotify = spotipy.Spotify(cache_token)
print("Connected.")
for playlist in PLAYLISTS:
    print("Analyzing {}".format(playlist))
    results = get_playlist_tracks(USER, playlist)
    playlist_name = spotify.user_playlist(user=None, playlist_id=playlist, fields="name")
    playlist_name = playlist_name["name"]
    for item in results:
        print("Gather data for track :: {}".format(item['track']['name']))
        track = item['track']
        id = track['id']
        name = track['name']
        name = unidecode(name)
        name = bytes(name, 'utf-8').decode('utf-8', 'ignore')
        name = unidecode(name)
        songArtist = track['artists']
        artists = ''
        for blank in songArtist:
            artists = blank['name']
        features = spotify.audio_features(id)
        danceability = 0.0
        energy = 0.0
        key = 0.0
        loudness = 0.0
        mode = 0.0
        speechiness = 0.0
        acousticness = 0.0
        instrumentalness = 0.0
        liveness = 0.0
        valence = 0.0
        tempo = 0.0
        duration_ms = 0.0
        time_signature = 0.0
        for feature in features:
            danceability = feature['danceability']
            energy = feature['energy']
            key = feature['key']
            loudness = feature['loudness']
            mode = feature['mode']
            speechiness = feature['speechiness']
            acousticness = feature['acousticness']
            instrumentalness = feature['instrumentalness']
            liveness = feature['liveness']
            valence = feature['valence']
            tempo = feature['tempo']
            duration_ms = feature['duration_ms']
            time_signature = feature['time_signature']

        myData = [id, name, artists, danceability, energy, key, loudness, mode, speechiness, acousticness,
                  instrumentalness, liveness, valence, tempo, duration_ms, time_signature, playlist_name]
        myFile = open('tracks.csv', 'a', newline='')
        with open('tracks.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(myData)
