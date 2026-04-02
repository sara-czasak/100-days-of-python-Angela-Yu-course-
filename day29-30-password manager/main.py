from tkinter import *
from tkinter import messagebox
from brain import *


# Button functions
def save_password_data():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    if website == "" or username == "" or password == "":
        messagebox.showerror(title="Error", message="Please fill all fields")
    else:
        confirm = messagebox.askquestion(title="Check", message=f"Please confirm data: \nWebsite: {website}\nUsername: {username}\nPassword: {password}")
        if confirm == "yes":
            save_password(website, username, password)
            messagebox.showinfo("Password Saved!", "Password has been successfully saved!")
            website_entry.delete(0, END)
            username_entry.delete(0, END)
            password_entry.delete(0, END)


def make_password():
    passsword = create_password()
    password_entry.delete(0, END)
    password_entry.insert(END, passsword)

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
website_entry = Entry(window)
website_entry.focus()
website_entry.grid(row=1, column=1)
search_button = Button(window, text="Search", width=15)
search_button.grid(row=1, column=2, padx=1, pady=5)

username_label = Label(window, text="Email/Username:")
username_label.grid(row=2, column=0)
username_entry = Entry(window, width=42)
username_entry.grid(row=2, column=1, columnspan=2, padx=5, pady=5)

password_label = Label(window, text="Password:")
password_label.grid(row=3, column=0)
password_entry = Entry(window)
password_entry.grid(row=3, column=1)
generate_button = Button(text='Generate Password', command=make_password, width=15)
generate_button.grid(row=3, column=2, padx=1, pady=5)

add_button = Button(window, text='Add', width=35, command=save_password_data)
add_button.grid(row=4, column=1, columnspan=2, padx=5, pady=5)


window.mainloop()