# Tic_Tac_Toe
"A sleek, GUI-based Tic-Tac-Toe game built with Python and Tkinter. Featuring dynamic win-detection logic, real-time player switching, and a responsive grid layout. This project demonstrates clean event-driven programming and state management in a desktop environment."
🎮 Tic-Tac-Toe GUI (Python)
A fully functional, interactive Tic-Tac-Toe game built with a Graphical User Interface (GUI). This project demonstrates the implementation of game logic, state management, and event-driven programming using Python’s Tkinter library.

✨ Features
Intuitive GUI: A clean 3x3 grid interface built with custom styled buttons.

Dynamic State Management: Real-time tracking of player turns (X and O).

Win Detection Algorithm: A robust check-winner function that scans 8 possible winning combinations (rows, columns, and diagonals).

Smart Highlighting: Automatically highlights the winning combination in green to improve user experience.

Responsive UI: Uses a grid-based coordinate system for consistent layout.

🚀 Getting Started
Prerequisites
Python 3.x installed.

Tkinter (usually comes pre-installed with Python, but if not: pip install tk).

Installation
Clone the repository:

Bash
git clone https://github.com/YOUR_USERNAME/tic-tac-toe-gui.git
Navigate to the project folder:

Bash
cd tic-tac-toe-gui
Run the application:

Bash
    python tictactoe.py
    ```

## 🛠️ Technical Implementation

### The Core Logic
The project utilizes several key programming concepts:
*   **List Comprehension:** Used to initialize 9 button objects efficiently.
*   **Lambda Functions:** Utilized to pass specific indices to the event handler without executing the function immediately.
*   **Coordinate Mapping:** Uses floor division (`//`) and modulo (`%`) to map a 1D list index into a 2D grid coordinate system.



## 📈 Future Roadmap
- [ ] **AI Opponent:** Implement a Minimax algorithm for an unbeatable CPU.
- [ ] **Score Tracker:** Keep track of wins/losses across multiple rounds.
- [ ] **Custom Themes:** Allow users to choose different colors or dark/light modes.

## 📄 License
Distributed under the MIT License. See `LICENSE` for more information.
