"""
=========================================
AI PROMPTS
=========================================

This file contains all prompts used by
the AI Chat Conversation Analyzer.

"""

# ==========================================
# SUMMARY
# ==========================================

def summary_prompt(chat):

    return f"""
You are an AI Chat Conversation Analyzer.

Analyze the following chat carefully.

Return your answer in this format:

📄 Conversation Summary

Write a short summary.

😊 Overall Emotion

Positive / Neutral / Negative

🎯 Main Topic

One sentence.

📌 Important Points

- Point 1
- Point 2
- Point 3
- Point 4
- Point 5

⭐ Final Conclusion

A concise conclusion.

Conversation:

{chat}
"""


# ==========================================
# KEYWORDS
# ==========================================

def keyword_prompt(chat):

    return f"""
You are an AI assistant.

Extract ONLY the 15 most important keywords.

Rules:

- One keyword per line
- No numbering
- No explanation
- Maximum 3 words

Conversation:

{chat}
"""


# ==========================================
# INSIGHTS
# ==========================================

def insight_prompt(chat):

    return f"""
You are an AI Chat Conversation Analyzer.

Analyze the conversation.

Return:

📊 Communication Style

😊 Overall Mood

👥 Participant Behaviour

💡 Interesting Insights

⭐ Suggestions

Conversation:

{chat}
"""


# ==========================================
# SENTIMENT
# ==========================================

def sentiment_prompt(chat):

    return f"""
Analyze the conversation sentiment.

Return:

😊 Sentiment

Reason

Conversation:

{chat}
"""


# ==========================================
# EMOTION
# ==========================================

def emotion_prompt(chat):

    return f"""
Identify the dominant emotions in the conversation.

Return:

😊 Main Emotion

😐 Secondary Emotion

Explain in 3-4 lines.

Conversation:

{chat}
"""


# ==========================================
# TOPIC
# ==========================================

def topic_prompt(chat):

    return f"""
Analyze this conversation.

Return:

🎯 Main Topic

📌 Sub Topics

Conversation:

{chat}
"""


# ==========================================
# RESPONSE TIME
# ==========================================

def response_prompt(chat):

    return f"""
Analyze the response pattern.

Return:

⚡ Fast Replies

🐢 Slow Replies

📈 Conversation Flow

Conversation:

{chat}
"""


# ==========================================
# ACTIVE PERSON
# ==========================================

def active_prompt(chat):

    return f"""
Identify the most active participant.

Explain why.

Conversation:

{chat}
"""


# ==========================================
# ASK AI
# ==========================================

def ask_prompt(chat, question):

    return f"""
You are an AI Chat Conversation Analyzer.

Answer ONLY using the conversation below.

If the answer is not present, reply:

"I couldn't find that information in the conversation."

Conversation:

{chat}

Question:

{question}

Answer:
"""