# 🤖 Evaluasi Dampak 21 Chatbots pada Pembelajaran Mahasiswa

Proyek Akhir Praktikum Data Mining 2026 — Universitas Pelita Bangsa.

### 👤 Identitas Mahasiswa
* **Nama**: NANDANG DURYAT
* **NIM**: 312310233
* **Jurusan**: Teknik Informatika (Kelas I232A)
* **Peran**: Mahasiswa
* **Repository GitHub**: [nandurstudio/chatbot-impact-data-mining](https://github.com/nandurstudio/chatbot-impact-data-mining)
* **Link Streamlit (Go-Live)**: [chatbot-impact.streamlit.app](https://chatbot-impact.streamlit.app/)

Aplikasi ini merupakan dashboard interaktif berbasis **Streamlit** untuk mengevaluasi dampak penggunaan chatbot percakapan (*conversational chatbots*) terhadap proses pembelajaran mahasiswa universitas.

Dataset yang dianalisis didasarkan pada penelitian Jocelyn C. Dumlao (2024), *"21 Chatbots: Evaluating Their Impact on University Learning"*, dengan sampel data survei 131 responden mahasiswa di Bulgaria.

---

## 🚀 Fitur Utama Dashboard

1. **Overview & Ringkasan**: Ringkasan latar belakang riset, tujuan survei, dan metrik statistik cepat (total baris data, kolom numerik, data kosong).
2. **Preview Data Tabular**: Tabel pratinjau data interaktif dengan slider kontrol baris serta tabel detail skema tipe data kolom.
3. **Analisis Visual (EDA)**:
   * **Response Count Heatmap**: Visualisasi korelasi jenjang pendidikan (Q1) vs frekuensi penggunaan chatbot (Q4).
   * **Distribusi Agreement Levels (Q5.1 - Q5.5)**: Stacked bar chart frekuensi kesetujuan responden.
   * **Karakter Respon**: Histogram analisis panjang karakter jawaban teks mahasiswa.
4. **NLP & Topic Modeling**:
   * **Sentiment Distribution**: Analisis polaritas sentimen respon teks menggunakan library `TextBlob`.
   * **Word Cloud**: Visualisasi kata kunci yang paling sering muncul dari respon kualitatif responden.
   * **LDA Topic Modeling**: Klasterisasi jawaban teks menjadi 5 topik utama menggunakan algoritma *Latent Dirichlet Allocation*.
5. **Interactive Chatbots (21 Playgrounds)**: 
   * Simulasi 21 tipe logika chatbot yang terintegrasi langsung dalam GUI Streamlit (user dapat berinteraksi langsung dan menerima output dalam speech bubble).

---

## 🛠️ Struktur Project

```text
chatbot-impact-data-mining/
├── app.py                     # Main orchestrator & routing tab Streamlit
├── requirements.txt           # File dependensi pustaka Python
├── .gitignore                 # Daftar file/folder yang diabaikan Git
├── README.md                  # Dokumentasi proyek & identitas di GitHub
├── project_summary.json       # Log metrik teknis proyek (auto-generated)
├── final_report_2026.html     # Draf laporan utama proyek
├── final_audit_report_2026.html # Dokumen audit kepatuhan & kelengkapan proyek
├── AI_Chatbots_Students_Attitude_Dataset_EN.csv  # Dataset utama survei
├── POSTER Praktikum Nandang Duryat I232A Data Mining.png # Poster final proyek
├── utils/
│   └── data_loader.py         # Utility untuk memproses file CSV & DateTime
├── components/
│   ├── styles.py              # Injeksi CSS & styling visual (Dark/Light mode)
│   └── chatbot_logic.py       # Kumpulan logika respon 21 chatbot
└── tabs/
    ├── overview.py            # Render Tab Overview & Identitas Mahasiswa
    ├── preview.py             # Render Tab Preview Data Tabular & Skema Kolom
    ├── eda.py                 # Render Tab Grafik Visualisasi EDA
    ├── nlp.py                 # Render Tab Analisis Sentimen & Topic Modeling LDA
    └── chatbots.py            # Render Tab Playground Interaksi 21 Chatbot
```

---

## 💻 Cara Menjalankan Secara Lokal

### Prasyarat
Pastikan Anda sudah menginstal **Python 3.10+** di komputer Anda.

### Langkah-langkah
1. **Clone repository ini** (setelah diunggah ke GitHub):
   ```bash
   git clone https://github.com/username/repo-name.git
   cd repo-name
   ```
2. **Instal seluruh pustaka dependensi**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Jalankan server aplikasi Streamlit**:
   ```bash
   streamlit run app.py
   ```
4. **Akses Dashboard** di web browser Anda:
   👉 **`http://localhost:8501`** atau **`http://127.0.0.1:8501`**
