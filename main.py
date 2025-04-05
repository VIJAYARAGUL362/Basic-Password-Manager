from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_maker():
    """Generate a Random password"""
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)


    password_list = [random.choice(letters) for _ in range(nr_letters)]

    password_list += [random.choice(symbols) for _ in range(nr_symbols)]

    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)
    input_box_3.insert(0,password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_name = input_box_1.get()
    gmail = input_box_2.get()
    password_field = input_box_3.get()


    if len(password_field) != 0 and len(website_name) != 0:

        is_ok = messagebox.askokcancel(title=f"{website_name}",message=f"The website name is {website_name}\n "
                                                               f"The password is {password_field}\n"
                                                                       f"Do you want to save?")
        if is_ok:
            with open(file="Password_manager.text", mode="a") as file:
                file.write(f"{website_name} | {password_field} | {gmail}\n")
                delete()
    else:
        if len(password_field) == 0:
            problem = "password"
        elif len(website_name) == 0:
            problem = "website"
        else:
            problem = "password and website name"

        messagebox.showerror(title="Missing Fields",message=f"{problem} must contain some value")


# ---------------------------- UI SETUP ------------------------------- #

windows = Tk()
windows.config(padx=50,pady=50)
email_list = [None]
count = 0

def delete():
    input_box_1.delete(0,END)
    input_box_3.delete(0, END)
    input_box_1.focus()


# LOGO
photo = PhotoImage(file="logo.png")
canvas = Canvas(height=200,width=200,highlightthickness=0)
canvas.create_image(100,100,image = photo)
canvas.grid(row =0,column = 1)

# Label1
label1 = Label(text="Website:")
label1.grid(row =1,column = 0)

# Label2
label2 = Label(text="Email/Username:")
label2.grid(row =2,column = 0)

# Label 3
label3 = Label(text="Password:")
label3.grid(row =3,column = 0)


# Input box
input_box_1 = Entry(width=35)
input_box_1.grid(row = 1,column = 1,columnspan = 2)
input_box_1.focus()

# Input box
input_box_2 = Entry(width=35)
input_box_2.grid(row =2,column = 1,columnspan =2 )

# Input box
input_box_3 = Entry(width=21)
input_box_3.grid(row =3,column = 1)
if email_list[0] is None:
    email_list[0] = input_box_3.get()
if input_box_3.get() is not None:
    input_box_3.insert(0,f"{input_box_3.get()}")
    if input_box_3.get() != email_list[count]:
        email_list.append(input_box_3.get())
        count += 1
        print(email_list)


button1 = Button(text="Generate Password",command=password_maker)
button1.grid(row =3,column = 2)

# Button
button2 = Button(text ="Add",width=36,command=save)
button2.grid(row =4,column = 1)


windows.mainloop()