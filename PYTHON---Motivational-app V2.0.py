import random
import datetime

# --- DATABASE UPGRADES ---

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

affirmations = [
    "I am capable of achieving great things. 🌠",
    "I radiate positivity and confidence. 🌞",
    "I am grateful for today and all it brings. 🍀",
    "I focus on progress, not perfection. 🏗️",
    "I am calm, patient, and in control. 🌊",
    "I trust the process of life. 🌀"
]

# New data for your specific interests
vegan_tips = [
    "Fuel your brain with omega-3s from flax or chia seeds today. 🧠",
    "Try a new seasonal vegetable in your meal tonight. 🥬",
    "Remember: a plant-based diet is a gift to your body and the planet. 🌎",
    "Stay hydrated! Infuse your water with cucumber or mint for a fresh kick. 💧"
]

business_insights = [
    "Don't busy-fill your day; focus on the high-leverage tasks. 📈",
    "Your network is your net worth. Reach out to one person today. 🤝",
    "Systematize one repetitive task to buy back your time. ⚙️",
    "The best way to predict the future is to create it. 🏗️"
]

nature_breaks = [
    "Step outside and take five deep breaths of fresh air. 🌳",
    "Find a piece of nature (a tree, a bird, a cloud) and observe it for 60 seconds. ☁️",
    "Walk barefoot on the grass if you can—get grounded. 👣",
    "Notice the patterns in a leaf; nature's design is perfect. 🍂"
]

# --- FUNCTIONS ---

def show_menu():
    """Displays the interactive menu options to the user."""
    print("\n=== THE WELL-ROUNDED APP ===")
    print("1. Get a random motivational quote")
    print("2. Get today’s affirmation")
    print("3. Get a healthy vegan tip")
    print("4. Get a business mindset insight")
    print("5. Nature connection task")
    print("6. Log a quick gratitude note")
    print("7. Exit")

def get_quote():
    """Selects and returns a random string from the quotes list."""
    return random.choice(quotes)

def get_affirmation():
    """Uses the current day of the month to provide a consistent daily affirmation."""
    today = datetime.date.today().day
    return affirmations[today % len(affirmations)]

def get_vegan_health_tip():
    """Returns a random tip focused on vegan nutrition and wellness."""
    return random.choice(vegan_tips)

def get_business_tip():
    """Provides a productivity or strategy-focused tip for the business-minded."""
    return random.choice(business_insights)

def get_nature_task():
    """Suggests a small, actionable task to reconnect with the natural world."""
    return random.choice(nature_breaks)

def log_gratitude():
    """Allows the user to type a gratitude note and 'saves' it for the session."""
    note = input("\nWhat are you grateful for right now (family, health, a win)? ")
    print(f"✨ Note saved: '{note}' - Focusing on gratitude changes your vibration.")

# --- MAIN APP LOOP ---

while True:
    show_menu()
    choice = input("\nChoose an option (1-7): ")
    
    if choice == "1":
        print("\n💡 Quote: ", get_quote())
    elif choice == "2":
        print("\n🌞 Today’s Affirmation: ", get_affirmation())
    elif choice == "3":
        print("\n🥦 Vegan Health Tip: ", get_vegan_health_tip())
    elif choice == "4":
        print("\n💼 Business Insight: ", get_business_tip())
    elif choice == "5":
        print("\n🌲 Nature Break: ", get_nature_task())
    elif choice == "6":
        log_gratitude()
    elif choice == "7":
        print("\nThanks for using the App! Have a grounded and productive day. ✨")
        break
    else:
        print("\n⚠️ Invalid choice, please try again.")
