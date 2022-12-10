from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
screen = Canvas()
manager = Grid()
window.title("Widget Examples")
window.minsize(width=300, height=300)
window.config(padx=20, pady=20)


window.grid(widthInc=100 ,heightInc=100)
window.columnconfigure(3)
window.rowconfigure(3)



canvas = Canvas(window)
canvas.grid(column=2, row=2, padx=20, pady=20)
canvas.config(height=200, width=200)
my_photo = PhotoImage(file= "E:\Git\password-manager-start\logo.png")
canvas.create_image(100,100, image = my_photo)

# label = Label(image=my_photo)
# label.grid(column=2, row=2)

window.mainloop()