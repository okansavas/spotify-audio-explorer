import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_audio_features(df: pd.DataFrame):
    """
    Danceability ve Energy değerleri arasında güvenli bir scatter plot çizer,
    eksik verileri ve hataları filtreler.
    """
    # Eksik veri kontrolü
    required_cols = ['danceability', 'energy']
    if not all(col in df.columns for col in required_cols):
        raise ValueError("Gerekli sütunlar veri setinde bulunamadı!")
        
    # Boş değerleri temizle
    clean_df = df.dropna(subset=required_cols)
    
    try:
        plt.figure(figsize=(8, 6))
        sns.scatterplot(
            data=clean_df, 
            x='danceability', 
            y='energy', 
            alpha=0.7, 
            color='purple'
        )
        plt.title('Spotify Tracks: Danceability vs Energy')
        plt.xlabel('Danceability')
        plt.ylabel('Energy')
        plt.grid(True, linestyle='--', alpha=0.5)
        
        # Grafiği kaydet
        plt.savefig('outputs/scatter_plot.png', bbox_inches='tight')
        plt.close()
        print("Grafik başarıyla 'outputs/scatter_plot.png' olarak kaydedildi.")
        
    except Exception as e:
        print(f"Grafik çizilirken bir hata oluştu: {e}")
