import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_audio_features(df: pd.DataFrame):
    """
    Safely plots a scatter plot for danceability vs energy,
    filtering missing values and handling exceptions.
    """
    # Check for required columns
    required_cols = ['danceability', 'energy']
    if not all(col in df.columns for col in required_cols):
        raise ValueError("Required columns not found in the dataset!")
        
    # Drop missing values
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
        
        # Save the plot
        plt.savefig('outputs/scatter_plot.png', bbox_inches='tight')
        plt.close()
        print("Plot successfully saved as 'outputs/scatter_plot.png'.")
        
    except Exception as e:
        print(f"An error occurred while plotting: {e}")
