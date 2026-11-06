# Name: Syed Haris Hussain Shah
# Internship ID: B9_2265
# Task 4: Rule-Based Chatbot

print("=" * 40)
print("       Welcome to Python Chatbot")
print("=" * 40)

print("Bot: Hello! I am your Python chatbot.")
print("Bot: You can chat with me. Type 'exit' to quit.")

while True:

    # Get user input
    user_input = input("\nYou: ")

    # Normalize user input
    user_input = user_input.strip().lower()

    # Exit condition
    if user_input in ["exit", "quit", "bye"]:
        print("Bot: Goodbye! Have a great day.")
        break

    # Basic response
    elif user_input == "":
        print("Bot: Please enter something.")

    else:
        print("Bot: I am still learning. I don't understand that yet.")
