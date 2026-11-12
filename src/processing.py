import pandas as pd
from src.processing import clean_audio_data

def test_clean_audio_data():
    
    raw_data = pd.DataFrame({
        'track_name': ['Song A', None],
        'danceability': [0.8, None],
        'energy': [0.6, 0.5]
    })

    cleaned = clean_audio_data(raw_data)

    
    assert len(cleaned) == 1
    assert cleaned['track_name'].iloc[0] == 'Song A'
