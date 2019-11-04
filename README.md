# spotify-audio-feature-scraper
 
This script will gather [audio features from a Spotify track](https://developer.spotify.com/documentation/web-api/reference/tracks/get-audio-features/) from a Spotify playlist and make a .csv with them.  Audio features are information Spotify assigns to a track that attempt to categorize whether a track is happy or sad (valence), danceable (danceability), or spoken work (speechiness) among other features. 

## To Run

 1. Download this repo.
 2. Input variables and playlists into config.py. [You will need a Spotify API Key.](https://developer.spotify.com/documentation/web-api/quick-start/) Other fields can be field out based on the [Spotipy authentication docs.](https://spotipy.readthedocs.io/en/latest/)
 3. Run the main method. 
 4. The resulting .csv can be found in the root folder.

This project was for a UIowa Master's Course Project and will likely not be updated further, but feel free to contact me with any questions.. The final report for this project was a video [that can be found on YouTube.](https://youtu.be/VGbeRD5uLYc)
