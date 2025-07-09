import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import messagebox
import random

class GuessingGameApp(tb.Window):
    def __init__(self):
        super().__init__(themename="solar")  # Bright modern theme
        self.title("🎯 Guess the Number")
        self.geometry("400x400")
        self.target = random.randint(1, 100)
        self.create_widgets()

    def create_widgets(self):
        tb.Label(self, text="Guess the Number Game", font=("Helvetica", 18), bootstyle="danger").pack(pady=20)
        tb.Label(self, text="I'm thinking of a number between 1 and 100...", font=("Helvetica", 11)).pack(pady=10)

        self.guess_entry = tb.Entry(self, font=("Helvetica", 12), bootstyle="primary")
        self.guess_entry.pack(pady=10, ipadx=10, ipady=5)

        tb.Button(self, text="Submit Guess", command=self.check_guess, bootstyle="success").pack(pady=10)

        self.result_label = tb.Label(self, text="", font=("Helvetica", 14), bootstyle="warning")
        self.result_label.pack(pady=20)

        tb.Button(self, text="Restart Game", command=self.restart_game, bootstyle="secondary-outline").pack(pady=10)

    def check_guess(self):
        try:
            guess = int(self.guess_entry.get())
            print("User's guess :", guess, "\nTarget Answer :", self.target)
            if guess < self.target:
                self.result_label.config(text="Too low! Try again.")
                
            elif guess > self.target:
                self.result_label.config(text="Too high! Try again.")
            else:
                self.result_label.config(text=f"🎉 Correct! It was {self.target}")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number.")

    def restart_game(self):
        self.target = random.randint(1, 100)
        self.result_label.config(text="")
        self.guess_entry.delete(0, 'end')

if __name__ == "__main__":
    app = GuessingGameApp()
    app.mainloop()
