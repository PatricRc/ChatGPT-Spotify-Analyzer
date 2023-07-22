# Importing required libraries
import os
import spotipy
import pandas as pd
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv, find_dotenv
import openai

# Load environment variables
_ = load_dotenv(find_dotenv()) 

# Spotify API credentials
client_id = os.getenv('SPOTIFY_CLIENT_ID')
client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')
redirect_uri = os.getenv('SPOTIFY_REDIRECT_URI')

# OpenAI GPT-3 credentials
openai.api_key  = os.getenv('OPENAI_KEY')

# Spotify authorization scope
scope = 'user-library-read'

# Spotify user authorization
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, 
                                               client_id=client_id, 
                                               client_secret=client_secret, 
                                               redirect_uri=redirect_uri))

# Get user's liked songs
results = sp.current_user_saved_tracks(limit=50)

# Prepare empty lists where we will store our data
track_list = []
artist_list = []
album_list = []
release_date_list = []
duration_list = []
popularity_list = []
explicit_list = []
genre_list = []
artist_popularity_list = []
album_type_list = []
track_id_list = []
artist_id_list = []
album_id_list = []
danceability_list = []
energy_list = []
valence_list = []

# Iterate over liked songs and extract data
for item in results['items']:
    track = item['track']
    track_list.append(track['name'])
    artist_list.append(track['artists'][0]['name'])
    album_list.append(track['album']['name'])
    release_date_list.append(track['album']['release_date'])
    duration_list.append(track['duration_ms'] / 60000)  # Convert duration from ms to min
    popularity_list.append(track['popularity'])
    explicit_list.append(track['explicit'])
    track_id_list.append(track['id'])
    artist_id_list.append(track['artists'][0]['id'])
    album_id_list.append(track['album']['id'])
    album_type_list.append(track['album']['album_type'])

    # Get the artist object for the first artist of the track
    artist = sp.artist(track['artists'][0]['id'])
    artist_popularity_list.append(artist['popularity'])
    
    # Add the genres of the artist
    genre_list.append(artist['genres'])

    # Get the audio features object for the track
    audio_features = sp.audio_features(track['id'])[0]
    danceability_list.append(audio_features['danceability'])
    energy_list.append(audio_features['energy'])
    valence_list.append(audio_features['valence'])

# Convert the lists into a Pandas DataFrame
df = pd.DataFrame({
    'track': track_list,
    'artist': artist_list,
    'album': album_list,
    'release_date': release_date_list,
    'duration (min)': duration_list,
    'popularity': popularity_list,
    'explicit': explicit_list,
    'genre': genre_list,
    'artist_popularity': artist_popularity_list,
    'album_type': album_type_list,
    'track_id': track_id_list,
    'artist_id': artist_id_list,
    'album_id': album_id_list,
    'danceability': danceability_list,
    'energy': energy_list,
    'valence': valence_list
})

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0.8,
    )
    return response.choices[0].message["content"]

# This is an example of how to define the prompt.
# Replace with your own prompt to have a custom conversation with ChatGPT.

prompt = f"""
Act as a song analyst expert/
Your task is to help me give a complete description of a user spotify dataset/
Describe the personality of the user based on the dataset/
Output 500 words of your analysis and also recommend 10 songs based on the genre of the dataset/
The dataset you will use for the analysis is in triple backticks/
Spotify dataset: ```{df.to_string()}```
"""

# Note: You can replace the above prompt with any conversation starter or question you want to ask GPT-3
response = get_completion(prompt)
print(response)
