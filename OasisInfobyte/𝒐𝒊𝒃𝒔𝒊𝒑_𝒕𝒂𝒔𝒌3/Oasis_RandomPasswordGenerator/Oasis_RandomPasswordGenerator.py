#Advanced
import tkinter as tk
from tkinter import ttk, messagebox
import string
import pyperclip  
import random

class Password:
    def __init__(self, root):
        self.root = root
        self.root.title("Random Password Generator")
        self.length_var = tk.IntVar()
        self.uppercase_var = tk.BooleanVar()
        self.lowercase_var = tk.BooleanVar()
        self.digits_var = tk.BooleanVar()
        self.symbols_var = tk.BooleanVar()
        self.password_var = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        length_label = ttk.Label(self.root, text="Enter Password Length:")
        length_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)

        length_entry = ttk.Entry(self.root, textvariable=self.length_var)
        length_entry.grid(row=0, column=1, padx=10, pady=5, sticky=tk.W)
        length_entry.insert(0, "1")
        
        uppercase_check = ttk.Checkbutton(self.root, text="Uppercase", variable=self.uppercase_var)
        uppercase_check.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)

        lowercase_check = ttk.Checkbutton(self.root, text="Lowercase", variable=self.lowercase_var)
        lowercase_check.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)
        lowercase_check.invoke() 

        digits_check = ttk.Checkbutton(self.root, text="Numbers", variable=self.digits_var)
        digits_check.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)

        symbols_check = ttk.Checkbutton(self.root, text="Symbols", variable=self.symbols_var)
        symbols_check.grid(row=2, column=1, padx=10, pady=5, sticky=tk.W)

        generate_button = ttk.Button(self.root, text="Generate a Password", command=self.generate_random_password)
        generate_button.grid(row=3, column=0, columnspan=2, pady=10)

        password_label = ttk.Label(self.root, text="Generated Password:")
        password_label.grid(row=4, column=0, padx=10, pady=5, sticky=tk.W)

        password_entry = ttk.Entry(self.root, textvariable=self.password_var, state="readonly")
        password_entry.grid(row=4, column=1, padx=10, pady=5, sticky=tk.W + tk.E)

        copy_button = ttk.Button(self.root, text="Copy to Clipboard", command=self.copy_to_clipboard)
        copy_button.grid(row=5, column=0, columnspan=2, pady=10)

        complexity_label = ttk.Label(self.root, text="Choose at least 3 options for a secure password.")
        complexity_label.grid(row=6, column=0, columnspan=2, pady=5)

    def generate_random_password(self):
        selected_options = sum([self.uppercase_var.get(), self.lowercase_var.get(), self.digits_var.get(), self.symbols_var.get()])
        if selected_options < 3:
            messagebox.showinfo("Error", "Choose at least 3 options for a secure password.")
            return

        length = self.length_var.get()
        charset = ""

        if self.uppercase_var.get():
            charset += string.ascii_uppercase
        if self.lowercase_var.get():
            charset += string.ascii_lowercase
        if self.digits_var.get():
            charset += string.digits
        if self.symbols_var.get():
            charset += string.punctuation

        if not charset:
            messagebox.showinfo("Error", "Select at least one character set.")
            return

        password = ''.join(random.choice(charset) for _ in range(length))
        self.password_var.set(password)

    def copy_to_clipboard(self):
        generated_password = self.password_var.get()
        pyperclip.copy(generated_password)
 

if __name__ == "__main__":
    root = tk.Tk()
    app = Password(root)
    root.mainloop()


# Develop an advanced password generator with a graphical user interface (GUI) using Tkinter or PyQt. Enhance it by including options for password complexity,
#  adherence to security rules, and clipboard integration for easy copying.
# Key Concepts and Challenges:

# Randomization: Learn how to generate random characters and strings.
# User Input Validation: Validate user input for password length and character types.
# Character Set Handling: Manage different character sets (letters, numbers, symbols).
# GUI Design (for Advanced): Create an intuitive and user-friendly interface for password generation.
# Security Rules (for Advanced): Implement rules for generating strong, secure passwords.
# Clipboard Integration (for Advanced): Allow users to copy generated passwords to the clipboard for convenience.
# Customization (for Advanced): Enable users to customize password generation further, e.g., excluding specific characters.



