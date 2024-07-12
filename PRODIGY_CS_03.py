import tkinter as tk
from tkinter import ttk

def password_strength(password):
    # Check password length
    if len(password) < 8:
        return "Weak"
    elif 8 <= len(password) < 12:
        return "Medium"
    else:
        # Count occurrences of uppercase, lowercase, digits, and symbols
        upper_count = sum(1 for char in password if char.isupper())
        lower_count = sum(1 for char in password if char.islower())
        digit_count = sum(1 for char in password if char.isdigit())
        symbol_count = sum(1 for char in password if not char.isalnum())

        # Determine strength based on character types
        total_count = upper_count + lower_count + digit_count + symbol_count
        if total_count < 3:
            return "Weak"
        else:
            return "Strong"

def check_password_strength():
    password = password_entry.get()
    strength = password_strength(password)
    result_label.config(text=f"Password strength: {strength}")

root = tk.Tk()
root.title("Password Strength Checker")
root.configure(background="#000000")
root.geometry("400x200")
root.resizable(False, False)

style = ttk.Style()
style.configure("TFrame", background="#000000")
style.configure("TLabel", background="#000000", foreground="white", font=("Arial", 12))
style.configure("TButton", background="#2e7d32", foreground="white", font=("Arial", 12, "bold"))
style.map("TButton", background=[('active', '#1b5e20')])

frame = ttk.Frame(root, padding="10", style="TFrame")
frame.grid(row=0, column=0, sticky="nsew")

ttk.Label(frame, text="Enter your password:", style="TLabel").grid(row=0, column=0, pady=10)
password_entry = ttk.Entry(frame, show='*', width=30)
password_entry.grid(row=1, column=0, pady=10)

ttk.Button(frame, text="Check Strength", command=check_password_strength, style="TButton").grid(row=2, column=0, pady=10)

result_label = ttk.Label(frame, text="", style="TLabel")
result_label.grid(row=3, column=0, pady=10)

root.mainloop()