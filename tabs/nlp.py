import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from textblob import TextBlob
from wordcloud import WordCloud
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

def render_nlp_tab(df):
    st.subheader("NLP & Topic Modeling")
    
    if df is not None:
        st.markdown('<div class="section-header">Analisis Sentimen & Topik</div>', unsafe_allow_html=True)
        
        # Combine target text fields
        nlp_cols = ['Q1', 'Q2', 'Q3', 'Q4', 'Q10']
        valid_nlp_cols = [c for c in nlp_cols if c in df.columns]
        
        if len(valid_nlp_cols) > 0:
            # 1. Sentiment Score Distribution
            st.subheader("1. Distribusi Skor Sentimen Responden (TextBlob)")
            responses_text = df[valid_nlp_cols].fillna('')
            
            def get_sentiment(text):
                return TextBlob(str(text)).sentiment.polarity
            
            sentiments = responses_text.apply(lambda x: x.apply(get_sentiment).mean(), axis=1)
            
            fig, ax = plt.subplots(figsize=(10, 4))
            ax.hist(sentiments, bins=20, edgecolor='k', alpha=0.7, color='#4A90E2')
            ax.set_title('Sentiment Distribution of Responses')
            ax.set_xlabel('Sentiment Score (-1.0 to 1.0)')
            ax.set_ylabel('Frequency')
            st.pyplot(fig)
            
            # 2. Word Cloud
            st.subheader("2. Word Cloud Kata Terpopuler")
            combined_text = ' '.join(df[valid_nlp_cols].fillna('').astype(str).agg(' '.join, axis=1))
            
            if len(combined_text.strip()) > 0:
                wordcloud = WordCloud(width=800, height=350, background_color='white').generate(combined_text)
                fig, ax = plt.subplots(figsize=(10, 4))
                ax.imshow(wordcloud, interpolation='bilinear')
                ax.axis('off')
                st.pyplot(fig)
            
            # 3. Topic Modeling (LDA)
            st.subheader("3. Topic Modeling Menggunakan Latent Dirichlet Allocation (LDA)")
            
            vectorizer = CountVectorizer(stop_words='english')
            text_series = df[valid_nlp_cols].fillna('').astype(str).agg(' '.join, axis=1)
            X = vectorizer.fit_transform(text_series)
            
            lda = LatentDirichletAllocation(n_components=5, random_state=0)
            lda.fit(X)
            
            no_top_words = 10
            feature_names = vectorizer.get_feature_names_out()
            
            topic_word_weights = []
            for topic_idx, topic in enumerate(lda.components_):
                words = [feature_names[i] for i in topic.argsort()[:-no_top_words - 1:-1]]
                weights = [topic[i] for i in topic.argsort()[:-no_top_words - 1:-1]]
                topic_word_weights.append(pd.DataFrame({'Words': words, 'Weights': weights}))
                
            selected_topic = st.selectbox("Pilih Topik untuk Dilihat Kata Kuncinya", [f"Topic {i+1}" for i in range(5)])
            topic_num = int(selected_topic.split()[-1]) - 1
            
            fig, ax = plt.subplots(figsize=(8, 4))
            sns.barplot(x='Weights', y='Words', data=topic_word_weights[topic_num], palette='YlGnBu', ax=ax)
            ax.set_title(f'Topic {topic_num+1} - Top Words Weights')
            st.pyplot(fig)
        else:
            st.info("Dataset tidak memiliki kolom teks untuk diproses NLP.")
    else:
        st.warning("⚠️ Silakan unggah dataset (.csv) terlebih dahulu di sidebar untuk melihat analisis NLP.")
