from tkinter import *
import tkinter.messagebox as messagebox
from tkinter import filedialog
from tkmacosx import Button

from EncryptionHandler import EncryptionDecryption
from LoginPage import LoginPage

root = Tk()
root.title("Encryption and Decryption Data")
root.geometry("1920x1000+0+0")
private_key = None
plaintext_text = None
key_entry_var = None
algorithm_var = None


#==================================================================================================
def encrypt_text():
    global plaintext_text, key_entry_var, algorithm_var
    
    plaintext = plaintext_text.get("1.0", END)
    key = key_entry_var.get().strip()
    algorithm = algorithm_var.get()
    ciphertext = EncryptionDecryption.encrypt(plaintext, key, algorithm)
    if ciphertext is not None:
        plaintext_text.delete("1.0", END)
        plaintext_text.insert(END, ciphertext)

def decrypt_text():
    global plaintext_text, key_entry_var, algorithm_var
    
    ciphertext_str = plaintext_text.get("1.0", END)
    key = key_entry_var.get().strip()
    algorithm = algorithm_var.get()
    plaintext = EncryptionDecryption.decrypt(ciphertext_str, key, algorithm)
    if plaintext is not None:
        plaintext_text.delete("1.0", END)
        plaintext_text.insert(END, plaintext)


def insert_file_content():
    global plaintext_text
    
    file_path = filedialog.askopenfilename(initialdir="/", title="Select File", filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
    if file_path:
        try:
            with open(file_path, 'r') as file:
                content = file.read()
                plaintext_text.delete("1.0", END)
                plaintext_text.insert(END, content)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to read file: {str(e)}")

def save_encrypted_file():
    global plaintext_text
    
    ciphertext = plaintext_text.get("1.0", END)
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
    if file_path:
        try:
            with open(file_path, 'w') as file:
                file.write(ciphertext)
                messagebox.showinfo("File Saved", "Encrypted file saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save file: {str(e)}")

def reset():
    global plaintext_text, key_entry_var
    
    plaintext_text.delete("1.0", END)
    key_entry_var.set("")

def iexit():
    root.destroy()

#============================================ GUI ======================================================

def on_login_success():
    global plaintext_text, key_entry_var, algorithm_var
    
    button_frame = Frame(root)
    button_frame.pack(pady=20)

    text_encryption_button = Button(button_frame, font=('arial', 20, 'normal'), width=150, height=45, text="Encrypt Text", bg='#D1DCA7', command=encrypt_text)
    text_encryption_button.pack(side=LEFT, padx=10)

    text_decryption_button = Button(button_frame, font=('arial', 20, 'normal'), width=150, height=45, text="Decrypt Text", bg='cadetblue2', command=decrypt_text)
    text_decryption_button.pack(side=LEFT, padx=10)

    save_file_button = Button(button_frame, font=('arial', 15, 'normal'), width=150, height=45, text="Save Encrypted File", bg='MediumPurple1', command=save_encrypted_file)
    save_file_button.pack(side=LEFT, padx=10)

    bottom_frame = Frame(root)
    bottom_frame.pack(side=BOTTOM, fill=X, pady=20)  

    reset_button = Button(bottom_frame, font=('arial', 20, 'normal'), width=100, height=45, bg='#D9D9D9', text="Reset", command=reset)
    reset_button.pack(side=LEFT, padx=(400, 50), pady=5)  

    exit_button = Button(bottom_frame, font=('arial', 20, 'normal'), width=100, height=45, bg='#D9D9D9', text="Exit", command=iexit)
    exit_button.pack(side=RIGHT, padx=(50, 400), pady=5)  

    key_frame = Frame(root)
    key_frame.pack(pady=20)

    key_label = Label(key_frame, font=('arial', 24, 'bold'), text="Enter Key:")
    key_label.pack(side=LEFT, padx=10)

    key_entry_var = StringVar()
    key_entry = Entry(key_frame, font=('arial', 24, 'bold'), width=12, justify='center', textvariable=key_entry_var, show="*")
    key_entry.pack(side=LEFT, padx=10)

    algorithm_var = StringVar()
    algorithm_var.set("XOR (Exclusive OR)") 
    algorithm_menu = OptionMenu(key_frame, algorithm_var, "XOR (Exclusive OR)", "CAESER (Cipher)", "One Time Pad (Cipher)")
    algorithm_menu.pack(side=LEFT, padx=10)

    plain_frame = Frame(root)
    plain_frame.pack(pady=20)

    plaintext_label = Label(plain_frame, font=('arial', 24, 'bold'), text="Enter Plain Text:")
    plaintext_label.pack(side=LEFT, padx=10) 

    plaintext_text = Text(plain_frame, font=('arial', 24, 'bold'), width=50, height=15)
    plaintext_text.pack(side=LEFT, fill=BOTH, expand=True, padx=10, pady=10) 

    insert_file_button = Button(plain_frame, font=('arial', 16, 'normal'), width=150, height=45, text="Insert File Content", bg='#D9D9D9', command=insert_file_content)
    insert_file_button.pack(side=RIGHT, padx=(25, 25), pady=5)

login_page = LoginPage(root, on_login_success)
root.mainloop()
