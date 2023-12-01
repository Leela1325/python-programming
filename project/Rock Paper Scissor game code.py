import tkinter as tk
import random

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors Game")

        self.result_label = tk.Label(root, text="", font=("Helvetica", 16))
        self.result_label.pack(pady=40)

        self.player_hand_label = tk.Label(root, font=("Arial", 40))
        self.computer_hand_label = tk.Label(root, font=("Arial", 40))

        rock_button = tk.Button(root, text="✊ Rock", command=lambda: self.play("rock"))
        paper_button = tk.Button(root, text="✋ Paper", command=lambda: self.play("paper"))
        scissors_button = tk.Button(root, text="✌ Scissors", command=lambda: self.play("scissors"))

        rock_button.pack(side=tk.LEFT, padx=100)
        paper_button.pack(side=tk.LEFT, padx=100)
        scissors_button.pack(side=tk.LEFT, padx=100)

    def play(self, player_choice):
        choices = ["rock", "paper", "scissors"]
        computer_choice = random.choice(choices)

        self.display_hand(player_choice, self.player_hand_label, "Your Choice:")
        self.display_hand(computer_choice, self.computer_hand_label, "Computer's Choice:")

        if player_choice == computer_choice:
            result = "It's a tie!"
        elif (
            (player_choice == "rock" and computer_choice == "scissors")
            or (player_choice == "paper" and computer_choice == "rock")
            or (player_choice == "scissors" and computer_choice == "paper")
        ):
            result = "You win!"
        else:
            result = "You lose!"

        self.result_label.config(text=result)

    def display_hand(self, choice, label, title):
        hand_emojis = {
            "rock": "✊",
            "paper": "✋",
            "scissors": "✌",
        }

        hand_emoji = hand_emojis.get(choice, "")
        label.config(text=f"{title} {hand_emoji}")
        label.pack(pady=40)

if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()
