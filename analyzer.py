import requests

# ==========================================
# OLLAMA URL
# ==========================================

OLLAMA_URL = "http://localhost:11434"

# ==========================================
# CHECK OLLAMA
# ==========================================

def check_ollama():

    try:

        response = requests.get(
            f"{OLLAMA_URL}/api/tags",
            timeout=3
        )

        return response.status_code == 200

    except:

        return False


# ==========================================
# GET INSTALLED MODELS
# ==========================================

def get_models():

    try:

        response = requests.get(
            f"{OLLAMA_URL}/api/tags"
        )

        models = response.json()["models"]

        return [
            model["name"]
            for model in models
        ]

    except:

        return ["llama3.2:1b"]


# ==========================================
# GENERATE AI RESPONSE
# ==========================================

def generate_response(prompt, model):

    payload = {

        "model": model,
        "prompt": prompt,
        "stream": False

    }

    response = requests.post(

        f"{OLLAMA_URL}/api/generate",

        json=payload

    )

    return response.json()["response"]


# ==========================================
# AI SUMMARY
# ==========================================

def summarize_chat(chat, model):

    prompt = f"""

You are an AI Chat Conversation Analyzer.

Read the conversation carefully.

Return your answer in this format:

📄 Conversation Summary

😊 Overall Emotion

🎯 Main Topic

📌 Important Points

⭐ Final Conclusion

Conversation:

{chat}

"""

    return generate_response(
        prompt,
        model
    )


# ==========================================
# EMOTION DETECTION
# ==========================================

def detect_emotion(chat, model):

    prompt = f"""

Analyze the conversation.

Return only:

Overall Emotion

Explain why in 2-3 lines.

Conversation:

{chat}

"""

    return generate_response(
        prompt,
        model
    )


# ==========================================
# SENTIMENT ANALYSIS
# ==========================================

def sentiment(chat, model):

    prompt = f"""

Classify the conversation as:

Positive

Negative

Neutral

Explain briefly.

Conversation:

{chat}

"""

    return generate_response(
        prompt,
        model
    )


# ==========================================
# KEYWORDS
# ==========================================

def extract_keywords(chat, model):

    prompt = f"""

Extract the 15 most important keywords.

Rules:

One keyword per line.

No numbering.

Conversation:

{chat}

"""

    return generate_response(
        prompt,
        model
    )


# ==========================================
# TOPIC DETECTION
# ==========================================

def detect_topic(chat, model):

    prompt = f"""

Identify the main topic of this conversation.

Also provide:

Sub Topics

Conversation:

{chat}

"""

    return generate_response(
        prompt,
        model
    )


# ==========================================
# AI INSIGHTS
# ==========================================

def generate_insights(chat, model):

    prompt = f"""

Analyze this conversation.

Provide:

Conversation Quality

Communication Style

Important Decisions

Suggestions

Overall Insight

Conversation:

{chat}

"""

    return generate_response(
        prompt,
        model
    )


# ==========================================
# RESPONSE TIME ANALYSIS
# ==========================================

def response_time_analysis(chat, model):

    prompt = f"""

Analyze the response timing between participants.

Mention:

Fast Replies

Slow Replies

Conversation Flow

Conversation:

{chat}

"""

    return generate_response(
        prompt,
        model
    )


# ==========================================
# MOST ACTIVE PERSON
# ==========================================

def active_person(chat, model):

    prompt = f"""

Based on the conversation,

identify the most active participant.

Explain why.

Conversation:

{chat}

"""

    return generate_response(
        prompt,
        model
    )


# ==========================================
# ASK AI
# ==========================================

def ask_chat(chat, question, model):

    prompt = f"""

You are an AI Chat Conversation Analyzer.

Answer ONLY using the given conversation.

If the answer does not exist,

reply:

"I couldn't find that information in the conversation."

Conversation:

{chat}

Question:

{question}

Answer:

"""

    return generate_response(
        prompt,
        model
    )