# Spotify Audio Feature Analysis

This project analyzes Spotify audio features to discover trends in danceability, energy, tempo, and other characteristics of popular tracks.
It includes EDA, clustering, a simple classification baseline for predicting track popularity, and a Streamlit explorer app.

## Contents
- `notebooks/Spotify_audio_features_analysis.ipynb` : Jupyter Notebook with EDA, clustering (KMeans), PCA, and a RandomForest classifier baseline.
- `app/streamlit_app.py` : Lightweight Streamlit app to explore features and view cluster labels.
- `requirements.txt` : Python dependencies.
- `data/` : Place your `tracks.csv` here if automatic download fails.

## Data
The notebook tries to download a public CSV of Spotify audio features. If the automatic download fails, place a CSV file named `tracks.csv` in the `data/` folder. Expected columns include: `danceability, energy, key, loudness, mode, speechiness, acousticness, instrumentalness, liveness, valence, tempo, duration_ms, popularity`, and track identifiers like `name`, `artists`.

## How to run
1. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the notebook:
   ```bash
   jupyter notebook notebooks/Spotify_audio_features_analysis.ipynb
   ```
3. (Optional) Run the Streamlit app:
   ```bash
   streamlit run app/streamlit_app.py
   ```

## Notes
- The notebook includes example code to perform PCA and KMeans clustering, plus a baseline model to predict whether a track is 'popular' (e.g., popularity >= 70).
- No Spotify API key is required for this project if you use a CSV dataset.
