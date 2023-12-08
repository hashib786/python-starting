from tkinter import *

window = Tk()
window.title("Hashib First GUI")
window.minsize(width=500, height=300)

my_label = Label(text="Hashib Raja First GUI",
                 font=("Arial", 24, "bold"))
my_label.pack()

# Buttons ************


def button_click():
    # my_label["text"] = "Button Pressed" if my_label["text"] == "Hashib Raja First GUI" else "Hashib Raja First GUI"
    my_label.config(text=input.get())


button = Button(text="Add", command=button_click)
button.pack()

# Inputs ************
input = Entry(width=10)
input.pack()

window.mainloop()
