from tkinter import *
from tkinter import messagebox
import json

class LoginPage:
    def __init__(self, root, on_login_success):
        self.root = root
        self.on_login_success = on_login_success  
        self.root.title("Login Page")
        self.root.geometry("400x200")

        self.username_label = Label(root, text="Username:")
        self.username_label.pack()

        self.username_entry = Entry(root)
        self.username_entry.pack()

        self.password_label = Label(root, text="Password:")
        self.password_label.pack()

        self.password_entry = Entry(root, show="*")
        self.password_entry.pack()

        self.login_button = Button(root, text="Login", command=self.login)
        self.login_button.pack()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if self.check_credentials(username, password):
            if self.check_admin_role(username):
                messagebox.showinfo("Login", "Login successful!")
                self.on_login_success()
            else:
                messagebox.showerror("Login Failed", "You don't have admin privileges.")
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    def check_credentials(self, username, password):
        with open("credentials.json", "r") as file:
            credentials = json.load(file)
        
        if username in credentials and credentials[username]["password"] == password:
            return True
        else:
            return False

    def check_admin_role(self, username):
        with open("credentials.json", "r") as file:
            credentials = json.load(file)
        
        if username in credentials:
            return credentials[username]["role"] == "admin"
        else:
            return False


if __name__ == "__main__":
    root = Tk()
    login_page = LoginPage(root, lambda: print("Login successful")) 
    root.mainloop()
