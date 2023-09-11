from tkinter import *
import random

RED = "#e7305b"
PURPLE = "#9000a0"
YELLOW = "#ffffe0"
BLACK = "#000000"
FONT_NAME = "Courier"

def generate_password():
   
    password_field.delete(1, 99999999)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&',  '*', '+']

    nr_letters = int(letter_input.get())
    nr_symbols = int(symbols_input.get())
    nr_numbers = int(number_input.get())

    password = []

    for letter in range(nr_letters):
        password += random.choice(letters)

    for symbol in range(nr_symbols):
        password += random.choice(symbols)

    for letter in range(nr_numbers):
        password += random.choice(numbers)

    random.shuffle(password)

    new_pass = ""

    for char in password:
        new_pass += char

    password_field.insert(index=0, string=new_pass)

window = Tk()

title_label = Label(text="Welcome To My Password Generator!", bg=YELLOW, fg=PURPLE, font=(FONT_NAME, 45))
title_label.pack()

letter_label = Label(text="1.How many letters do you want in your password?", bg=YELLOW, fg=BLACK, font=(FONT_NAME,
                                                                                                             20))
letter_label.place(x=10, y=100)

letter_input = Spinbox(from_=0, to=20, width=10, font=(FONT_NAME, 20))
letter_input.place(x=800, y=100)

symbols_label = Label(text="2. How many symbols would you like?", bg=YELLOW, fg=BLACK, font=(FONT_NAME, 20))
symbols_label.place(x=10, y=150)

symbols_input = Spinbox(from_=0, to=20, width=10, font=(FONT_NAME, 20))
symbols_input.place(x=800, y=150)

number_label = Label(text="3. How many numbers would you like?", bg=YELLOW, fg=BLACK, font=(FONT_NAME, 20))
number_label.place(x=10, y=200)

number_input = Spinbox(from_=0, to=20, width=10, font=(FONT_NAME, 20))
number_input.place(x=800, y=200)

generate_button = Button(text="Generate", bg="#5bafee", font=(FONT_NAME, 20), command=generate_password)
generate_button.pack(pady=200)

password_field = Entry(width=42, font=(FONT_NAME, 30), fg=RED)
password_field.place(x=10, y=350)

window.title("Password_Generator App")
window.config(padx=100, pady=50, bg=YELLOW)
window.geometry("+270+100")
window.minsize(width=270, height=300)
window.resizable(False, False)

window.mainloop()