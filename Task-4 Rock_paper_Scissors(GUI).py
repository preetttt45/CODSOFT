import tkinter as tk
import random

# Create the main window
root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("400x500")
root.resizable(False, False)
root.configure(bg="#f0f8ff")  # Light background color

# Game variables
player_score = 0
computer_score = 0
round_number = 0
options = ["Rock", "Paper", "Scissors"]

# Function that runs when player makes a move
def play_round(player_choice):
    global player_score, computer_score, round_number

    # Randomly choose computer's move
    computer_choice = random.choice(options)

    # Show both choices
    result_text.set(f"You chose: {player_choice}\nComputer chose: {computer_choice}")

    # Determine the winner
    if player_choice == computer_choice:
        outcome = "It's a draw!"
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Scissors" and computer_choice == "Paper") or \
         (player_choice == "Paper" and computer_choice == "Rock"):
        outcome = "You win this round!"
        player_score += 1
    else:
        outcome = "Computer wins this round!"
        computer_score += 1

    # Increase round count
    round_number += 1

    # Update the result display
    result_text.set(result_text.get() + f"\n{outcome}")

    # Update the score label
    score_label.config(
        text=f"Score - You: {player_score} | Computer: {computer_score} | Round: {round_number}"
    )

# Function to quit the app
def exit_game():
    root.destroy()

# ---- GUI Layout ----

# Game title
title_label = tk.Label(root, text="Rock Paper Scissors", font=("Helvetica", 18, "bold"), bg="#f0f8ff")
title_label.pack(pady=20)

# Variable to show results in real time
result_text = tk.StringVar()
result_text.set("Make your move!")  # Default text before game starts

# Label that shows the result and choices
result_label = tk.Label(root, textvariable=result_text, font=("Arial", 12), bg="#f0f8ff", justify="center")
result_label.pack(pady=30)

# Frame to hold buttons
button_frame = tk.Frame(root, bg="#f0f8ff")
button_frame.pack()

# Rock button
rock_btn = tk.Button(button_frame, text="🪨 Rock", width=10, height=2, command=lambda: play_round("Rock"))
rock_btn.grid(row=0, column=0, padx=10)

# Paper button
paper_btn = tk.Button(button_frame, text="📄 Paper", width=10, height=2, command=lambda: play_round("Paper"))
paper_btn.grid(row=0, column=1, padx=10)

# Scissors button
scissors_btn = tk.Button(button_frame, text="✂️ Scissors", width=10, height=2, command=lambda: play_round("Scissors"))
scissors_btn.grid(row=0, column=2, padx=10)

# Label to show the ongoing score
score_label = tk.Label(root, text="Score - You: 0 | Computer: 0 | Round: 0", font=("Arial", 11), bg="#f0f8ff")
score_label.pack(pady=20)

# Exit button to close the app
exit_button = tk.Button(root, text="Exit Game", command=exit_game, bg="red", fg="white", width=15)
exit_button.pack(pady=10)

# Run the GUI app
root.mainloop()