import tkinter as tk

window = tk.Tk()
window.title('Km to Mile Converter')
window.minsize(500, 300)

label = tk.Label(window, text="I'm a label", fg="red", font=("Arial", 20, 'bold'))
label.pack()


window.mainloop()