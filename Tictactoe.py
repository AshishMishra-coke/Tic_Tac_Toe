# This is a simple Tic-Tac-Toe game implemented using Tkinter in Python GUI based.
import tkinter as tk
from tkinter import messagebox

def check_winner():
    global winner
    # These are the 8 ways to win
    for combo in [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]:
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] != "":
            # Highlight winning buttons
            for i in combo:
                buttons[i].config(bg="Green") 
            
            winner = False
            messagebox.showinfo("Tic-Tac-Toe", f"Player {buttons[combo[0]]['text']} Wins!")
            root.destroy() # Using destroy is cleaner than quit() for closing the window

def button_click(index):
    if buttons[index]["text"] == "" and not winner:
        buttons[index]["text"] = current_player
        check_winner()
        if not winner:
            toggle_player()

def toggle_player():
    global current_player
    current_player = "O" if current_player == "X" else "X"
    label.config(text=f"Player {current_player}'s turn")


root = tk.Tk() 
root.title("Tic-Tac-Toe")

winner = False
current_player = "X"

# Capital 'B' in Button and passed 'root' as parent B is always written in capital letter and root is the parent window for all the buttons
buttons = [tk.Button(root, text="", font=("Arial", 20), width=5, height=2, 
                     command=lambda i=i: button_click(i)) for i in range(9)]


for i, button in enumerate(buttons):
    button.grid(row=i//3, column=i%3)

#  Capital 'L' in Label we have consider it all the time
label = tk.Label(root, text=f"Player {current_player}'s turn", font=("Arial", 15))
label.grid(row=3, column=0, columnspan=3)

root.mainloop()