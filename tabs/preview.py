import streamlit as st
import pandas as pd

def render_preview_tab(df):
    st.subheader("Preview Data Tabular")
    
    if df is not None:
        st.markdown('<div class="section-header">Tabel Data Utama</div>', unsafe_allow_html=True)
        rows_to_show = st.slider("Pilih jumlah baris yang ingin ditampilkan", min_value=5, max_value=100, value=10, step=5)
        st.dataframe(df.head(rows_to_show), use_container_width=True)
        
        st.markdown('<div class="section-header">Struktur & Tipe Data Kolom</div>', unsafe_allow_html=True)
        schema_df = pd.DataFrame({
            "Tipe Data": df.dtypes.astype(str),
            "Jumlah Nilai Non-Null": df.notnull().sum().values,
            "Jumlah Nilai Kosong (Null)": df.isnull().sum().values,
            "Sample Nilai Pertama": [str(x) for x in df.iloc[0].values]
        }).set_index(df.columns)
        
        st.dataframe(schema_df, use_container_width=True)
    else:
        st.warning("⚠️ Silakan unggah dataset (.csv) terlebih dahulu di sidebar untuk melihat preview data.")
