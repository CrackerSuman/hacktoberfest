import time
import random

# Define messages
good_morning_messages = [
    "Good morning, my love! 😊",
    "Rise and shine, beautiful! 🌞",
    "Wishing you a fantastic morning! ❤️",
]

good_night_messages = [
    "Good night, sweetheart! 🌙",
    "Sweet dreams, my love! 😴",
    "Sending you a hug through the night! 🌠",
]

# Function to send messages
def send_message(messages):
    message = random.choice(messages)
    print(message)  # Replace with your code to send the message to your girlfriend

# Schedule good morning and good night messages
while True:
    current_time = time.localtime()
    if current_time.tm_hour == 8 and current_time.tm_min == 0:
        send_message(good_morning_messages)
    elif current_time.tm_hour == 22 and current_time.tm_min == 0:
        send_message(good_night_messages)
    time.sleep(60)  # Check the time every minute
