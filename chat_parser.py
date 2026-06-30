"""
==========================================
CHAT PARSER
==========================================

Supports:

✔ WhatsApp Exported Chats
✔ Messenger TXT Chats (basic)
✔ Returns clean message records

"""

import re
from datetime import datetime


# ==========================================
# WHATSAPP DATE PATTERN
# Example:
# 12/05/24, 8:30 PM - John: Hello
# ==========================================

PATTERN = re.compile(
    r"^(\d{1,2}/\d{1,2}/\d{2,4}),\s"
    r"(\d{1,2}:\d{2}\s?[APMapm]{0,2})"
    r"\s-\s"
    r"([^:]+):\s"
    r"(.*)"
)


# ==========================================
# PARSE CHAT
# ==========================================

def parse_chat(chat_text):

    messages = []

    current_message = None

    lines = chat_text.split("\n")

    for line in lines:

        line = line.strip()

        if not line:
            continue

        match = PATTERN.match(line)

        # -----------------------------
        # NEW MESSAGE
        # -----------------------------

        if match:

            date = match.group(1)

            time = match.group(2)

            sender = match.group(3).strip()

            message = match.group(4).strip()

            current_message = {
                "date": date,
                "time": time,
                "sender": sender,
                "message": message
            }

            messages.append(current_message)

        # -----------------------------
        # MULTI-LINE MESSAGE
        # -----------------------------

        else:

            if current_message:

                current_message["message"] += (
                    "\n" + line
                )

    return messages


# ==========================================
# TOTAL PARTICIPANTS
# ==========================================

def get_participants(messages):

    return sorted(
        list(
            {
                msg["sender"]
                for msg in messages
            }
        )
    )


# ==========================================
# TOTAL WORDS
# ==========================================

def total_words(messages):

    count = 0

    for msg in messages:

        count += len(
            msg["message"].split()
        )

    return count


# ==========================================
# TOTAL MESSAGES
# ==========================================

def total_messages(messages):

    return len(messages)


# ==========================================
# MOST ACTIVE USER
# ==========================================

def most_active(messages):

    stats = {}

    for msg in messages:

        sender = msg["sender"]

        stats[sender] = stats.get(sender, 0) + 1

    if not stats:

        return None

    return max(
        stats,
        key=stats.get
    )


# ==========================================
# MESSAGE COUNT
# ==========================================

def message_count(messages):

    stats = {}

    for msg in messages:

        sender = msg["sender"]

        stats[sender] = stats.get(sender, 0) + 1

    return stats


# ==========================================
# LONGEST MESSAGE
# ==========================================

def longest_message(messages):

    if not messages:

        return ""

    longest = max(
        messages,
        key=lambda x: len(x["message"])
    )

    return longest


# ==========================================
# SHORTEST MESSAGE
# ==========================================

def shortest_message(messages):

    if not messages:

        return ""

    shortest = min(
        messages,
        key=lambda x: len(x["message"])
    )

    return shortest


# ==========================================
# CHAT DURATION
# ==========================================

def chat_duration(messages):

    if len(messages) < 2:

        return "Unknown"

    try:

        first = datetime.strptime(
            messages[0]["date"],
            "%d/%m/%y"
        )

        last = datetime.strptime(
            messages[-1]["date"],
            "%d/%m/%y"
        )

        days = (last - first).days

        return f"{days} Days"

    except:

        return "Unknown"


# ==========================================
# SEARCH MESSAGES
# ==========================================

def search_messages(messages, keyword):

    keyword = keyword.lower()

    results = []

    for msg in messages:

        if keyword in msg["message"].lower():

            results.append(msg)

    return results