import random

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/122.0.0.0",
    "Mozilla/5.0 (X11; Linux x86_64) Chrome/120.0.0.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
]

def get_random_headers():
    return {
        "User-Agent": random.choice(USER_AGENTS),
        "Accept": "text/html",
        "Connection": "keep-alive"
    }

def generate_variations(username: str):
    variations = {username}

    if "_" in username:
        variations.add(username.replace("_", ""))
        variations.add(username.replace("__", "_"))

    variations.add(username.replace("0", "o"))
    variations.add(username.replace("o", "0"))
    variations.add(username + "_")
    variations.add(username + "1")

    return list(variations)

def calculate_confidence(status, exists):
    if status == 200 and exists:
        return "HIGH"
    if status == 403:
        return "BLOCKED"
    if status == "ERR":
        return "ERROR"
    return "LOW"
