from tkinter import *
from brain import *


# Button functions
def save_password_data():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    save_password(website, username, password)


# UI
window = Tk()
window.title("* Password Manager *")
window.config(padx=20, pady=20)

logo = Canvas(window, width=200, height=200)
logo_img = PhotoImage(file='./logo.png')
logo.create_image(100, 100, image=logo_img)
logo.grid(row=0, column=0, columnspan=3, padx=20, pady=20)

website_label = Label(window, text="Website:")
website_label.grid(row=1, column=0)
website_entry = Entry(window, width=42)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2, padx=5, pady=5)

username_label = Label(window, text="Email/Username:")
username_label.grid(row=2, column=0)
username_entry = Entry(window, width=42)
username_entry.grid(row=2, column=1, columnspan=2, padx=5, pady=5)

password_label = Label(window, text="Password:")
password_label.grid(row=3, column=0)
password_entry = Entry(window)
password_entry.grid(row=3, column=1)
generate_button = Button(text='Generate Password')
generate_button.grid(row=3, column=2, padx=1, pady=5)

add_button = Button(window, text='Add', width=35, command=save_password_data)
add_button.grid(row=4, column=1, columnspan=2, padx=5, pady=5)


window.mainloop()