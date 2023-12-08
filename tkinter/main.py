import tkinter

window = tkinter.Tk()
window.title("Hashib First GUI")
window.minsize(width=500, height=300)

my_label = tkinter.Label(text="Hashib Raja First GUI",
                         font=("Arial", 24, "bold"))
my_label.pack()


window.mainloop()
