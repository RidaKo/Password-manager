from tkinter import *
from tkinter import messagebox
from pass_gen import make_pass
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def create_password() -> None:
    password = make_pass()
    password_entry.delete(first=0, last=len(password_entry.get()))
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
#site: str, user: str, psw: str
def save() ->None:
    site, user, psw = get_strings()
    if len(site) ==0 or len(psw)==0:
        messagebox.askretrycancel(title="Oops", message=f"Please don't leave any fields empty!")
    else:    
        confirmation = messagebox.askokcancel(title=site, message=f"These are the details you have entered:\n"
        f" Email: {user}\n Pasword: {psw}\n Do you wish to continue?")
        if confirmation == True:
            with open("data.txt", "a") as data:
                data.write(f"{site} | {user} | {psw} \n")
            website_entry.delete(0 ,END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

password = ""


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
canvas.config(height=200, width=200)
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

website_entry.focus()
user_entry.insert(0, "email@gmail.com")

# Taking out the strings
def get_strings():

    site = website_entry.get()
    user = user_entry.get()
    psw = password_entry.get()
    return site, user, psw


# Configuring button commands
add_button.config(command=save)
gen_password_button.config(command=create_password)

window.mainloop()