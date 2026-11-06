
import string


# ==========================================
# 1. CHATBOT WELCOME MESSAGE
# ==========================================

print("=" * 40)
print("       Welcome to Python Chatbot")
print("=" * 40)

print("Bot: Hello! I am your Python chatbot.")
print("Bot: Type 'help' to see what I can do.")
print("Bot: Type 'exit' to end the conversation.")


# ==========================================
# 2. INITIALIZE USER DATA
# ==========================================

user_name = None


# ==========================================
# 3. MAIN CHATBOT LOOP
# ==========================================

while True:

    # Get user input and normalize it
    user_input = input("\nYou: ").strip().lower()

    # Remove punctuation
    user_input = user_input.translate(
        str.maketrans("", "", string.punctuation)
    )


    # ======================================
    # 4. HANDLE USER MESSAGES
    # ======================================

    # Greeting responses
    if user_input in ["hello", "hi", "hey"]:
        print("Bot: Hello! How can I help you?")

    # How are you responses
    elif user_input in ["how are you", "how are you doing"]:
        print("Bot: I'm doing great! Thanks for asking.")

    # Chatbot identity
    elif user_input in [
        "what is your name",
        "whats your name",
        "who are you"
    ]:
        print("Bot: My name is Python Chatbot. I'm a simple rule-based chatbot.")

    # Asking about user's name
    elif user_input in [
        "do you know my name",
        "do yo know my name",
        "what is my name",
        "whats my name"
    ]:
        if user_name:
            print(f"Bot: Your name is {user_name.title()}.")
        else:
            print("Bot: I don't know your name yet. Please introduce yourself.")

    # Thank you responses
    elif user_input in ["thanks", "thank you", "thankyou"]:
        print("Bot: You're welcome!")

    # Help command
    elif user_input == "help":
        print("Bot: You can:")
        print("- Greet me")
        print("- Ask me how I am")
        print("- Ask my name")
        print("- Tell me your name")
        print("- Ask me to remember your name")
        print("- Type 'exit' to end the conversation")

    # Remember user's name
    elif "my name is " in user_input:
        user_name = user_input.split("my name is ", 1)[1].strip()

        if user_name:
            print(f"Bot: Nice to meet you, {user_name.title()}!")
        else:
            print("Bot: Please tell me your name.")

    # Exit chatbot
    elif user_input in ["exit", "quit", "bye"]:
        print("Bot: Goodbye!")
        break

    # Default response
    else:
        print("Bot: Sorry, I didn't understand that. Please try again.")


# ==========================================
# 5. END OF CHATBOT
# ==========================================
