import string
import random
import pyperclip
import json


# Save password to file
def save_password(website, username, password):
    data = {
        website: {
            "username": username,
            "password": password,
        }
    }
    with open('password_data.json', 'w') as file:
        json.dump(data, file, indent=4)


# Generate password
def create_password():
    uppercase = random.choices(string.ascii_uppercase, k=3)
    lowercase = random.choices(string.ascii_lowercase, k=5)
    digits = random.choices(string.digits, k=3)
    symbols = random.choices(string.punctuation, k=1)

    password = uppercase + lowercase + digits + symbols
    for i in range(10):
        password = "".join(random.sample(password, len(password)))
        pyperclip.copy(password)
    return password


def search_password(website):
    with open('password_data.json', 'r') as file:
        data = json.load(file)
        if website in data:
            return data[website]
        else:
            return None