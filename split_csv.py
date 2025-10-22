import pandas as pd
import os

# CSV dosyasını oku
print("CSV dosyası okunuyor...")
df = pd.read_csv('data/tracks.csv')

print(f"Toplam satır sayısı: {len(df)}")

# 4 eşit parçaya böl (her biri ~25-30 MB olur)
num_parts = 4
part_size = len(df) // num_parts

for i in range(num_parts):
    start_idx = i * part_size
    if i == num_parts - 1:  # Son parça
        end_idx = len(df)
    else:
        end_idx = (i + 1) * part_size
    
    part_df = df.iloc[start_idx:end_idx]
    filename = f'data/tracks_part_{i+1}.csv'
    part_df.to_csv(filename, index=False)
    print(f"{filename} kaydedildi - {len(part_df)} satır")

print("Dosya bölme işlemi tamamlandı!")