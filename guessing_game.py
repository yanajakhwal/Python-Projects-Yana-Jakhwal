## Guessing-Game
##    Generates a random number between 1 and 100, tracks user attempts, and provides feedback on whether the guessed number is 
##    greater or smaller. Utilizes global variables for game state management, including the secret number and the number of attempts.

import random
import tkinter as tk

def new_game():
    global secret_number, attempts
    secret_number = random.randint(1, 100)
    attempts = 0
    output_label.config(text="Welcome to the Number Guessing Game!\nI have chosen a number between 1 and 100.")
    submit_button.config(state="active")
    entry_guess.config(state="normal")
    attempts_label.config(text="Trials: 0", fg="red")
    root.config(bg="gray")

def check_guess():
    global attempts
    guess = int(entry_guess.get())
    attempts += 1
    attempts_label.config(text=f"Trials: {attempts}")
    if guess < secret_number:
        output_label.config("The number is greater.")
    elif guess > secret_number:
        output_label.config("The number is smaller.")
    else:
        output_label.config(text=f"Congratulations! You guessed the {secret_number} in {attempts} attempts!")
        submit_button.config(state="disabled")
        entry_guess.config(state="disabled")

root = tk.Tk()
root.title("The Number Guessing Game")

secret_number = None
attempts = 0

output_label = tk.Label(root, text="", pady=10)
entry_guess = tk.Entry(root, state="disabled")
submit_button = tk.Button(root, text="Submit", command=check_guess, state="disabled")
new_game_button = tk.Button(root, text="New Game", command=new_game)
attempts_label = tk.Label(root, text="Trials: 0")

output_label.pack()
entry_guess.pack()
submit_button.pack()
attempts_label.pack()
new_game_button.pack()

new_game()

root.mainloop()
