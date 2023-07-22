![ChatGPT-Spotify-Analyzer](https://github.com/PatricRc/ChatGPT-Spotify-Analyzer/assets/85771918/3bb43c8c-bb3e-41c3-9ba9-516b35adb995)


# ChatGPT-Spotify-Analyzer
Enhance your Spotify experience with AI-Music-Analyzer. Dive into detailed playlist analysis using Spotify's API and OpenAI's GPT-3. Ideal for music lovers, data enthusiasts, and tech explorers!

## Overview 📗

This project allows users to input their Spotify playlist and receive back a detailed dataframe that includes data points such as track name, artist, album, release date, popularity, explicitness, genre, and more. Additionally, the project uses OpenAI's GPT-3 model to provide song recommendations based on the genres in the user's playlist.

## Features ✨

- Detailed analysis of Spotify playlists including track info, artist info, and audio features.
- Integration with OpenAI's GPT-3 model for song recommendations.
- Fun and professional tone for engaging interactions.

## How to Use ✍️

To use AI Music Analyzer, you need to have a Spotify account and a playlist you want to analyze. You also need to set up your Spotify API credentials and your OpenAI API key in your local environment.

## Installation 🔧

Please follow the instructions in the [Installation Guide](INSTALLATION.md) to set up and run AI Music Analyzer on your machine.

## Future Plans 🚀

We plan to continually update AI Music Analyzer with new features and improvements. If you have any suggestions or feedback, please feel free to open an issue or submit a pull request.

## License 📜

AI Music Analyzer is licensed under the [MIT License](LICENSE).
# Installation Guide

This guide will walk you through the steps to install and run the Spotify Data Analysis project on your local machine.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- You have a recent version of Python installed (3.7 or later is recommended).
- You have a basic understanding of how to use the command line on your computer.

## Installation Steps

1. **Clone the repository**

   Open your terminal and use `git` to clone the repository. Replace `your-username` and `your-repository` with your GitHub username and the name of your repository:

   ```bash
   git clone https://github.com/your-username/your-repository.git

Navigate into the cloned repository:

    cd your-repository

2. **Set up a virtual environment (optional but recommended)**

   It's often a good idea to create a virtual environment for your Python projects to isolate the dependencies for each project. You can create a virtual environment using the venv module that comes with Python:

   ```bash
   python3 -m venv env

And then activate the virtual environment. On macOS and Linux:
    
    source env/bin/activate

On Windows:
    
    .\env\Scripts\activate

3. **Install the required packages**

    The project comes with a requirements.txt file that lists all the Python packages that the project depends on. You can install all these packages using pip:

     ```bash
   pip install -r requirements.txt

4. **Set up your Spotify API credentials**

    You will need to create an application on the Spotify Developer Dashboard to get the client_id, client_secret, and redirect_uri that the project needs. Once you have these, add them to a .env file in the root directory of the project:

    ```bash
    SPOTIPY_CLIENT_ID='your-spotify-client-id'
    SPOTIPY_CLIENT_SECRET='your-spotify-client-secret'
    SPOTIPY_REDIRECT_URI='your-spotify-redirect-uri'

Replace 'your-spotify-client-id', 'your-spotify-client-secret', and 'your-spotify-redirect-uri' with your actual Spotify API credentials.

5.**Run the project**

You can now run the project:

    python main.py


## API Reference

### Spotify API

#### Get a Playlist

```http
  GET /v1/playlists/{playlist_id}
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `playlist_id` | `string` | **Required**. Required. The Spotify ID for the playlist. |
| `market` | `string` | An ISO 3166-1 alpha-2 country code. Optional. |

#### Get a Track

```http
    GET /v1/tracks/{id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. The Spotify ID for the track. |

### OpenAI GPT-3 API
#### Create a Chat Completion

```http
    POST /v1/engines/davinci-codex/completions
```
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `message` | `array` | **Required**. Array of message objects. |
| `model` | `string` | The ID of the model to use. |
| `max_tokens` | `integer` | TThe maximum length of the generated content. |

#### Each message object in the messages array has role and content properties:

{
  "role": "system",
  "content": "You are a helpful assistant."
},
{
  "role": "user",
  "content": "Who won the world series in 2020?"
}

Please note that these API references are quite simplified. The actual Spotify and OpenAI APIs have many more endpoints and options. Be sure to check out the full API documentation on their official websites for more details:

- Spotify Web API Reference (https://developer.spotify.com/documentation/web-api)
- OpenAI API Reference (https://platform.openai.com/docs/api-reference/introduction/)

## Project Image

![Captura de pantalla 2023-07-22 120817](https://github.com/PatricRc/ChatGPT-Spotify-Analyzer/assets/85771918/d8796b1c-b56b-44d1-8f32-2a7193447729)



## Badges


[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)



