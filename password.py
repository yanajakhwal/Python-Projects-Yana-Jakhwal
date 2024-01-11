## Password Generator
##    A user-friendly graphical interface allowing users to input the desired password length. 
##    Includes error handling to ensure the password length is at least 6 characters. 
##    The application outputs the generated password on the Tkinter window, providing an easy 
##    and convenient tool for creating strong passwords.

import string
import tkinter as tk
import random

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_password_interface():
    password_length = int(entry_length.get())

    if password_length < 6:
        label_result.config(text="Password length must be at least 6 characters.")
    else:
        generated_password = generate_password(password_length)
        label_result.config(text="Generated Password:\n" + generated_password)

root = tk.Tk()
root.title("Password Generator")

label_length = tk.Label(root, text="Enter the desired password length: ")
label_length.pack()

entry_length = tk.Entry(root)
entry_length.pack()

button_generate = tk.Button(root, text="Generate Password", command=generate_password_interface)
button_generate.pack()

label_result = tk.Label(root, text="")
label_result.pack()

root.mainloop()
