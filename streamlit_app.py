import streamlit as st
import pandas as pd

# URL dataset di GitHub (ganti dengan link dataset Anda)
DATA_URL = 'https://raw.githubusercontent.com/kuta-ndze/PriceOptimization/refs/heads/main/Cafe%2B-%2BDateInfo.csv'

def load_data():
    return pd.read_csv(DATA_URL)

# Memuat dataset
st.title('Visualisasi Dataset dari GitHub')
data = load_data()

# Menampilkan data dalam bentuk tabel
st.write('Dataframe:')
st.dataframe(data.head())

# Memilih kolom untuk ditampilkan
columns = data.columns
selected_columns = st.multiselect('Pilih 5 kolom untuk divisualisasikan:', columns, default=columns[:5])

if len(selected_columns):
    st.write(f'Visualisasi 5 Kolom: {selected_columns}')

    # Membuat grafik untuk tiap kolom yang dipilih
    for col in selected_columns:
        st.write(f'Grafik Kolom: {col}')
        st.line_chart(data[col])

else:
    st.warning("Silakan pilih tepat 5 kolom untuk divisualisasikan.")
