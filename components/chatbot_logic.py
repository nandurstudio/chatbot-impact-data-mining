# Functions representing response logic for 21 Chatbots

def get_chatbot_timestamp_response(ts_input):
    try:
        hour = int(ts_input.split()[1].split(":")[0])
        if hour < 12:
            return "Good morning! Thanks for completing the survey early."
        elif 12 <= hour < 18:
            return "Good afternoon! Hope you're having a productive day."
        else:
            return "Good evening! Thank you for taking the time to complete the survey."
    except Exception:
        return "Format timestamp tidak valid. Gunakan format 'MM.DD.YYYY HH:MM:SS'."

def get_degree_feedback(degree):
    degree_lower = degree.lower()
    if degree_lower == "bachelor":
        return "As a Bachelor’s student, you're at the start of your academic journey. AI tools can assist you in building strong foundations."
    elif degree_lower == "master":
        return "As a Master’s student, you're diving deeper into research. AI can help streamline your advanced studies."
    else:
        return "As a PhD student, AI can accelerate your literature review and synthesis."

def get_field_feedback(field):
    if "economic" in field.lower():
        return "AI tools such as predictive modeling can be very useful in economic research and analysis."
    else:
        return f"Your field of study, {field}, may benefit from AI in research assistance and automation of routine tasks."

def get_ai_usage_motivation(freq):
    f = freq.lower()
    if f == "never":
        return "Don't hesitate to explore AI tools! They can greatly assist your learning process."
    elif f == "rarely":
        return "Using AI tools a little more can enhance your research and productivity."
    elif f == "sometimes":
        return "You're on the right path! Keep using AI tools to further improve your workflow."
    else:
        return "You seem to be familiar with AI tools. Have you considered exploring more advanced AI applications?"

def get_survey_sentiment(sent):
    s = sent.lower()
    if s == "strongly agree":
        return "You seem very positive about AI! It's great to see you embracing new technologies."
    elif s == "agree":
        return "You have a favorable opinion of AI. It’s a valuable tool in modern education."
    elif s == "neutral":
        return "You are undecided about AI. Perhaps exploring more AI tools will help you form an opinion."
    elif s == "disagree":
        return "It’s important to address your concerns. Understanding how AI complements education may change your view."
    else:
        return "You may have strong concerns about AI. Engaging with how AI can be used responsibly might help alleviate these worries."

def get_tool_suggestions(exp):
    e = exp.lower()
    if e == "agree":
        return "We recommend tools like GPT-4 for content generation and machine learning platforms like Google Colab for experiments."
    elif e == "neutral":
        return "You might want to try basic AI tools like ChatGPT or Grammarly to see their potential."
    else:
        return "You might not have had the best experience. Consider trying different AI tools that align with your needs."

def get_ethics_concern(concern):
    if concern.lower() == "yes":
        return "AI ethics is a critical issue. It’s important to stay informed and ensure ethical practices in AI development."
    else:
        return "It’s great that you’re confident in AI. However, staying updated on AI ethics will keep you aware of its impact."

def get_ai_careers(career):
    if career.lower() == "yes":
        return "AI is becoming integral to many industries. Stay curious and keep building your AI skills!"
    else:
        return "Even if AI doesn’t seem relevant now, it’s likely to be part of future workplace environments."

def get_confidence_level(conf):
    c = conf.lower()
    if c == "very confident":
        return "You seem to be highly confident! Continue exploring new AI tools to stay ahead."
    elif c == "confident":
        return "You have a good level of confidence. Keep using AI tools to enhance your learning."
    elif c == "neutral":
        return "If you're unsure, try starting with simpler AI tools like Grammarly or ChatGPT."
    else:
        return "It’s okay to feel unconfident at first. AI tools can be learned gradually."

def get_learning_resources(exp_lvl):
    l = exp_lvl.lower()
    if l == "none":
        return "Start with free AI resources like Coursera's 'AI for Everyone' or Google's AI Crash Course."
    elif l == "minimal":
        return "You might want to try interactive AI platforms like Teachable Machine or explore simple AI projects on GitHub."
    elif l == "moderate":
        return "With moderate exposure, you could enhance your knowledge through platforms like FastAI or experimenting with TensorFlow/Keras."
    else:
        return "With extensive experience, dive into advanced areas like deep learning, reinforcement learning, or AI research papers."

def get_adoption_challenges(challenge):
    c = challenge.lower()
    if c == "lack of knowledge":
        return "Consider joining AI communities like Kaggle or AI forums to expand your knowledge through collaboration."
    elif c == "lack of time":
        return "AI learning can be done in small steps. Try spending 30 minutes a week exploring a specific AI topic."
    elif c == "complexity":
        return "Start with simple tools and move step by step. AI doesn't have to be complicated at the beginning."
    else:
        return "Many AI tools are free or open-source. Explore platforms like Google Colab, which offers free cloud computing for AI projects."

def get_tool_recommendation(need):
    n = need.lower()
    if n == "text analysis":
        return "You can explore tools like GPT-4 for generating text or analyzing large amounts of written content."
    elif n == "image processing":
        return "For image processing, try OpenCV or deep learning libraries like TensorFlow and Keras."
    elif n == "data analysis":
        return "Pandas and Scikit-learn are great for handling data analysis tasks. You might also want to look into AI-powered dashboards like Power BI."
    else:
        return "AI tools like Google Scholar’s AI-enhanced search or semantic search engines can streamline your research process."

def get_ethics_discussion(eth):
    e = eth.lower()
    if e == "bias":
        return "AI bias is a critical issue. It’s important to ensure datasets are representative to avoid unfair outcomes."
    elif e == "privacy":
        return "AI privacy concerns are valid. Make sure the AI tools you use comply with privacy laws like GDPR."
    elif e == "accountability":
        return "AI accountability is still a growing field. It's vital to clearly define who is responsible for AI decisions."
    else:
        return "Transparency in AI models (such as explainability in decision-making) is essential to build trust in AI technologies."

def get_learning_difficulty(diff):
    d = diff.lower()
    if d == "very difficult":
        return "AI can be challenging, but start with basic tutorials on YouTube or AI courses on platforms like Coursera to ease the process."
    elif d == "difficult":
        return "AI requires practice. Try solving small projects or joining communities like Kaggle to learn through experience."
    elif d == "moderate":
        return "You’re progressing well! Keep learning and experimenting with new tools. Practice makes perfect."
    else:
        return "Great! Since you find AI learning easy, consider exploring more complex projects or even participating in AI challenges."

def get_future_trends(trend):
    t = trend.lower()
    if t == "ai in education":
        return "AI in education is transforming how students learn, making personalized learning more accessible. It’s an exciting field!"
    elif t == "ai in healthcare":
        return "AI in healthcare is making breakthroughs in diagnosis, personalized medicine, and patient care."
    elif t == "ai in finance":
        return "AI in finance is reshaping trading strategies, fraud detection, and financial advising. A trend to watch closely!"
    else:
        return "AI is now creating art, music, and designs. The intersection of creativity and AI is a fascinating space!"

def get_personalization_opinion(pers):
    p = pers.lower()
    if p == "yes":
        return "Personalization can help create tailored learning experiences and enhance productivity at work."
    elif p == "no":
        return "You might feel that personalization through AI could be intrusive. Privacy and transparency are key in AI applications."
    else:
        return "It's understandable to be undecided. The impact of personalization in AI can vary depending on its implementation."

def get_career_guidance(deg, field_study):
    d = deg.lower()
    fs = field_study.lower()
    if d == "bachelor":
        if "international economic relations" in fs:
            return "For Bachelor's in International Economic Relations, you could consider careers in economic analysis, international trade consulting, or global business strategy. AI can assist with data-driven decisions."
        else:
            return f"For a Bachelor's in {field_study}, AI skills in data analysis, automation, and predictive modeling can open many doors."
    elif d == "master":
        if "international economic relations" in fs:
            return "With a Master's in International Economic Relations, you could explore roles like international economic policy advisor or AI applications in international market forecasting."
        else:
            return f"A Master's in {field_study} combined with AI expertise can lead to advanced roles like AI research or AI-powered innovations in your domain."
    else:
        return "With a PhD, you can delve into AI research, developing new AI models, or leading AI innovation in your field."

def get_time_management(tm):
    t = tm.lower()
    if t == "often":
        return "It’s great that you want to learn AI, but finding time can be tricky. Try scheduling small, focused sessions (15-30 minutes) in your weekly calendar to slowly build your AI skills."
    elif t == "sometimes":
        return "AI learning can be demanding, but finding some time each week can help you progress. Consider learning on weekends or during free time with bite-sized content like YouTube videos."
    else:
        return "You seem to be managing your time well. Keep exploring new topics and experimenting with AI projects whenever you get a chance!"

def get_research_suggestions(fs_research, eth_concern):
    ec = eth_concern.lower()
    if ec == "bias":
        return f"In {fs_research}, research how bias in AI algorithms can affect decision-making processes in international trade, global policies, or economic forecasts."
    elif ec == "privacy":
        return f"Privacy concerns in AI are crucial in {fs_research}. You can explore how AI technologies impact privacy in global business transactions or international data handling."
    elif ec == "accountability":
        return f"Explore how AI accountability is managed in {fs_research}, such as responsibility for AI-driven decisions in economic markets or international relations."
    else:
        return f"Transparency is key to AI. In {fs_research}, you can explore how transparent AI models can improve international business transparency or economic predictions."

def get_learning_style(style):
    s = style.lower()
    if s == "structured":
        return "If you prefer structured learning, try enrolling in comprehensive AI courses on platforms like Coursera or edX, where you can follow a set curriculum with guided learning."
    else:
        return "For self-paced learning, explore free resources like GitHub repositories, AI blogs, or YouTube tutorials to learn AI at your own speed."

def get_skill_building(exp_lvl):
    el = exp_lvl.lower()
    if el == "beginner":
        return "Start with basic skills like Python programming, data handling (Pandas), and learning simple AI concepts like classification and regression."
    elif el == "intermediate":
        return "Enhance your skills by diving into neural networks, deep learning, and working with popular AI libraries like TensorFlow and PyTorch."
    else:
        return "Focus on mastering AI frameworks, optimizing deep learning models, or exploring research-level AI topics such as reinforcement learning or generative models."
