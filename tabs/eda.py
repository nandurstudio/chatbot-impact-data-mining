import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def render_eda_tab(df):
    st.subheader("Eksplorasi Data Singkat (EDA)")
    
    if df is not None:
        st.markdown('<div class="section-header">Grafik Hasil Eksplorasi Data</div>', unsafe_allow_html=True)
        
        # 1. Heatmap
        st.subheader("1. Response Count Heatmap: Education Level (Q1) vs Frequency (Q4)")
        if 'Q1' in df.columns and 'Q4' in df.columns:
            fig, ax = plt.subplots(figsize=(10, 4))
            val_col = 'Q5.1' if 'Q5.1' in df.columns else df.columns[0]
            pivot_table = df.pivot_table(index='Q1', columns='Q4', values=val_col, aggfunc='count')
            sns.heatmap(pivot_table, annot=True, cmap='coolwarm', fmt="g", ax=ax)
            ax.set_title("Response Count Heatmap for Education Level and Frequency of Responses")
            st.pyplot(fig)
        else:
            st.info("Kolom Q1 dan Q4 tidak ditemukan untuk Visualisasi Heatmap.")
            
        # 2. Stacked Bar Chart Agreement Levels (Q5.1 - Q5.5)
        st.subheader("2. Distribusi Agreement Levels (Q5.1 sampai Q5.5)")
        q5_cols = [c for c in df.columns if c.startswith('Q5.')]
        if len(q5_cols) >= 5 and 'Q1' in df.columns and 'Q4' in df.columns:
            fig, ax = plt.subplots(figsize=(12, 5))
            response_counts = df[['Q1', 'Q4'] + q5_cols].melt(
                id_vars=['Q1', 'Q4'], value_vars=q5_cols, 
                var_name='Question', value_name='Response'
            )
            response_order = ['Strongly Disagree', 'Disagree', 'Neutral', 'Agree', 'Strongly Agree']
            sns.countplot(data=response_counts, x='Question', hue='Response', 
                          order=q5_cols, hue_order=response_order, palette='coolwarm', ax=ax)
            ax.set_title('Distribution of Agreement Levels Across Questions')
            plt.xticks(rotation=45)
            plt.tight_layout()
            st.pyplot(fig)
        else:
            st.info("Kolom Q5.x tidak ditemukan untuk Visualisasi Stacked Bar.")
            
        # 3. Agreement by Education
        st.subheader("3. Jumlah Respon 'Agree' berdasarkan Education Level & Frekuensi")
        if len(q5_cols) > 0 and 'Q1' in df.columns and 'Q4' in df.columns:
            response_counts = df[['Q1', 'Q4'] + q5_cols].melt(
                id_vars=['Q1', 'Q4'], value_vars=q5_cols, 
                var_name='Question', value_name='Response'
            )
            agree_responses = response_counts[response_counts['Response'] == 'Agree'].groupby(['Q1', 'Q4']).size().unstack()
            fig, ax = plt.subplots(figsize=(10, 4))
            agree_responses.plot(kind='bar', stacked=True, colormap='viridis', ax=ax)
            ax.set_title('Agreement Responses by Education Level and Frequency')
            ax.set_ylabel('Number of "Agree" Responses')
            plt.xticks(rotation=0)
            st.pyplot(fig)
            
        # 4. Response Length Analysis
        st.subheader("4. Analisis Panjang Karakter Respon Jawaban")
        text_cols = ['Q1', 'Q2', 'Q3', 'Q4', 'Q10']
        existing_text_cols = [c for c in text_cols if c in df.columns]
        if len(existing_text_cols) > 0:
            response_lengths = df[existing_text_cols].fillna('').map(len)
            fig, ax = plt.subplots(figsize=(10, 5))
            for col in response_lengths.columns:
                ax.hist(response_lengths[col], bins=20, alpha=0.5, label=col)
            ax.set_title('Distribution of Response Lengths for Each Question')
            ax.set_xlabel('Response Length')
            ax.set_ylabel('Frequency')
            ax.legend(loc='upper right')
            st.pyplot(fig)
            
    else:
        st.warning("⚠️ Silakan unggah dataset (.csv) terlebih dahulu di sidebar untuk melihat eksplorasi data.")
