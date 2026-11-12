import pandas as pd

def clean_audio_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Spotify veri setindeki eksik değerleri temizler ve sayısal sütunların 
    tiplerini doğru formata dönüştürür.
    """
    # 1. Eksik değerleri temizle (Örn: danceability, energy vb. boş olan satırları at veya doldur)
    numeric_cols = ['danceability', 'energy', 'tempo', 'valence']
    
    # Sütunların varlığını kontrol ederek veri setini temizle
    existing_cols = [col for col in numeric_cols if col in df.columns]
    
    if existing_cols:
        # Boş değer içeren satırları filtrele veya uygun bir değerle doldur
        df = df.dropna(subset=existing_cols)
        
        # Sayısal sütunların tiplerini float'a dönüştürerek tip çakışmalarını önle
        for col in existing_cols:
            df[col] = df[col].astype(float)
            
    return df
