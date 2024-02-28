import tkinter as tk
import base64
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
## from PIL import Image, ImageTk
## from cryptography.fernet import Fernet
import standardVigenere
import productCipher
import vigenere
import playfair
import affine
import autokeyVigenere

class EncryptionApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Classic Cryptography App")

        # # Load background image
        # self.bg_image = Image.open("background_image.jpg")
        # self.bg_photo = ImageTk.PhotoImage(self.bg_image)
        # self.bg_image.putalpha(128) 

        # # Create a canvas to hold the background image
        # self.canvas = tk.Canvas(master, width=self.bg_image.width, height=self.bg_image.height)
        # self.canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")
        # self.canvas.grid(row=0, column=0, columnspan=4, rowspan=4, sticky="nsew")
                        
        # Load and display image
        ## image = Image.open("anya.png")
        ## photo = ImageTk.PhotoImage(image)
        ## self.image_label = ttk.Label(master, image=photo)
        ## self.image_label.image = photo
        ## self.image_label.grid(row=0, column=0, columnspan=3, padx=5, pady=5, sticky='w')
        
        # Title label
        self.title_label = ttk.Label(master, text="Welcome to Classic Cryptographic Generator", font=("Helvetica", 16, "bold"))
        self.title_label.grid(row=0, column=1, columnspan=3, padx=8, pady=5)        
        
        # Input
        self.input_type_var = tk.StringVar()
        self.input_type_var.set("Text")

        self.input_type_label = ttk.Label(master, text="Select Input Type:")
        self.input_type_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        self.input_type_menu = ttk.OptionMenu(master, self.input_type_var, "Text", "Text", "File", command=self.toggle_input)
        self.input_type_menu.grid(row=1, column=1, padx=5, pady=5)

        self.input_label = ttk.Label(master, text="Input:")
        self.input_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")

        self.input_text = tk.Text(master, height=5, width=40)
        self.input_text.grid(row=2, column=1, padx=5, pady=5, columnspan=2)
        
        self.input_file_button = ttk.Button(master, text="Open File", command=self.open_file)
        # self.input_file_button.grid(row=1, column=2, padx=5, pady=5)
        
        self.file_label = ttk.Label(master, text="")
        self.file_label.grid(row=2, column=2, padx=5, pady=5, sticky="w")

        self.file_content_label = ttk.Label(master, text="")
        self.file_content_label.grid(row=3, column=1, padx=5, pady=5, sticky="w")

        # Choose Action
        self.choice_label = ttk.Label(master, text="Choose Action:")
        self.choice_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")

        self.choice_var = tk.StringVar()
        self.choice_var.set("Encrypt")
        self.choice_menu = ttk.OptionMenu(master, self.choice_var, "Encrypt", "Encrypt", "Decrypt", command=self.toggle_additional_key)
        self.choice_menu.grid(row=4, column=1, padx=5, pady=5)

        # Choose Technique
        self.technique_label = ttk.Label(master, text="Choose Technique:")
        self.technique_label.grid(row=5, column=0, padx=5, pady=5, sticky="w")

        self.technique_var = tk.StringVar()
        self.technique_var.set("Vigenere Standard")
        self.technique_menu = ttk.OptionMenu(master, self.technique_var, "Vigenere Standard Cipher", "Vigenere Standard Cipher", "Extended Vigenere Cipher", "Playfair Cipher","Product Cipher", "Affine Cipher", "Autokey Vigenere Cipher", command=self.toggle_additional_key)
        self.technique_menu.grid(row=5, column=1, padx=5, pady=5)

        # Key Input
        self.key_label = ttk.Label(master, text="Key:")
        self.key_label.grid(row=6, column=0, padx=5, pady=5, sticky="w")

        self.key_entry = ttk.Entry(master)
        self.key_entry.grid(row=6, column=1, padx=5, pady=5)

        self.column_key_label = ttk.Label(master, text="Column Key:")
        self.column_key_label.grid(row=7, column=0, padx=5, pady=5, sticky="w")

        self.column_key_entry = ttk.Entry(master)
        self.column_key_entry.grid(row=7, column=1, padx=5, pady=5)
        self.column_key_label.grid_remove()
        self.column_key_entry.grid_remove()
        
        self.key_b_label = ttk.Label(master, text="Key (b):")
        self.key_b_label.grid(row=7, column=0, padx=5, pady=5, sticky="w")

        self.key_b_entry = ttk.Entry(master)
        self.key_b_entry.grid(row=7, column=1, padx=5, pady=5)
        self.key_b_label.grid_remove()
        self.key_b_entry.grid_remove()

        self.process_button = ttk.Button(master, text="Process", command=self.process)
        self.process_button.grid(row=8, column=1, padx=5, pady=5)

        self.output_label = ttk.Label(master, text="Output:")
        self.output_label.grid(row=9, column=0, padx=5, pady=5, sticky="w")

        self.output_text = tk.Text(master, height=5, width=40)
        self.output_text.grid(row=9, column=1, padx=5, pady=5, columnspan=2)
        
        self.base64_output_label = ttk.Label(master, text="Base64 Output:")
        self.base64_output_label.grid(row=10, column=0, padx=5, pady=5, sticky="w")

        self.base64_output_text = tk.Text(master, height=5, width=40)
        self.base64_output_text.grid(row=10, column=1, padx=5, pady=5, columnspan=2)

        self.save_button = ttk.Button(master, text="Save Output", command=self.save_output)
        self.save_button.grid(row=11, column=1, padx=5, pady=5)

        self.download_label = ttk.Label(master, text="Berhasil! Silahkan download hasil filenya!")

        self.content = None
        self.isBinary = False
        self.byteArray = None
    

    def toggle_input(self, *args):
        input_type = self.input_type_var.get()
        if input_type == "Text":
            self.input_text.grid(row=2, column=1, padx=5, pady=5, columnspan=2)
            self.input_file_button.grid_remove()
            self.file_label.grid_remove()
            self.input_text.delete("1.0", tk.END)
            self.file_content_label.grid_remove()
        elif input_type == "File":
            self.input_text.grid_remove()
            self.input_label.grid_remove()
            self.input_file_button.grid(row=1, column=1, padx=5, pady=5, columnspan=2)


    def toggle_additional_key(self, *args):
        technique = self.technique_var.get()
        if technique == "Product Cipher":
            self.key_b_label.grid_remove()
            self.key_b_entry.grid_remove()
            self.key_label.config(text="Key :")
            self.column_key_label.grid()
            self.column_key_entry.grid()
            self.column_key_entry.config(validate="key", validatecommand=(self.master.register(self.validate_column_key), "%P"))
        elif technique == "Affine Cipher":
            self.key_label.config(text="Key (a):")
            self.key_b_label.grid()
            self.key_b_entry.grid()
            self.key_b_entry.config(validate="key", validatecommand=(self.master.register(self.validate_column_key), "%P"))
            self.column_key_label.grid_remove()
            self.column_key_entry.grid_remove()
            self.column_key_entry.config(validate="none")
        else:
            self.key_label.config(text="Key :")
            self.key_b_label.grid_remove()
            self.key_b_entry.grid_remove()
            self.key_b_entry.config(validate="none")

            self.column_key_label.grid_remove()
            self.column_key_entry.grid_remove()
            self.column_key_entry.config(validate="none")

    def open_file(self):
        file_path = filedialog.askopenfilename()
        if file_path[-4:] != ".txt":
            self.isBinary = True
        if file_path and not self.isBinary:
            with open(file_path, "r") as file:
                content = file.read()
                self.input_text.delete("1.0", tk.END)
                self.input_text.insert("1.0", content)
                ## print("base64" + base64_content)
        elif self.isBinary:
            with open(file_path, "rb") as file:
                content = file.read()
                ## base64_content = base64.b64encode(content).decode('utf-8')
                self.input_text.delete("1.0", tk.END)
                self.input_text.insert("1.0", content)

                self.content = content

            
            # Update file label to display the filename
            self.file_label.config(text="File: " + file_path)

    def save_output(self):
        output_text = self.output_text.get("1.0", "end-1c")
        if not output_text and not self.isBinary:
            messagebox.showerror("Error", "No output to save.")
            return

        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            if not self.isBinary:  # If the data is text
                with open(file_path, "w") as file:
                    file.write(output_text)
            else:  # If the data is binary
                with open(file_path, "wb") as file:
                    file.write(self.byteArray)

            messagebox.showinfo("Success", "Output saved successfully.")
        else:
            self.file_label.grid_remove()
                
    def process(self):
        input_text = self.input_text.get("1.0", "end-1c")
        choice = self.choice_var.get()
        technique = self.technique_var.get()
        key = self.key_entry.get()

        if not input_text and not self.content:
            messagebox.showerror("Error", "Please enter some text.")
            return

        if not key:
            messagebox.showerror("Error", "Please enter a key.")
            return
        if technique != "Extended Vigenere Cipher" and self.isBinary:
            messagebox.showerror("Error", "File format incompatible with chosen cipher!")
        if technique == "Vigenere Standard Cipher":
            if not key.isalpha():
                messagebox.showerror("Error", "Input must contain only letters.")
                return
            if choice == "Encrypt":
                encrypted_text = standardVigenere.encrypt(input_text, key)
            else:
                encrypted_text = standardVigenere.decrypt(input_text, key)
        elif technique == "Product Cipher":
            if not key.isalpha():
                messagebox.showerror("Error", "Input must contain only letters.")
                return
            column_key = int(self.column_key_entry.get())
            if choice == "Encrypt":
                encrypted_text = productCipher.encrypt(input_text, column_key, key)
            else:
                encrypted_text = productCipher.decrypt(input_text, column_key, key)
        elif technique == "Extended Vigenere Cipher":
            if self.content == None:
                if choice == "Encrypt":
                    encrypted_text = vigenere.extendedVigenereEncrypt(input_text, key)
                    print(encrypted_text)
                else:
                    encrypted_text = vigenere.extendedVigenereDecrypt(input_text, key)
            else:
                self.output_label.grid_remove()
                self.output_text.grid_remove()
                self.base64_output_label.grid_remove()
                self.base64_output_text.grid_remove()
                if choice == "Encrypt":
                    self.isBinary = True
                    self.byteArray = vigenere.extendedVigenereEncryptBytes(self.content, key)
                else:
                    self.isBinary = True
                    self.byteArray = vigenere.extendedVigenereDecryptBytes(self.content, key)
                self.download_label.grid(row=9, column=1, padx=5, pady=5)
        elif technique == "Playfair Cipher":
            if choice == "Encrypt":
                encrypted_text = playfair.playfairEncrypt(input_text, key)
            else:
                encrypted_text = playfair.playfairDecrypt(input_text, key)
        elif technique == "Affine Cipher":
            if (not key.isdigit() or not self.key_b_entry.get().isdigit()):  # Check if key is not an integer
                messagebox.showerror("Error", "Key must be an integer.")
                return
            key_a = int(key)
            key_b = int(self.key_b_entry.get())
            if not affine.isRelativePrime(key_a):
                messagebox.showerror("Error", "Key (a) must be relative prime to 26")
                return
            if choice == "Encrypt":
                encrypted_text = affine.encrypt(input_text, key_a, key_b)
            else:
                encrypted_text = affine.decrypt(input_text, key_a, key_b)
        elif technique == "Autokey Vigenere Cipher":
            if not key.isalpha():
                messagebox.showerror("Error", "Input must contain only letters.")
                return
            if choice == "Encrypt":
                encrypted_text = autokeyVigenere.encrypt(input_text, key)
            else:
                encrypted_text = autokeyVigenere.decrypt(input_text, key)
        else:
            messagebox.showerror("Error", "Invalid technique selected.")
            return

        if not self.isBinary:
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, encrypted_text)
        
        if technique == "Extended Vigenere Cipher":
            if not self.content:
                base64_cipher = base64.b64encode(encrypted_text.encode()).decode()
                
                # Delete previous content and insert new content
                self.base64_output_text.delete("1.0", tk.END)
                self.base64_output_text.insert(tk.END, base64_cipher)
        else:
            self.base64_output_text.delete("1.0", tk.END)
    def validate_column_key(self, new_text):
        try:
            if new_text == "":
                return True
            int(new_text)
            return True
        except ValueError:
            return False
        
def main():
    root = tk.Tk()
    app = EncryptionApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()