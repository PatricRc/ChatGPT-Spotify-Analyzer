# AI Music Analyzer: Spotify Insights with GPT

[![MIT License](https://img.shields.io/badge/License-MIT-blue.svg)](https://choosealicense.com/licenses/mit/)
[![Python Version](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

![Project Banner](https://github.com/PatricRc/ChatGPT-Spotify-Analyzer/assets/85771918/3bb43c8c-bb3e-41c3-9ba9-516b35adb995)

**Dive deep into your Spotify listening habits and get AI-powered personality insights and song recommendations!**

This project leverages the Spotify Web API to extract detailed information about your saved tracks (or any playlist) and uses the OpenAI API (GPT-3.5/GPT-4) to generate a personalized analysis of your music taste and suggest new songs you might love.

## 📚 Table of Contents

*   [Overview](#-overview)
*   [Features](#-features)
*   [Tech Stack](#-tech-stack)
*   [Getting Started](#-getting-started)
    *   [Prerequisites](#prerequisites)
    *   [Installation](#installation-)
    *   [Configuration](#configuration-)
*   [Usage](#-usage)
*   [Project Visualization](#-project-visualization)
*   [Contributing](#-contributing)
*   [License](#-license)
*   [Acknowledgments](#-acknowledgments)

## 📗 Overview

AI Music Analyzer connects to your Spotify account, fetches data about your music preferences (like saved tracks or specific playlists), analyzes various attributes including track details, artist information, and audio features (like danceability, energy, valence), and then passes this data to an AI model (OpenAI's GPT) to:

1.  Generate a descriptive analysis of the musical profile.
2.  Infer personality traits based on listening patterns.
3.  Recommend new songs tailored to the analyzed genres and features.

It's a fun tool for music lovers curious about their habits and data enthusiasts exploring API integrations and AI applications.

## ✨ Features

*   **Detailed Spotify Data Extraction:** Gathers comprehensive data including track name, artist, album, release date, duration, popularity, explicitness, genres, and audio features.
*   **AI-Powered Analysis:** Utilizes OpenAI's GPT models to interpret music data and generate insightful text.
*   **Personality Insights:** Offers a unique perspective on how music taste might reflect personality traits.
*   **Personalized Recommendations:** Suggests new tracks based on the analysis of existing playlists or saved songs.
*   **Environment Variable Management:** Securely handles API keys using `.env` files.
*   **Easy to Run:** Simple Python script execution.

## 🛠️ Tech Stack

*   **Language:** Python 3.7+
*   **APIs:**
    *   Spotify Web API (via `spotipy`)
    *   OpenAI API (via `openai`)
*   **Data Handling:** `pandas`
*   **Environment Variables:** `python-dotenv`

## 🚀 Getting Started

Follow these steps to set up and run the project locally.

### Prerequisites

*   Python 3.7 or later
*   Git
*   A Spotify account (Premium not required, but needed for some features)
*   An OpenAI API key

### Installation 🔧

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/PatricRc/ChatGPT-Spotify-Analyzer.git
    cd ChatGPT-Spotify-Analyzer
    ```

2.  **Set up a virtual environment (Recommended):**
    *   On macOS/Linux:
        ```bash
        python3 -m venv env
        source env/bin/activate
        ```
    *   On Windows:
        ```powershell
        python -m venv env
        .\env\Scripts\activate
        ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *(If `requirements.txt` doesn't exist, you might need to create one based on the imports in `Main_code.py`: `pip install spotipy pandas python-dotenv openai`)*

### Configuration 🔑

1.  **Spotify API Credentials:**
    *   Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/).
    *   Create an App. Note the `Client ID` and `Client Secret`.
    *   Edit the settings for your app and add a `Redirect URI`. For local development, `http://localhost:8888/callback` is common. Make sure this matches the `redirect_uri` in your code or environment variables.

2.  **OpenAI API Key:**
    *   Get your API key from the [OpenAI Platform](https://platform.openai.com/account/api-keys).

3.  **Create `.env` file:**
    *   In the root directory of the project, create a file named `.env`.
    *   Add your credentials like this:
        ```dotenv
        SPOTIFY_CLIENT_ID='YOUR_SPOTIFY_CLIENT_ID'
        SPOTIFY_CLIENT_SECRET='YOUR_SPOTIFY_CLIENT_SECRET'
        SPOTIFY_REDIRECT_URI='YOUR_SPOTIFY_REDIRECT_URI'
        OPENAI_KEY='YOUR_OPENAI_API_KEY'
        ```
    *   Replace the placeholder values with your actual credentials.

## ✍️ Usage

1.  Ensure your virtual environment is activated.
2.  Make sure your `.env` file is correctly configured in the project root.
3.  Run the main script:
    ```bash
    python Main_code.py
    ```
4.  The script will:
    *   Authenticate with Spotify (you might need to authorize it in your browser the first time).
    *   Fetch your saved tracks (up to the limit set in the script, currently 50).
    *   Process the data and create a DataFrame.
    *   Send the DataFrame to OpenAI's API using a predefined prompt.
    *   Print the AI-generated analysis and song recommendations to the console.

*   **Customization:** You can modify the `prompt` variable within `Main_code.py` to change the type of analysis or recommendations requested from the AI. You can also adjust the `limit` in `sp.current_user_saved_tracks(limit=50)` to fetch more songs (up to Spotify's API limits).
*   **Jupyter Notebook:** For a more interactive exploration, check out the `SpotifyAPI_ChatGPT.ipynb` notebook which includes steps for analyzing different playlists and manual authentication examples.

## 🖼️ Project Visualization

Here's a glimpse of the data analysis process:
![Screenshot of code or data analysis](https://github.com/PatricRc/ChatGPT-Spotify-Analyzer/assets/85771918/d8796b1c-b56b-44d1-8f32-2a7193447729)
*(Consider adding a screenshot of the terminal output showing the AI analysis)*

## 🤝 Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to:

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

Please ensure your code adheres to good practices and includes relevant documentation.

## 📜 License

Distributed under the MIT License. See `LICENSE` file for more information.

## 🙏 Acknowledgments

*   [Spotify Web API](https://developer.spotify.com/documentation/web-api/)
*   [OpenAI API](https://platform.openai.com/docs)
*   [Spotipy Documentation](https://spotipy.readthedocs.io/)
*   Readme template inspiration ([othneildrew/Best-README-Template](https://github.com/othneildrew/Best-README-Template))


