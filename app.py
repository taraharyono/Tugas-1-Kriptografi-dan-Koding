import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from cryptography.fernet import Fernet
import standardVigenere
import productCipher

class EncryptionApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Encryption and Decryption App")

        self.input_label = ttk.Label(master, text="Input:")
        self.input_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.input_text = tk.Text(master, height=5, width=40)
        self.input_text.grid(row=0, column=1, padx=5, pady=5, columnspan=2)
        
        self.input_file_button = ttk.Button(master, text="Open File", command=self.open_file)
        self.input_file_button.grid(row=0, column=3, padx=5, pady=5)

        self.choice_label = ttk.Label(master, text="Choose Action:")
        self.choice_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        self.choice_var = tk.StringVar()
        self.choice_var.set("Encrypt")
        self.choice_menu = ttk.OptionMenu(master, self.choice_var, "Encrypt", "Encrypt", "Decrypt", command=self.toggle_column_key)
        self.choice_menu.grid(row=1, column=1, padx=5, pady=5)

        self.technique_label = ttk.Label(master, text="Choose Technique:")
        self.technique_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")

        self.technique_var = tk.StringVar()
        self.technique_var.set("Vigenere Standard")
        self.technique_menu = ttk.OptionMenu(master, self.technique_var, "Vigenere Standard", "Vigenere Standard", "Product Cipher", command=self.toggle_column_key)
        self.technique_menu.grid(row=2, column=1, padx=5, pady=5)

        self.key_label = ttk.Label(master, text="Key:")
        self.key_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")

        self.key_entry = ttk.Entry(master)
        self.key_entry.grid(row=3, column=1, padx=5, pady=5)

        self.column_key_label = ttk.Label(master, text="Column Key:")
        self.column_key_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")

        self.column_key_entry = ttk.Entry(master)
        self.column_key_entry.grid(row=4, column=1, padx=5, pady=5)
        self.column_key_label.grid_remove()
        self.column_key_entry.grid_remove()

        self.process_button = ttk.Button(master, text="Process", command=self.process)
        self.process_button.grid(row=5, column=1, padx=5, pady=5)

        self.output_label = ttk.Label(master, text="Output:")
        self.output_label.grid(row=6, column=0, padx=5, pady=5, sticky="w")

        self.output_text = tk.Text(master, height=5, width=40)
        self.output_text.grid(row=6, column=1, padx=5, pady=5, columnspan=2)


    def toggle_column_key(self, *args):
        technique = self.technique_var.get()
        if technique == "Product Cipher":
            self.column_key_label.grid()
            self.column_key_entry.grid()
        else:
            self.column_key_label.grid_remove()
            self.column_key_entry.grid_remove()

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
                self.input_text.delete("1.0", tk.END)
                self.input_text.insert("1.0", content)
                
    def process(self):
        input_text = self.input_text.get("1.0", "end-1c")
        choice = self.choice_var.get()
        technique = self.technique_var.get()
        key = self.key_entry.get()

        if not input_text:
            messagebox.showerror("Error", "Please enter some text.")
            return

        if not key:
            messagebox.showerror("Error", "Please enter a key.")
            return

        if technique == "Vigenere Standard":
            if choice == "Encrypt":
                encrypted_text = standardVigenere.encrypt(input_text, key)
            else:
                encrypted_text = standardVigenere.decrypt(input_text, key)
        elif technique == "Product Cipher":
            if choice == "Encrypt":
                encrypted_text = productCipher.encrypt(input_text, key)
            else:
                encrypted_text = productCipher.decrypt(input_text, key)
        else:
            messagebox.showerror("Error", "Invalid technique selected.")
            return

        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, encrypted_text)

def main():
    root = tk.Tk()
    app = EncryptionApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()