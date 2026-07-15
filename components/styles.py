import streamlit as st

def inject_custom_css():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&display=swap');
        
        html, body, [class*="css"] {
            font-family: 'Outfit', sans-serif;
        }
        
        .main-title {
            font-size: 2.8rem;
            font-weight: 800;
            background: linear-gradient(135deg, #007FFF, #8B0082);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 0.2rem;
        }
        
        .sub-title {
            font-size: 1.15rem;
            color: var(--text-color);
            opacity: 0.7;
            margin-bottom: 2rem;
            font-weight: 400;
        }
        
        .section-header {
            font-size: 1.5rem;
            font-weight: 700;
            color: var(--text-color);
            margin-top: 1.5rem;
            margin-bottom: 1rem;
            border-bottom: 2px solid rgba(128, 128, 128, 0.2);
            padding-bottom: 0.3rem;
        }
        
        .metric-card {
            background: var(--secondary-background-color);
            color: var(--text-color);
            border-radius: 12px;
            padding: 1.25rem;
            border: 1px solid rgba(128, 128, 128, 0.2);
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.02);
            text-align: center;
            transition: all 0.3s ease;
        }
        
        .metric-card:hover {
            transform: translateY(-3px);
            box-shadow: 0 10px 15px rgba(0, 0, 0, 0.05);
            border-color: #007FFF;
        }
        
        .metric-value {
            font-size: 1.8rem;
            font-weight: 700;
            color: #007FFF;
        }
        
        .metric-label {
            font-size: 0.85rem;
            color: var(--text-color);
            opacity: 0.8;
            margin-top: 0.25rem;
            font-weight: 500;
        }
        
        .chat-bubble {
            background: var(--secondary-background-color);
            border-radius: 15px;
            padding: 1rem 1.5rem;
            margin-top: 1rem;
            border-left: 5px solid #007FFF;
            font-size: 1.05rem;
            color: var(--text-color);
        }
        </style>
    """, unsafe_allow_html=True)
