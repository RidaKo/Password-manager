from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
screen = Canvas()
manager = Grid()
window.title("Ortaria(password vesrion)")
window.minsize(width=300, height=300)
window.config(padx=50, pady=50)

window.grid(widthInc=100 , heightInc=100)
window.columnconfigure(3)
window.rowconfigure(3)


# Canvas creation
canvas = Canvas(window)
canvas.grid(column=1, row=0,pady=20 ,sticky = "W")
canvas.config(height=200, width=200, background='gray')
# create an image
my_photo = PhotoImage(file= "E:\Git\password-manager-start\logo.png")
canvas.create_image(100,100, image = my_photo)

# labels
website_label = Label(text="Website", font='Helvetica 11 bold')
user_label = Label(text="Email/Username",font='Helvetica 11 bold')
password_label = Label(text="Password",font='Helvetica 11 bold')

# entries
website_entry = Entry(width=55)
user_entry = Entry(width=55)
password_entry = Entry(width=35)

# buttons
gen_password_button = Button(text="Generate Password", width=16)
add_button = Button(text="Add" ,width=47)

# Grid everything
website_label.grid(column=0, row=1)
user_label.grid(column=0, row=2)
password_label.grid(column=0, row=3)

website_entry.grid(column=1, row=1, columnspan=2,sticky = "W")
user_entry.grid(column=1, row=2, columnspan=2,sticky = "W")
password_entry.grid(column=1, row=3,sticky = "W")

gen_password_button.grid(column=2, row=3, sticky="W")
add_button.grid(column=1, row=4, columnspan=2 ,sticky="W")


window.mainloop()