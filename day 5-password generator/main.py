# Password generator

import random
import string

print("*** WELCOME TO THE SECURE PASSWORD GENERATOR ***")
print("Please answer the following questions:")
letters = int(input("How many letters do you want your password to contain?\n"))
numbers = int(input("How many numbers do you want your password to contain?\n"))
special_chars = int(input("How many special characters do you want your password to contain?\n"))

uppercase = random.choices(string.ascii_uppercase, k=2)
lowercase = random.choices(string.ascii_lowercase, k=letters-2)
digits = random.choices(string.digits, k=numbers)
symbols = random.choices(string.punctuation, k=special_chars)

password = uppercase + lowercase + digits + symbols
for i in range(10):
    password = "".join(random.sample(password, len(password)))

print(f"Your new secure password is: {password}")