import tkinter as tk 
from tkinter import messagebox
import sqlite3
import re
from PIL import ImageTk , Image
from tkinter import ttk

import re




class ClientFormPage:
    def __init__(self, master, hotel_booking_form):
        self.master = master
        master.title("Zoo App Client Form")

        self.hotel_booking_form = hotel_booking_form

        self.tree = ttk.Treeview(master, columns=('Name', 'Email', 'Check-in Date', 'Check-out Date', 'Room Type'), show='headings')
        self.tree.heading('Name', text='Name')
        self.tree.heading('Email', text='Email')
        self.tree.heading('Check-in Date', text='Check-in Date')
        self.tree.heading('Check-out Date', text='Check-out Date')
        self.tree.heading('Room Type', text='Room Type')
        self.tree.pack()

        self.load_bookings()

    # def load_bookings(self):
    #     self.tree.delete(*self.tree.get_children())  # Clear the treeview
    #     bookings = self.hotel_booking_form.get_all_bookings()
    #     if bookings is None:
    #         bookings = []
    #     for booking in bookings:
    #         self.tree.insert('', 'end', values=booking)
    def load_bookings(self):
        try:
            self.tree.delete(*self.tree.get_children())  # Clear the treeview
            bookings = self.hotel_booking_form.get_all_bookings()
            if bookings is None:
                bookings = []
            for booking in bookings:
                self.tree.insert('', 'end', values=booking)
        except Exception as e:
            print(f"An error occurred: {e}")


import re
import sqlite3
import tkinter as tk
from tkinter import messagebox

class SignUpPage:
    def __init__(self, master):
        self.master = master
        self.create_gui()

    def create_gui(self):
        self.master.title("Zoo App Sign Up")
        self.master.geometry("800x600")
        # Load the image file
        img = Image.open("images/jungle.jpg")  # Replace with your image file path

        # Resize the image
        img = img.resize((900, 900), Image.LANCZOS)  # Resize to match your window size

        # Convert the image to a Tkinter-compatible photo image
        bg = ImageTk.PhotoImage(img)

        # Create a label with the image and add it to the window
        bg_label = tk.Label(self.master, image=bg)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Keep a reference to the image to prevent it from being garbage collected
        bg_label.image = bg

        self.username_label = tk.Label(self.master, text="Email:")
        self.username_label.pack(pady=5)
        self.username_entry = tk.Entry(self.master)
        self.username_entry.pack(pady=5)

        self.password_label = tk.Label(self.master, text="Password:")
        self.password_label.pack(pady=5)
        self.password_entry = tk.Entry(self.master, show="*")
        self.password_entry.pack(pady=5)

        self.confirm_password_label = tk.Label(self.master, text="Confirm Password:")
        self.confirm_password_label.pack(pady=5)
        self.confirm_password_entry = tk.Entry(self.master, show="*")
        self.confirm_password_entry.pack(pady=5)

        self.sign_up_button = tk.Button(self.master, text="Sign Up", command=self.sign_up)
        self.sign_up_button.pack(pady=10)

    def sign_up(self):
        email = self.username_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()

        # Validate the email
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            messagebox.showerror("Sign Up Failed", "Invalid email")
            return

        # Validate the password
        if len(password) < 8 or not re.search(r"\d", password):
            messagebox.showerror("Sign Up Failed", "Password must be at least 8 characters long and contain a number")
            return

        # Check if the password and confirm password match
        if password != confirm_password:
            messagebox.showerror("Sign Up Failed", "Passwords do not match")
            return

        # Perform sign-up logic here
        conn = sqlite3.connect('zoo_app.db')
        c = conn.cursor()

        # Create table if it doesn't exist
        c.execute('''CREATE TABLE IF NOT EXISTS users
                     (email text, password text)''')

        # Insert a row of data
        c.execute("INSERT INTO users VALUES (?,?)", (email, password))

        # Save (commit) the changes
        conn.commit()

        # Close the connection
        conn.close()

        messagebox.showinfo("Sign Up Successful", "Account created successfully")

if __name__ == "__main__":
    root = tk.Tk()
    SignUpPage(root)
    root.mainloop()
# class SignUpPage:
   
#     def __init__(self, master):
#         self.master = master
#         master.title("Sign Up Page")

#         self.username_label = tk.Label(master, text="Username")
#         self.username_label.pack()

#         self.username_entry = tk.Entry(master)
#         self.username_entry.pack()

#         self.password_label = tk.Label(master, text="Password")
#         self.password_label.pack()

#         self.password_entry = tk.Entry(master, show="*")
#         self.password_entry.pack()

#         self.confirm_password_label = tk.Label(master, text="Confirm Password")
#         self.confirm_password_label.pack()

#         self.confirm_password_entry = tk.Entry(master, show="*")
#         self.confirm_password_entry.pack()

#         self.signup_button = tk.Button(master, text="Sign Up", command=self.signup)
#         self.signup_button.pack()


#     def signup(self):
#         username = self.username_entry.get()
#         password = self.password_entry.get()
#         confirm_password = self.confirm_password_entry.get()

#         # Validate the username as an email
#         # Validate the username as an email
#         if not re.match(r"[^@]+@[^@]+\.[^@]+", username):
#             messagebox.showerror("Sign Up error", "Invalid email")
#             return

#         # Validate the password
#         if not re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$", password):
#             messagebox.showerror("Sign Up error", "Password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, and one number")
#             return

#         # Here you should register the new user
#         # For example, let's just check if the passwords match
#         if password == confirm_password:
#             messagebox.showinfo("Sign Up info", "Sign Up successful")
#             self.master.destroy()  # close the sign up window
#             root = tk.Tk()  # create a new root window
#             app = HomePage(root)  # open the main app
#             root.mainloop()
#         else:
#             messagebox.showerror("Sign Up error", "Passwords do not match")

# # Create a new Tk root window
# root = tk.Tk()

# # Create the sign up page
# signup_page = SignUpPage(root)

# # Start the Tkinter event loop
# root.mainloop()  # ... other code ...