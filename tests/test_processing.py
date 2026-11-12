import pandas as pd
import pytest
from src.processing import clean_audio_data

def test_clean_audio_data():
    # Test için örnek ham veri oluşturalım
    raw_data = pd.DataFrame({
        'track_name': ['Song 1', 'Song 2', None],
        'danceability': [0.8, None, 0.5],
        'energy': [0.6, 0.7, 0.9],
        'tempo': [120.0, 110.0, 130.0],
        'valence': [0.5, 0.4, 0.3]
    })
    
    cleaned = clean_audio_data(raw_data)
    
    # Beklenen: Boş değerli (NaN) satırların temizlenmiş olması
    # 2. satırda 'danceability' None olduğu için filtrelenmeli, geriye 2 satır kalmalı
    assert len(cleaned) == 2
    assert cleaned['track_name'].iloc[0] == 'Song 1'
    assert cleaned['track_name'].iloc[1] == 'Song 3'
