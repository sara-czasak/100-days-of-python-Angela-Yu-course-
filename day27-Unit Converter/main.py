from tkinter import *


def convert():
    kilometers = int(miles.get()) * 1.6
    km['text'] = str(kilometers)


window = Tk()
window.title('Km to Mile Converter')
window.minsize(200, 100)

miles = Entry(window)
miles.grid(row=0, column=1, padx=10, pady=10)

miles_label = Label(window, text="Miles")
miles_label.grid(row=0, column=2, padx=10, pady=10)

equal_label = Label(window, text="is equal to")
equal_label.grid(row=1, column=0, padx=10)

km = Label(window, text="0")
km.grid(row=1, column=1)

km_label = Label(window, text="Km")
km_label.grid(row=1, column=2)

button = Button(window, text="Convert", command=convert)
button.grid(row=2, column=1)

window.mainloop()