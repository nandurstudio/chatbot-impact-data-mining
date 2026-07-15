import streamlit as st
from components.styles import inject_custom_css
from utils.data_loader import load_data
from tabs.overview import render_overview_tab
from tabs.preview import render_preview_tab
from tabs.eda import render_eda_tab
from tabs.nlp import render_nlp_tab
from tabs.chatbots import render_chatbots_tab

# Set page config
st.set_page_config(
    page_title="21 Chatbots Evaluation Dashboard",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply premium styles
inject_custom_css()

# Header Section
st.markdown('<div class="main-title">Evaluasi Dampak 21 Chatbots</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Final Project Praktikum Data Mining 2026 — Universitas Pelita Bangsa</div>', unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.image("https://img.icons8.com/fluent/96/000000/artificial-intelligence.png", width=80)
    st.header("⚙️ Data & Controls")
    
    delimiter = st.selectbox("Pemisah Kolom (Delimiter)", [";", ","], index=0)
    encoding = st.selectbox("Encoding File", ["ISO-8859-1", "utf-8", "utf-8-sig"], index=0)
    
    uploaded_file = st.file_uploader("Unggah File Dataset (.csv)", type=["csv"])
    
    st.markdown("---")
    st.markdown("""
    **Dataset Info:**
    - Title: *21 Chatbots: Evaluating Their Impact on University Learning*
    - Author: Jocelyn C. Dumlao (2024)
    - Respondent: 131 students
    """)

# Load Dataset if available
import os
local_dataset_path = "AI_Chatbots_Students_Attitude_Dataset_EN.csv"

df = None
if uploaded_file is not None:
    try:
        df = load_data(uploaded_file, delimiter, encoding)
        st.sidebar.success("Dataset loaded successfully!")
    except Exception as e:
        st.sidebar.error(f"Error loading file: {e}")
elif os.path.exists(local_dataset_path):
    try:
        df = load_data(local_dataset_path, ";", "ISO-8859-1")
        st.sidebar.info("Dataset auto-loaded from project path!")
    except Exception as e:
        st.sidebar.error(f"Error auto-loading dataset: {e}")

# Render Tabbed navigation
tab_list = st.tabs([
    "🏠 Overview & Summary", 
    "🔍 Preview Data", 
    "📊 Analisis Visual (EDA)", 
    "📝 NLP & Topic Modeling", 
    "🤖 Interactive Chatbots (21 Playgrounds)"
])

with tab_list[0]:
    render_overview_tab(df)

with tab_list[1]:
    render_preview_tab(df)

with tab_list[2]:
    render_eda_tab(df)

with tab_list[3]:
    render_nlp_tab(df)

with tab_list[4]:
    render_chatbots_tab()
