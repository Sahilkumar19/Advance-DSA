import hashlib
from tkinter import Tk, Label, Entry, Button, messagebox, Toplevel

# Database to store the users' credentials
user_info = {
    'sahil': '5c0755c6fae2b66608de33165df0ba65',  # password1
    'ranjan': 'e10adc3949ba59abbe56e057f20f883e',  # 123456
    'suraj': '8127a1ad276367223d9d0a2d264e4b2e'   # suraj123
}

# User authentication
def login(username, password):
    # Check if the username exists in the database
    if username in user_info:
        # Compare the entered password with the stored hash
        if hashlib.md5(password.encode()).hexdigest() == user_info[username]:
            print(hashlib.md5(password.encode()).hexdigest())
            return True
    return False

# GUI Framework
class PasswordManagerGUI:
    def __init__(self):
        self.root = Tk()
        self.root.title("Password Manager")
        self.root.attributes('-fullscreen', True)  # Set full screen mode

        self.label_username = Label(self.root, text="Username:")
        self.label_username.pack()
        self.entry_username = Entry(self.root)
        self.entry_username.pack()

        self.label_password = Label(self.root, text="Password:")
        self.label_password.pack()
        self.entry_password = Entry(self.root, show="*")
        self.entry_password.pack()

        self.button_login = Button(self.root, text="Login", command=self.login_user)
        self.button_login.pack()

    def login_user(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        if login(username, password):
            messagebox.showinfo("Success", "Logged in successfully!")
            self.open_next_page(username)
        else:
            messagebox.showerror("Error", "Incorrect username or password!")

    def open_next_page(self, username):
        self.root.withdraw()  # Hide the login window

        # Open the next page
        next_page = Toplevel()
        next_page.title("Welcome")
        next_page.attributes('-fullscreen', True)  # Set full screen mode

        label_welcome = Label(next_page, text=f"Welcome, {username}!")
        label_welcome.pack()

        button_logout = Button(next_page, text="Logout", command=lambda: self.logout(next_page))
        button_logout.pack()

    def logout(self, window):
        window.destroy()  # Close the next page
        self.root.deiconify()  # Show the login window

if __name__ == "__main__":
    app = PasswordManagerGUI()
    app.root.mainloop()
