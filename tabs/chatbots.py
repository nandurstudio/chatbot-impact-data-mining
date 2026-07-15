import streamlit as st
import components.chatbot_logic as cb

def render_chatbots_tab():
    st.markdown('<div class="section-header">🤖 Chatbot Simulation Playground</div>', unsafe_allow_html=True)
    st.write("Silakan pilih salah satu dari 21 tipe Chatbot dari menu dropdown di bawah untuk menguji respon logisnya.")
    
    chatbot_options = [
        "Chatbot 1: Timestamp Response Bot",
        "Chatbot 2: Degree-Based Custom Feedback Bot",
        "Chatbot 3: Field of Study Bot",
        "Chatbot 4: AI Usage Frequency and Motivation Bot",
        "Chatbot 5: Survey Sentiment Summary Bot",
        "Chatbot 6: Personalized AI Tool Suggestions Bot",
        "Chatbot 7: AI Ethical Concerns Bot",
        "Chatbot 8: AI in Future Careers Bot",
        "Chatbot 9: AI Confidence Level Bot",
        "Chatbot 10: AI Learning Resources Bot",
        "Chatbot 11: AI Adoption Challenges Bot",
        "Chatbot 12: AI Tool Recommendation Bot",
        "Chatbot 13: AI Ethics Discussion Bot",
        "Chatbot 14: Learning AI Difficulty Bot",
        "Chatbot 15: Future AI Trends Bot",
        "Chatbot 16: AI Personalization Bot",
        "Chatbot 17: AI Career Guidance Bot",
        "Chatbot 18: AI Time Management Bot",
        "Chatbot 19: AI Research Bot",
        "Chatbot 20: AI Learning Style Bot",
        "Chatbot 21: AI Skill Building Bot"
    ]
    
    selected_bot = st.selectbox("Pilih Chatbot", chatbot_options)
    
    if selected_bot == "Chatbot 1: Timestamp Response Bot":
        st.info("Bot ini memberikan salam/respon berdasarkan waktu pengisian survei.")
        ts_input = st.text_input("Masukkan Timestamp (Format: MM.DD.YYYY HH:MM:SS)", "09.08.2024 14:30:00")
        if st.button("Kirim"):
            res = cb.get_chatbot_timestamp_response(ts_input)
            st.markdown(f'<div class="chat-bubble">💬 <b>Timestamp Bot:</b> {res}</div>', unsafe_allow_html=True)
                
    elif selected_bot == "Chatbot 2: Degree-Based Custom Feedback Bot":
        st.info("Bot ini memberikan saran akademik berdasarkan jenjang pendidikan.")
        degree = st.selectbox("Pilih Jenjang Pendidikan", ["Bachelor", "Master", "PhD"])
        if st.button("Kirim"):
            res = cb.get_degree_feedback(degree)
            st.markdown(f'<div class="chat-bubble">💬 <b>Degree Bot:</b> {res}</div>', unsafe_allow_html=True)

    elif selected_bot == "Chatbot 3: Field of Study Bot":
        st.info("Bot ini merekomendasikan tool AI spesifik untuk bidang studi tertentu.")
        field = st.text_input("Masukkan Bidang Studi Anda", "Economics and Management")
        if st.button("Kirim"):
            res = cb.get_field_feedback(field)
            st.markdown(f'<div class="chat-bubble">💬 <b>Field Bot:</b> {res}</div>', unsafe_allow_html=True)

    elif selected_bot == "Chatbot 4: AI Usage Frequency and Motivation Bot":
        st.info("Bot ini memberikan motivasi berdasarkan seberapa sering Anda memakai AI.")
        freq = st.selectbox("Seberapa sering Anda menggunakan tool AI?", ["Never", "Rarely", "Sometimes", "Often"])
        if st.button("Kirim"):
            res = cb.get_ai_usage_motivation(freq)
            st.markdown(f'<div class="chat-bubble">💬 <b>Motivation Bot:</b> {res}</div>', unsafe_allow_html=True)

    elif selected_bot == "Chatbot 5: Survey Sentiment Summary Bot":
        st.info("Bot ini menyimpulkan sikap umum Anda terhadap AI di bidang pendidikan.")
        sent = st.selectbox("Bagaimana sikap Anda terhadap AI dalam pendidikan?", ["Strongly Agree", "Agree", "Neutral", "Disagree", "Strongly Disagree"])
        if st.button("Kirim"):
            res = cb.get_survey_sentiment(sent)
            st.markdown(f'<div class="chat-bubble">💬 <b>Sentiment Bot:</b> {res}</div>', unsafe_allow_html=True)

    elif selected_bot == "Chatbot 6: Personalized AI Tool Suggestions Bot":
        st.info("Mendapatkan rekomendasi tool AI berdasarkan kenyamanan pengalaman Anda.")
        exp = st.selectbox("Bagaimana Anda menilai pengalaman Anda dengan tool AI?", ["Agree", "Neutral", "Disagree"])
        if st.button("Kirim"):
            res = cb.get_tool_suggestions(exp)
            st.markdown(f'<div class="chat-bubble">💬 <b>Suggestion Bot:</b> {res}</div>', unsafe_allow_html=True)

    elif selected_bot == "Chatbot 7: AI Ethical Concerns Bot":
        st.info("Membahas kekhawatiran etika atau privasi data AI.")
        concern = st.selectbox("Apakah Anda cemas dengan masalah etika atau privasi data AI?", ["Yes", "No"])
        if st.button("Kirim"):
            res = cb.get_ethics_concern(concern)
            st.markdown(f'<div class="chat-bubble">💬 <b>Ethics Bot:</b> {res}</div>', unsafe_allow_html=True)

    elif selected_bot == "Chatbot 8: AI in Future Careers Bot":
        st.info("Membahas prospek peran AI di karir masa depan.")
        career = st.selectbox("Apakah Anda melihat AI memegang peran penting di karir masa depan Anda?", ["Yes", "No"])
        if st.button("Kirim"):
            res = cb.get_ai_careers(career)
            st.markdown(f'<div class="chat-bubble">💬 <b>Career Bot:</b> {res}</div>', unsafe_allow_html=True)

    elif selected_bot == "Chatbot 9: AI Confidence Level Bot":
        st.info("Bot ini mendeteksi tingkat kepercayaan diri Anda menggunakan AI di universitas.")
        conf = st.selectbox("Seberapa percaya diri Anda menggunakan AI di lingkungan belajar?", ["Very Confident", "Confident", "Neutral", "Unconfident"])
        if st.button("Kirim"):
            res = cb.get_confidence_level(conf)
            st.markdown(f'<div class="chat-bubble">💬 <b>Confidence Bot:</b> {res}</div>', unsafe_allow_html=True)

    elif selected_bot == "Chatbot 10: AI Learning Resources Bot":
        st.info("Menyarankan sumber belajar AI berdasarkan pemaparan Anda sebelumnya.")
        exp_lvl = st.selectbox("Bagaimana pemaparan Anda terhadap tool AI?", ["None", "Minimal", "Moderate", "Extensive"])
        if st.button("Kirim"):
            res = cb.get_learning_resources(exp_lvl)
            st.markdown(f'<div class="chat-bubble">💬 <b>Resources Bot:</b> {res}</div>', unsafe_allow_html=True)

    elif selected_bot == "Chatbot 11: AI Adoption Challenges Bot":
        st.info("Membantu mencarikan solusi atas hambatan utama dalam mengadopsi AI.")
        challenge = st.selectbox("Apa tantangan terbesar Anda dalam mengadopsi AI?", ["Lack of Knowledge", "Lack of Time", "Complexity", "Cost"])
        if st.button("Kirim"):
            res = cb.get_adoption_challenges(challenge)
            st.markdown(f'<div class="chat-bubble">💬 <b>Adoption Bot:</b> {res}</div>', unsafe_allow_html=True)

    elif selected_bot == "Chatbot 12: AI Tool Recommendation Bot":
        st.info("Merekomendasikan tool spesifik sesuai kebutuhan tugas.")
        need = st.selectbox("Untuk apa Anda membutuhkan tool AI?", ["Text Analysis", "Image Processing", "Data Analysis", "Research"])
        if st.button("Kirim"):
            res = cb.get_tool_recommendation(need)
            st.markdown(f'<div class="chat-bubble">💬 <b>Recommend Bot:</b> {res}</div>', unsafe_allow_html=True)

    elif selected_bot == "Chatbot 13: AI Ethics Discussion Bot":
        st.info("Mendiskusikan isu etika AI secara mendalam.")
        eth = st.selectbox("Apa isu etika AI yang paling Anda cemaskan?", ["Bias", "Privacy", "Accountability", "Transparency"])
        if st.button("Kirim"):
            res = cb.get_ethics_discussion(eth)
            st.markdown(f'<div class="chat-bubble">💬 <b>Ethics Discussion Bot:</b> {res}</div>', unsafe_allow_html=True)

    elif selected_bot == "Chatbot 14: Learning AI Difficulty Bot":
        st.info("Memberikan suntikan motivasi berdasarkan tingkat kesulitan belajar AI Anda.")
        diff = st.selectbox("Seberapa sulit Anda mempelajari tool AI?", ["Very Difficult", "Difficult", "Moderate", "Easy"])
        if st.button("Kirim"):
            res = cb.get_learning_difficulty(diff)
            st.markdown(f'<div class="chat-bubble">💬 <b>Difficulty Bot:</b> {res}</div>', unsafe_allow_html=True)

    elif selected_bot == "Chatbot 15: Future AI Trends Bot":
        st.info("Mengeksplorasi tren teknologi AI masa depan yang menarik minat Anda.")
        trend = st.selectbox("Tren AI masa depan mana yang paling Anda minati?", ["AI in Education", "AI in Healthcare", "AI in Finance", "AI in Art"])
        if st.button("Kirim"):
            res = cb.get_future_trends(trend)
            st.markdown(f'<div class="chat-bubble">💬 <b>Trend Bot:</b> {res}</div>', unsafe_allow_html=True)

    elif selected_bot == "Chatbot 16: AI Personalization Bot":
        st.info("Membahas penggunaan AI untuk mempersonalisasi lingkungan kerja atau studi.")
        pers = st.selectbox("Apakah menurut Anda AI harus digunakan untuk mempersonalisasi lingkungan belajar/kerja?", ["Yes", "No", "Neutral"])
        if st.button("Kirim"):
            res = cb.get_personalization_opinion(pers)
            st.markdown(f'<div class="chat-bubble">💬 <b>Personalization Bot:</b> {res}</div>', unsafe_allow_html=True)

    elif selected_bot == "Chatbot 17: AI Career Guidance Bot":
        st.info("Memberikan rekomendasi karir spesifik berdasarkan jenjang pendidikan dan jurusan.")
        deg = st.selectbox("Pilih Degree", ["Bachelor", "Master", "PhD"])
        field_study = st.text_input("Jurusan / Bidang Studi", "International Economic Relations")
        if st.button("Kirim"):
            res = cb.get_career_guidance(deg, field_study)
            st.markdown(f'<div class="chat-bubble">💬 <b>Career Guidance Bot:</b> {res}</div>', unsafe_allow_html=True)

    elif selected_bot == "Chatbot 18: AI Time Management Bot":
        st.info("Membantu manajemen waktu dalam belajar kecerdasan buatan.")
        tm = st.selectbox("Seberapa sering Anda kesulitan membagi waktu untuk belajar AI?", ["Often", "Sometimes", "Rarely"])
        if st.button("Kirim"):
            res = cb.get_time_management(tm)
            st.markdown(f'<div class="chat-bubble">💬 <b>Time Management Bot:</b> {res}</div>', unsafe_allow_html=True)

    elif selected_bot == "Chatbot 19: AI Research Bot":
        st.info("Mencari topik penelitian AI yang tepat sesuai rumpun studi dan kecemasan etika.")
        fs_research = st.text_input("Jurusan / Bidang Studi", "International Economic Relations")
        eth_concern = st.selectbox("Isu etika AI yang menarik minat Anda", ["Bias", "Privacy", "Accountability", "Transparency"])
        if st.button("Kirim"):
            res = cb.get_research_suggestions(fs_research, eth_concern)
            st.markdown(f'<div class="chat-bubble">💬 <b>Research Bot:</b> {res}</div>', unsafe_allow_html=True)

    elif selected_bot == "Chatbot 20: AI Learning Style Bot":
        st.info("Menyarankan metode belajar optimal berdasarkan gaya belajar Anda.")
        style = st.selectbox("Apakah Anda lebih suka pembelajaran terstruktur atau eksplorasi mandiri?", ["Structured", "Self-paced"])
        if st.button("Kirim"):
            res = cb.get_learning_style(style)
            st.markdown(f'<div class="chat-bubble">💬 <b>Learning Style Bot:</b> {res}</div>', unsafe_allow_html=True)

    elif selected_bot == "Chatbot 21: AI Skill Building Bot":
        st.info("Menyusun roadmap keahlian AI yang harus dikembangkan sesuai tingkat keahlian saat ini.")
        exp_lvl = st.selectbox("Pilih Tingkat Pengalaman AI Anda Saat Ini", ["Beginner", "Intermediate", "Advanced"])
        if st.button("Kirim"):
            res = cb.get_skill_building(exp_lvl)
            st.markdown(f'<div class="chat-bubble">💬 <b>Skill Building Bot:</b> {res}</div>', unsafe_allow_html=True)
