import string

# ---------- Normalization ----------
def normalize(text):
    text = text.strip().lower()
    text = text.replace("'", "")  # whats, im, dont
    return text.translate(str.maketrans("", "", string.punctuation))

# ---------- Session state ----------
session = {
    "name": None,
    "mode": "main",        # main | help_menu | support | orders | awaiting_name
    "turns": 0,
    "fallbacks": 0,
}

# ---------- Intent handlers (functional dictionary map) ----------
def greet(text):
    if session["name"]:
        return f"Hello again, {session['name'].title()}! How can I help?"
    return "Hello! How can I help you?"

def how_are_you(text):
    return "I'm doing great, thanks for asking!"

def bot_identity(text):
    return "I'm Python Chatbot, a rule-based assistant."

def set_name(text):
    name = text.split("my name is", 1)[1].strip()
    if not name:
        session["mode"] = "awaiting_name"
        return "What should I call you?"
    session["name"] = name
    return f"Nice to meet you, {name.title()}!"

def get_name(text):
    if session["name"]:
        return f"Your name is {session['name'].title()}."
    return "I don't know your name yet. Say 'my name is ...'."

def thanks(text):
    return "You're welcome!"

def open_help(text):
    session["mode"] = "help_menu"
    return ("What do you need help with?\n"
            "  1. Account\n  2. Orders\n  3. Technical support\n"
            "  (type a number, or 'back')")

INTENTS = {
    "greet": greet, "how_are_you": how_are_you, "identity": bot_identity,
    "set_name": set_name, "get_name": get_name, "thanks": thanks, "help": open_help,
}

# Keyword rules: intent -> trigger phrases (checked with substring match)
KEYWORDS = {
    "set_name": ["my name is"],
    "get_name": ["know my name", "what is my name", "whats my name"],
    "how_are_you": ["how are you"],
    "identity": ["your name", "who are you"],
    "thanks": ["thanks", "thank you", "thankyou"],
    "help": ["help", "menu", "support"],
    "greet": ["hello", "hi", "hey"],
}

def detect_intent(text):
    words = text.split()
    for intent, phrases in KEYWORDS.items():
        for p in phrases:
            # single words must match whole words, so "hi" doesn't match "this"
            if (" " in p and p in text) or (" " not in p and p in words):
                return intent
    return None

# ---------- Help trees (nested flows) ----------
HELP_TREES = {
    "1": {"title": "Account", "options": {
        "1": "To reset your password, use 'Forgot password' on the login page.",
        "2": "To update your email, go to Settings > Profile.",
    }},
    "2": {"title": "Orders", "options": {
        "1": "Track an order from 'My Orders' using your order ID.",
        "2": "Returns are accepted within 30 days of delivery.",
    }},
    "3": {"title": "Technical support", "options": {
        "1": "Try restarting the app and clearing the cache.",
        "2": "For bugs, email support@example.com with a screenshot.",
    }},
}

def handle_help_menu(text):
    if text in ("back", "main", "cancel"):
        session["mode"] = "main"
        return "Back to the main menu. What else can I do?"
    if text in HELP_TREES:
        session["mode"] = f"tree_{text}"
        tree = HELP_TREES[text]
        lines = [f"{tree['title']} help:"]
        lines += [f"  {k}. Topic {k}" for k in tree["options"]]
        lines.append("  (type a number, or 'back')")
        return "\n".join(lines)
    return "Please choose 1, 2 or 3 (or type 'back')."

def handle_tree(text):
    tree = HELP_TREES[session["mode"].split("_")[1]]
    if text == "back":
        session["mode"] = "help_menu"
        return "Back to help topics. Choose 1, 2 or 3."
    if text in tree["options"]:
        return tree["options"][text]
    return f"Choose one of {', '.join(tree['options'])} or type 'back'."

def handle_awaiting_name(text):
    session["name"] = text
    session["mode"] = "main"
    return f"Nice to meet you, {text.title()}!"

# ---------- Fallback ----------
def fallback():
    session["fallbacks"] += 1
    if session["fallbacks"] >= 3:
        session["fallbacks"] = 0
        return "I'm still not getting it. Type 'help' for a menu of things I can do."
    return "Sorry, I didn't understand that. Try rephrasing, or type 'help'."

# ---------- Router ----------
def respond(text):
    session["turns"] += 1
    mode = session["mode"]

    if mode == "awaiting_name":
        return handle_awaiting_name(text)
    if mode == "help_menu":
        return handle_help_menu(text)
    if mode.startswith("tree_"):
        return handle_tree(text)

    intent = detect_intent(text)
    if intent in INTENTS:
        session["fallbacks"] = 0
        return INTENTS[intent](text)
    return fallback()

# ---------- Main loop ----------
def main():
    print("=" * 40)
    print("       Welcome to Python Chatbot")
    print("=" * 40)
    print("Bot: Hi! Type 'help' for options or 'exit' to quit.")

    while True:
        try:
            raw = input("\nYou: ")
        except (EOFError, KeyboardInterrupt):
            print("\nBot: Goodbye!")
            break

        text = normalize(raw)
        if not text:
            print("Bot: Please type something.")
            continue
        if text in ("exit", "quit", "bye"):
            print(f"Bot: Goodbye{', ' + session['name'].title() if session['name'] else ''}!")
            break

        print("Bot:", respond(text))

if __name__ == "__main__":
    main()