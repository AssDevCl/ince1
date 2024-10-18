import tkinter as tk
import pyautogui
import time
from threading import Thread

# Function to simulate mouse movement to prevent AFK
def simulate_afk():
    while True:
        # Move the mouse every few seconds to simulate activity
        pyautogui.move(10, 0)
        time.sleep(5)  # Wait 5 seconds before the next move
        pyautogui.move(-10, 0)
        time.sleep(5)

# Class to create the graphical interface
class AFKApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AFK Simulator")
        self.root.geometry("300x200")

        # Label with a message
        self.label = tk.Label(root, text="Simulating AFK...", font=("Arial", 14))
        self.label.pack(pady=50)

        # Start button
        self.start_button = tk.Button(root, text="Start AFK", command=self.start_afk)
        self.start_button.pack(pady=10)

        # Stop button
        self.stop_button = tk.Button(root, text="Stop AFK", command=self.stop_afk)
        self.stop_button.pack(pady=10)
        self.stop_button.config(state=tk.DISABLED)

        self.afk_thread = None
        self.running = False

    # Function to start the AFK simulation
    def start_afk(self):
        self.running = True
        self.afk_thread = Thread(target=simulate_afk)
        self.afk_thread.daemon = True  # Allows the thread to close with the program
        self.afk_thread.start()
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)

    # Function to stop the AFK simulation
    def stop_afk(self):
        self.running = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

# Main application execution
if __name__ == "__main__":
    root = tk.Tk()
    app = AFKApp(root)
    root.mainloop()
