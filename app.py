import sys
import random

# Rule-based response mapping
CHAT_RESPONSES = {
    "hello": ["Hello! How can I help you today?", "Hi there! What's on your mind?", "Greetings!"],
    "how are you": ["I'm doing great, thank you! How are you?", "Operational and ready to chat!", "Doing well, thank you."],
    "what is your name": ["I am ChatbotAI, your friendly console companion.", "They call me ChatbotAI."],
    "bye": ["Goodbye! Have a nice day.", "See you later!", "Farewell!"],
    "help": ["I can answer basic queries, converse with you, or tell jokes. Try typing 'tell me a joke'!"]
}

JOKES = [
    "Why do programmers wear glasses? Because they can't C#!",
    "How many programmers does it take to change a light bulb? None, that's a hardware problem.",
    "There are 10 types of people: those who understand binary, and those who don't."
]

def get_response(msg):
    msg_clean = msg.lower().strip().replace("?", "").replace("!", "")
    if "joke" in msg_clean:
        return random.choice(JOKES)
    for key, responses in CHAT_RESPONSES.items():
        if key in msg_clean:
            return random.choice(responses)
    return "I'm not sure I understand that. Type 'help' to see what I can do!"

def main():
    print("--- ChatbotAI CLI Assistant ---")
    print("Type 'bye' to exit the chat.")
    print("-" * 40)
    
    while True:
        msg = input("You: ").strip()
        if msg.lower() == 'bye':
            print("Bot: Goodbye!")
            sys.exit(0)
        if not msg:
            continue
        response = get_response(msg)
        print(f"Bot: {response}")

if __name__ == "__main__":
    main()
