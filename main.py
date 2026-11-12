import pandas as pd
import os
from src.processing import clean_audio_data
from src.visualization import plot_audio_features

def main():
    print("Initializing Spotify Audio Explorer...")
    
    # Create outputs directory if it doesn't exist
    os.makedirs('outputs', exist_ok=True)
    
    # Sample dataset
    data = {
        'track_name': ['Track A', 'Track B', 'Track C', 'Track D'],
        'danceability': [0.75, 0.82, 0.45, 0.60],
        'energy': [0.80, 0.65, 0.30, 0.50],
        'tempo': [125.5, 118.2, 95.0, 110.0],
        'valence': [0.6, 0.7, 0.2, 0.5]
    }
    
    df = pd.DataFrame(data)
    
    # 1. Clean and process data
    print("Cleaning data and handling type conversions...")
    cleaned_df = clean_audio_data(df)
    
    # 2. Safely visualize
    print("Generating visualization...")
    plot_audio_features(cleaned_df)
    
    print("Process completed successfully!")

if __name__ == "__main__":
    main()
