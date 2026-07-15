import streamlit as st
import pandas as pd
import numpy as np
import json
import os

def update_project_summary(filename, rows, cols):
    path = "project_summary.json"
    data = {}
    if os.path.exists(path):
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception:
            pass
    else:
        data = {
            "project_name": "Evaluasi Dampak 21 Chatbots pada Pembelajaran Mahasiswa",
            "preprocessing_steps": [
                "Pembersihan string kosong (fillna)",
                "Konversi tipe data Timestamp ke Datetime",
                "Ekstraksi panjang karakter dari respon teks kualitatif"
            ],
            "model_used": [
                {
                  "name": "Latent Dirichlet Allocation (LDA)",
                  "library": "scikit-learn"
                },
                {
                  "name": "Sentiment Polarity Analyzer",
                  "library": "TextBlob"
                }
            ],
            "evaluation_metrics": {
                "topic_modeling": "Ekstraksi 5 klaster topik menggunakan CountVectorizer & LDA",
                "sentiment_analysis": "Skor polaritas rata-rata (-1.0 s.d 1.0) untuk mendeteksi emosi responden"
            },
            "streamlit_features": [
                "File Uploader dinamis untuk konfigurasi csv",
                "Preview Data Tabular & Analisis tipe data kolom",
                "Grafik EDA Interaktif (Heatmap, Stacked Bar, dan Histogram)",
                "Visualisasi NLP (Sentiment Histogram, Word Cloud, dan Topic Word Weights)",
                "Interactive Playground untuk simulasi logika 21 Chatbot"
            ]
        }

    if "dataset_info" not in data:
        data["dataset_info"] = {}
    
    data["dataset_info"]["filename"] = filename
    data["dataset_info"]["total_rows"] = int(rows)
    data["dataset_info"]["total_columns"] = int(cols)
    data["dataset_info"]["target_variable"] = "Q5.1 (Attitude toward AI) / Q10 (Qualitative Response)"

    try:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
    except Exception:
        pass

@st.cache_data
def load_data(file_obj, delim, enc):
    # Determine filename
    filename = "Uploaded File"
    if isinstance(file_obj, str):
        filename = os.path.basename(file_obj)
    elif hasattr(file_obj, "name"):
        filename = file_obj.name
        
    df = pd.read_csv(file_obj, delimiter=delim, encoding=enc, encoding_errors='replace')
    if 'Timestamp' in df.columns:
        df['Timestamp'] = pd.to_datetime(df['Timestamp'], errors='coerce')
        
    # Automatically update the summary metrics
    update_project_summary(filename, df.shape[0], df.shape[1])
    return df
