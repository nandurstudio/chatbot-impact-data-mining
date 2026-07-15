import streamlit as st
import numpy as np

def render_overview_tab(df):
    st.subheader("Ringkasan Dataset & Proyek")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ### Latar Belakang Penelitian
        Penelitian ini mengeksplorasi bagaimana chatbot percakapan (conversational chatbots) memengaruhi pembelajaran elektronik mahasiswa universitas di Bulgaria. 
        Survei ini mengumpulkan tanggapan dari mahasiswa mengenai frekuensi penggunaan, kegunaan, kepercayaan, serta kondisi lingkungan saat berinteraksi dengan chatbot AI.
        
        Secara khusus, penelitian ini mengevaluasi seberapa baik chatbot ini mendukung pembelajaran di tingkat universitas, seperti dalam menyelesaikan masalah matematika. 
        Di antara chatbot yang diuji, ChatGPT Plus menunjukkan performa terbaik.
        
        ### Metrik Utama yang Diteliti:
        1. **Frekuensi Penggunaan (Use Frequency)**
        2. **Tingkat Kepercayaan (Trust Level)**
        3. **Kegunaan (Usefulness)**
        4. **Kondisi Lingkungan (Environmental Conditions)**
        5. **Skor Performa Chatbot (Chatbot Performance Score)**
        """)
        
    with col2:
        with st.container(border=True):
            st.markdown("### 👤 Identitas Mahasiswa")
            st.markdown("""
            * **Nama**: NANDANG DURYAT
            * **NIM**: 312310233
            * **Jurusan**: Teknik Informatika (I232A)
            * **Status**: Mahasiswa
            """)
        st.info("""
        💡 **Panduan Memulai:**
        Dataset otomatis dimuat dari direktori project. Anda juga bisa mengunggah file dataset baru (.csv) melalui menu di panel samping kiri.
        """)

    if df is not None:
        st.markdown('<div class="section-header">Metrik Statistik Singkat</div>', unsafe_allow_html=True)
        m1, m2, m3, m4 = st.columns(4)
        with m1:
            st.markdown(f'<div class="metric-card"><div class="metric-value">{df.shape[0]}</div><div class="metric-label">Jumlah Responden</div></div>', unsafe_allow_html=True)
        with m2:
            st.markdown(f'<div class="metric-card"><div class="metric-value">{df.shape[1]}</div><div class="metric-label">Jumlah Kolom/Metrik</div></div>', unsafe_allow_html=True)
        with m3:
            numeric_cols = len(df.select_dtypes(include=[np.number]).columns)
            st.markdown(f'<div class="metric-card"><div class="metric-value">{numeric_cols}</div><div class="metric-label">Kolom Numerik</div></div>', unsafe_allow_html=True)
        with m4:
            missing_vals = df.isnull().sum().sum()
            st.markdown(f'<div class="metric-card"><div class="metric-value">{missing_vals}</div><div class="metric-label">Data Kosong (Null)</div></div>', unsafe_allow_html=True)
