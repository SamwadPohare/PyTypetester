import tkinter as tk
from tkinter import messagebox
import random
import time
from utils import mistake, speed_time, calculate_accuracy

class TypeTesterGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Typetester - GUI Edition")
        self.master.geometry("600x500")
        self.master.config(padx=20, pady=20)

        self.start_time = None
        self.passage = self.get_random_passage()

        # Widgets
        self.label = tk.Label(master, text="Type the passage below:", font=("Arial", 14))
        self.label.pack(pady=10)

        self.text_display = tk.Text(master, height=5, font=("Courier", 12), wrap="word")
        self.text_display.insert(tk.END, self.passage)
        self.text_display.config(state='disabled')
        self.text_display.pack(pady=10)

        self.entry = tk.Text(master, height=5, font=("Courier", 12), wrap="word")
        self.entry.pack(pady=10)

        self.start_button = tk.Button(master, text="Start Typing", command=self.start_typing)
        self.start_button.pack(pady=5)

        self.submit_button = tk.Button(master, text="Submit", state='disabled', command=self.submit_text)
        self.submit_button.pack(pady=5)

        self.result_label = tk.Label(master, text="", font=("Arial", 12), fg="green")
        self.result_label.pack(pady=10)

    def get_random_passage(self):
        try:
            with open("tests/sample_texts.txt", "r") as f:
                lines = f.readlines()
            return random.choice(lines).strip()
        except FileNotFoundError:
            return "The quick brown fox jumps over the lazy dog."

    def start_typing(self):
        self.entry.delete("1.0", tk.END)
        self.start_time = time.time()
        self.submit_button.config(state='normal')
        self.result_label.config(text="")

    def submit_text(self):
        end_time = time.time()
        user_input = self.entry.get("1.0", tk.END).strip()

        wpm = speed_time(self.start_time, end_time, user_input)
        errors = mistake(self.passage, user_input)
        accuracy = calculate_accuracy(self.passage, user_input)

        result = f"Speed: {wpm} WPM | Mistakes: {errors} | Accuracy: {accuracy}%"
        self.result_label.config(text=result)

        self.submit_button.config(state='disabled')

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = TypeTesterGUI(root)
    root.mainloop()
