import string
import random


# Save password to file
def save_password(website, username, password):
    with open('password_data.txt', 'a') as file:
        file.write(f"{website} | {username} | {password}\n")


# Generate password
def create_password():
    uppercase = random.choices(string.ascii_uppercase, k=3)
    lowercase = random.choices(string.ascii_lowercase, k=5)
    digits = random.choices(string.digits, k=3)
    symbols = random.choices(string.punctuation, k=1)

    password = uppercase + lowercase + digits + symbols
    for i in range(10):
        password = "".join(random.sample(password, len(password)))
    return password