import streamlit as st
import pandas as pd
from chat_parser import parse_chat
from analyzer import (
    check_ollama,
    get_models,
    generate_response
)
from prompts import (
    summary_prompt,
    keyword_prompt,
    insight_prompt
)

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="AI Chat Conversation Analyzer",
    page_icon="💬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# CUSTOM CSS
# ==========================================

st.markdown("""
<style>

.stApp{
    background:#0E1117;
    color:white;
}

#MainMenu{
visibility:hidden;
}

footer{
visibility:hidden;
}

header{
visibility:hidden;
}

[data-testid="stSidebar"]{
background:#161B22;
}

.stButton>button{
width:100%;
background:#2563EB;
color:white;
border:none;
border-radius:8px;
padding:10px;
font-weight:bold;
}

[data-testid="stFileUploader"]{
border:2px dashed #2563EB;
padding:15px;
border-radius:10px;
}

.metric-box{
background:#1F2937;
padding:15px;
border-radius:10px;
text-align:center;
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# SIDEBAR
# ==========================================

with st.sidebar:

    st.title("💬 AI Chat Analyzer")

    if check_ollama():
        st.success("🟢 Ollama Online")
    else:
        st.error("🔴 Ollama Offline")
        st.info("Run : ollama serve")

    st.divider()

    models = get_models()

    selected_model = st.selectbox(
        "Choose AI Model",
        models
    )

    st.divider()

    st.write("### Supported Files")

    st.write("✅ WhatsApp TXT")

    st.write("✅ Messenger TXT")

    st.divider()

    st.write("### AI Features")

    st.write("📄 Summary")

    st.write("😊 Emotion Detection")

    st.write("📊 Sentiment")

    st.write("👤 Most Active Person")

    st.write("🔑 Keywords")

    st.write("💡 AI Insights")

    st.write("❓ Ask AI")

# ==========================================
# TITLE
# ==========================================

st.title("💬 AI Chat Conversation Analyzer")

st.subheader(
    "Analyze WhatsApp & Messenger Chats using Local AI"
)

st.write(
    "Upload an exported chat and let AI understand your conversation."
)

st.divider()

# ==========================================
# FILE UPLOADER
# ==========================================

uploaded_file = st.file_uploader(
    "Upload Chat File",
    type=["txt"]
)

# ==========================================
# IF FILE UPLOADED
# ==========================================

if uploaded_file is not None:

    st.success("✅ Chat Uploaded Successfully")

    chat_text = uploaded_file.read().decode("utf-8")

    messages = parse_chat(chat_text)

    df = pd.DataFrame(messages)

    st.subheader("📄 Conversation Preview")

    st.dataframe(
        df.head(20),
        use_container_width=True
    )

    st.divider()

    total_messages = len(df)

    participants = df["sender"].nunique()

    total_words = df["message"].str.split().str.len().sum()

    c1,c2,c3 = st.columns(3)

    with c1:
        st.metric(
            "💬 Messages",
            total_messages
        )

    with c2:
        st.metric(
            "👥 Participants",
            participants
        )

    with c3:
        st.metric(
            "📝 Words",
            total_words
        )

    st.divider()
        # ==========================================
    # MOST ACTIVE PERSON
    # ==========================================

    st.subheader("👤 Most Active Participant")

    active_user = (
        df["sender"]
        .value_counts()
        .reset_index()
    )

    active_user.columns = [
        "Participant",
        "Messages"
    ]

    st.dataframe(
        active_user,
        use_container_width=True
    )

    st.bar_chart(
        active_user.set_index("Participant")
    )

    st.divider()

    # ==========================================
    # AI SUMMARY
    # ==========================================

    st.subheader("🤖 AI Conversation Summary")

    if st.button("🚀 Analyze Conversation"):

        with st.spinner("AI is analyzing the conversation..."):

            summary = generate_response(
                summary_prompt(chat_text),
                selected_model
            )

        st.success("Analysis Complete!")

        st.markdown(summary)

        st.download_button(
            "📥 Download Summary",
            summary,
            file_name="conversation_summary.txt",
            mime="text/plain"
        )

    st.divider()

    # ==========================================
    # KEYWORDS
    # ==========================================

    st.subheader("🔑 Important Keywords")

    if st.button("Extract Keywords"):

        with st.spinner("Finding keywords..."):

            keywords = generate_response(
                keyword_prompt(chat_text),
                selected_model
            )

        for word in keywords.split("\n"):

            if word.strip():

                st.info(f"🔹 {word}")

    st.divider()

    # ==========================================
    # AI INSIGHTS
    # ==========================================

    st.subheader("💡 AI Insights")

    if st.button("Generate Insights"):

        with st.spinner("Generating insights..."):

            insights = generate_response(
                insight_prompt(chat_text),
                selected_model
            )

        st.success("Insights Generated")

        st.write(insights)

    st.divider()

    # ==========================================
    # ASK AI
    # ==========================================

    st.subheader("❓ Ask AI About Conversation")

    question = st.text_input(
        "Ask anything about this chat..."
    )

    if st.button("Ask AI"):

        if question.strip() == "":

            st.warning("Please enter a question.")

        else:

            prompt = f"""
You are an AI Chat Conversation Analyzer.

Conversation:

{chat_text}

Question:

{question}

Answer:
"""

            with st.spinner("Thinking..."):

                answer = generate_response(
                    prompt,
                    selected_model
                )

            st.success("Answer")

            st.write(answer)

else:

    st.info(
        "⬆ Upload a WhatsApp or Messenger chat to begin."
    )