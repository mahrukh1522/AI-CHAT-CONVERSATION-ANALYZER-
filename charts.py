"""
=========================================
CHARTS
=========================================

Creates charts for the AI Chat Conversation Analyzer.
"""

import pandas as pd
import matplotlib.pyplot as plt


# ==========================================
# MESSAGES PER USER
# ==========================================

def messages_per_user(df):

    counts = df["sender"].value_counts()

    fig, ax = plt.subplots(figsize=(8,5))

    ax.bar(
        counts.index,
        counts.values
    )

    ax.set_title("Messages Per Participant")

    ax.set_xlabel("Participant")

    ax.set_ylabel("Messages")

    plt.xticks(rotation=20)

    return fig


# ==========================================
# DAILY ACTIVITY
# ==========================================

def daily_activity(df):

    activity = (
        df.groupby("date")
        .size()
    )

    fig, ax = plt.subplots(figsize=(10,5))

    ax.plot(
        activity.index,
        activity.values,
        marker="o"
    )

    ax.set_title("Daily Chat Activity")

    ax.set_xlabel("Date")

    ax.set_ylabel("Messages")

    plt.xticks(rotation=45)

    return fig


# ==========================================
# PIE CHART
# ==========================================

def message_distribution(df):

    counts = df["sender"].value_counts()

    fig, ax = plt.subplots(figsize=(6,6))

    ax.pie(
        counts.values,
        labels=counts.index,
        autopct="%1.1f%%",
        startangle=90
    )

    ax.set_title("Message Distribution")

    return fig


# ==========================================
# HOURLY ACTIVITY
# ==========================================

def hourly_activity(df):

    hours = []

    for t in df["time"]:

        try:

            hour = pd.to_datetime(t).hour

            hours.append(hour)

        except:

            pass

    hour_df = pd.Series(hours).value_counts().sort_index()

    fig, ax = plt.subplots(figsize=(10,5))

    ax.bar(
        hour_df.index,
        hour_df.values
    )

    ax.set_title("Hourly Activity")

    ax.set_xlabel("Hour")

    ax.set_ylabel("Messages")

    return fig


# ==========================================
# WEEKDAY ACTIVITY
# ==========================================

def weekday_activity(df):

    days = []

    for d in df["date"]:

        try:

            day = pd.to_datetime(
                d,
                dayfirst=True
            ).day_name()

            days.append(day)

        except:

            pass

    day_df = pd.Series(days).value_counts()

    order = [

        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"

    ]

    day_df = day_df.reindex(
        order,
        fill_value=0
    )

    fig, ax = plt.subplots(figsize=(10,5))

    ax.bar(
        day_df.index,
        day_df.values
    )

    ax.set_title("Weekly Activity")

    ax.set_xlabel("Day")

    ax.set_ylabel("Messages")

    plt.xticks(rotation=25)

    return fig


# ==========================================
# TOP WORDS
# ==========================================

def top_words(df):

    words = []

    stop_words = {

        "the","a","an","is","are","to","of",
        "and","or","in","on","for","at",
        "i","you","we","they","he","she",
        "it","this","that","my","your",
        "me","ok","okay","yes","no"

    }

    for message in df["message"]:

        for word in message.lower().split():

            word = word.strip(".,!?()[]{}<>:;\"'")

            if len(word) > 2 and word not in stop_words:

                words.append(word)

    word_df = (
        pd.Series(words)
        .value_counts()
        .head(10)
    )

    fig, ax = plt.subplots(figsize=(10,5))

    ax.bar(
        word_df.index,
        word_df.values
    )

    ax.set_title("Top 10 Most Used Words")

    ax.set_xlabel("Words")

    ax.set_ylabel("Frequency")

    plt.xticks(rotation=35)

    return fig


# ==========================================
# AVERAGE MESSAGE LENGTH
# ==========================================

def message_length(df):

    lengths = df["message"].apply(
        lambda x: len(str(x).split())
    )

    fig, ax = plt.subplots(figsize=(8,5))

    ax.hist(
        lengths,
        bins=20
    )

    ax.set_title("Message Length Distribution")

    ax.set_xlabel("Words")

    ax.set_ylabel("Frequency")

    return fig