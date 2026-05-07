import datetime
import random

def chatbot():
    print("🤖 Hello! I am your Personal Chatbot")
    name = input("🤖 What's your name? ")

    print(f"🤖 Nice to meet you, {name}!")
    print("🤖 Type 'help' to see what I can do.")
    print("🤖 Type 'bye' to exit.\n")

    while True:
        user = input(f"{name}: ").lower()

        # Greetings
        if user in ["hi", "hello", "hey", "hii"]:
            print("🤖 Hello! How can I help you?")

        # Creator
        elif "creator" in user or "who made you" in user:
            print("🤖 I was created using Python by a subbarao.")

        # Name
        elif "your name" in user:
            print("🤖 I am a Personal Python Chatbot.")

        # Purpose
        elif "why are you created" in user or "your purpose" in user:
            print("🤖 My purpose is to help, chat, and assist users.")

        # Features
        elif "features" in user or "what can you do" in user:
            print("🤖 I can:")
            print("   - Chat with you")
            print("   - Tell time and date")
            print("   - Motivate you")
            print("   - Tell jokes")
            print("   - Help in studies")

        # Time
        elif "time" in user:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"🤖 Current time is {time}")

        # Date
        elif "date" in user:
            date = datetime.datetime.now().strftime("%d-%m-%Y")
            print(f"🤖 Today's date is {date}")

        # Day
        elif "day" in user:
            day = datetime.datetime.now().strftime("%A")
            print(f"🤖 Today is {day}")

        # How are you
        elif "how are you" in user:
            print("🤖 I'm doing great! Thanks for asking 😊")

        # User feeling
        elif "i am sad" in user or "i feel sad" in user:
            print("🤖 Don't worry. Tough times never last 💪")

        elif "i am happy" in user:
            print("🤖 That's awesome! Keep smiling 😄")

        # Motivation
        elif "motivate" in user or "motivation" in user:
            print("🤖 Believe in yourself. You are stronger than you think!")

        # Jokes
        elif "joke" in user:
            jokes = [
                "Why do programmers prefer dark mode? Because light attracts bugs 😂",
                "Why was the computer cold? It forgot to close Windows 😂",
                "Why did Python break up with Java? Too many classes 😂"
            ]
            print("🤖 " + random.choice(jokes))

        # Study help
        elif "study" in user or "exam" in user:
            print("🤖 Stay focused, revise regularly, and practice daily.")

        # Programming
        elif "python" in user:
            print("🤖 Python is a powerful, easy-to-learn programming language.")

        elif "java" in user:
            print("🤖 Java is an object-oriented programming language.")

        # System info
        elif "are you human" in user:
            print("🤖 No, I am a software program.")

        elif "are you robot" in user:
            print("🤖 I am a virtual chatbot, not a physical robot.")

        # Thanks
        elif "thank" in user:
            print("🤖 You're welcome 😊")

        # Help
        elif "help" in user:
            print("🤖 You can ask me about:")
            print("   - My creator")
            print("   - Time / Date")
            print("   - Motivation")
            print("   - Jokes")
            print("   - Programming")
            print("   - Studies")

        # Exit
        elif user in ["bye", "exit", "quit"]:
            print(f"🤖 Do One Thing {name}! Have a great day 👋")
            break

        # Unknown
        else:
            print("🤖 Sorry, I didn't understand that.")

# Run chatbot
chatbot()
