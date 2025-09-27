import random
import datetime

# Motivational quotes database
quotes = [
    "Believe in yourself and all that you are. 🌟",
    "Every day is a new chance to grow. 🌱",
    "Success is the sum of small efforts repeated daily. 💪",
    "Your future is created by what you do today, not tomorrow. 🔥",
    "Dream big, work hard, stay focused. 🚀",
    "Happiness depends upon ourselves. 😊",
    "Challenges are what make life interesting. 🌍",
    "Keep going, you’re closer than you think. 🏆",
    "Turn your wounds into wisdom. 📖",
    "You are stronger than you know. 🐯"
]

# Daily affirmations generator
affirmations = [
    "I am capable of achieving great things. 🌠",
    "I radiate positivity and confidence. 🌞",
    "I am grateful for today and all it brings. 🍀",
    "I focus on progress, not perfection. 🏗️",
    "I am calm, patient, and in control. 🌊",
    "I trust the process of life. 🌀"
]

def show_menu():
    print("\n=== MOTIVATIONAL APP ===")
    print("1. Get a random motivational quote")
    print("2. Get today’s affirmation")
    print("3. Exit")

def get_quote():
    return random.choice(quotes)

def get_affirmation():
    today = datetime.date.today().day
    return affirmations[today % len(affirmations)]

# Main app loop
while True:
    show_menu()
    choice = input("Choose an option (1-3): ")
    
    if choice == "1":
        print("\n💡 Quote: ", get_quote())
    elif choice == "2":
        print("\n🌞 Today’s Affirmation: ", get_affirmation())
    elif choice == "3":
        print("\nThanks for using the Motivational App! Keep shining ✨")
        break
    else:
        print("\n⚠️ Invalid choice, please try again.")
