# Save password to file
def save_password(website, username, password):
    with open('password_data.txt', 'a') as file:
        file.write(f"{website} | {username} | {password}\n")