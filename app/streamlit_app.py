import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# --- Streamlit page setup ---
st.set_page_config(page_title='Spotify Audio Explorer', layout='wide')
st.title('Spotify Audio Feature Explorer')

# --- Data path ---
DATA_PATH = (
    os.path.join('..', 'data', 'tracks.csv')
    if os.path.exists(os.path.join('..', 'data', 'tracks.csv'))
    else os.path.join('data', 'tracks.csv')
)

# --- Data loading ---
@st.cache_data
def load_data(path=DATA_PATH):
    if os.path.exists(path):
        return pd.read_csv(path)
    else:
        st.error('tracks.csv not found in data/. Please provide a dataset.')
        return None

df = load_data()
if df is None:
    st.stop()

# --- Sidebar options ---
st.sidebar.header('Options')
n_samples = st.sidebar.slider(
    'Sample size (for plotting)', min_value=500, max_value=5000, value=2000, step=500
)

features = [
    'danceability', 'energy', 'tempo', 'valence', 'acousticness', 'instrumentalness'
]
for f in features:
    if f not in df.columns:
        st.error(f'Missing expected column: {f}')
        st.stop()

# --- Sampling & EDA ---
sample = df.sample(n=min(n_samples, len(df)), random_state=42)
st.subheader('Feature distributions (sample)')
st.write(sample[features].describe().T)

st.subheader('Scatter: energy vs danceability (colored by popularity)')
st.scatter_chart(
    sample[['energy', 'danceability', 'popularity']].rename(columns={'popularity': 'size'})
)

# --- PCA & Clustering ---
st.subheader('PCA projection (2 components) with KMeans clusters')
X = sample[features].fillna(0)
scaler = StandardScaler()
Xs = scaler.fit_transform(X)
pca = PCA(n_components=2, random_state=42)
proj = pca.fit_transform(Xs)

if st.sidebar.checkbox('Run KMeans clustering', value=True):
    from sklearn.cluster import KMeans

    k = st.sidebar.slider('K (clusters)', 2, 8, 4)
    kmeans = KMeans(n_clusters=k, random_state=42).fit(Xs)
    labels = kmeans.labels_

    df_proj = pd.DataFrame(proj, columns=['pc1', 'pc2'])
    df_proj['cluster'] = labels

    st.write('Cluster means:')
    st.write(df_proj.groupby('cluster').mean())

    # --- Plotly scatter plot ---
    import plotly.express as px

    fig = px.scatter(
        df_proj,
        x='pc1',
        y='pc2',
        color='cluster',
        title='KMeans Clustering (PCA Projection)',
        hover_data=['cluster']
    )
    st.plotly_chart(fig, use_container_width=True)

    st.write('Clusters preview (first 50 points):')
    st.dataframe(df_proj.head(50))

else:
    st.write('Clustering disabled.')
