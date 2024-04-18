import logging
import tkinter as tk
from tkinter import messagebox
import sqlite3
from tkcalendar import DateEntry
from tkinter import ttk
from PIL import ImageTk, Image 


# Set up logging
logging.basicConfig(filename='hotel_booking.log', level=logging.DEBUG)
class HotelBookingForm:
    def __init__(self, master):
        self.master = master
        self.create_gui()
        self.initialize_database()
        

    def create_gui(self):
        """Create the GUI for the hotel booking form."""
        self.master.title("Zoo App Hotel Booking")
        self.master.geometry("900x900")
        self.master.configure(background='#ffcc66')
        

        self.name_label = tk.Label(self.master, text="Name:")
        self.name_label.pack(pady=5)
        self.name_entry = tk.Entry(self.master)
        self.name_entry.pack(pady=5)

        self.email_label = tk.Label(self.master, text="Email:")
        self.email_label.pack(pady=5)
        self.email_entry = tk.Entry(self.master)
        self.email_entry.pack(pady=5)

        self.check_in_label = tk.Label(self.master, text="Check-in Date :")
        self.check_in_label.pack(pady=5)
        self.check_in_date_entry = DateEntry(self.master)
        self.check_in_date_entry.pack(pady=5)

        self.check_out_label = tk.Label(self.master, text="Check-out Date :")
        self.check_out_label.pack(pady=5)
        self.check_out_date_entry = DateEntry(self.master)
        self.check_out_date_entry.pack(pady=5)

        self.room_type_label = tk.Label(self.master, text="Room Type:")
        self.room_type_label.pack(pady=5)
        self.room_type_combobox = ttk.Combobox(self.master, values=["Single", "Double", "Suite"])
        self.room_type_combobox.pack(pady=5)

        self.check_availability_button = tk.Button(self.master, text="Check Availability", command=self.check_availability)
        self.check_availability_button.pack(pady=10)

        self.submit_button = tk.Button(self.master, text="Submit", command=self.submit)
        self.submit_button.pack(pady=10)
        # Load the image
        image = Image.open("images/suite.jpg")

         # Resize the image to fit the size of the page
        image = image.resize((600, 400), Image.ANTIALIAS)  # Replace (800, 600) with the size of your page

         # Convert the image to a Tkinter-compatible photo image
        self.image = ImageTk.PhotoImage(image)
        
        # Create a label with the image
        self.image_label = tk.Label(self.master, image=self.image)
        self.image_label.pack()


        self.page_frame = tk.Frame(self.master)
        self.page_frame.pack()

        self.page_label = tk.Label(self.page_frame, text="suite")
        self.page_label.pack()
        # self.home_button = tk.Button(self.master, text="Return to Home Page", command=self.zoo_app.show_main_page)
        # self.home_button.pack()
        
    def initialize_database(self):
        """Initialize the database."""
        self.conn = sqlite3.connect('bookings.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS bookings (
                name TEXT,
                email TEXT,
                check_in_date TEXT,
                check_out_date TEXT,
                room_type TEXT
            )
        ''')
        self.conn.commit()
         # Log the initialization of the database
        logging.info('Database initialized')

    def check_availability(self):
        """Check the availability of a room."""
        check_in_date = self.check_in_date_entry.get_date()
        check_out_date = self.check_out_date_entry.get_date()
        room_type = self.room_type_combobox.get()

        availability = self.get_availability(check_in_date, check_out_date, room_type)
        if availability:
            messagebox.showinfo("Availability", "Room is available for the selected dates.")
        else:
            messagebox.showinfo("Availability", "Room is not available for the selected dates.")

         # Log the check availability operation
        logging.info('Checked availability')

    def get_availability(self, check_in_date, check_out_date, room_type):
        """Check the availability of a room in the database."""
        self.cursor.execute('''
            SELECT * FROM bookings
            WHERE room_type = ? AND (
                (check_in_date <= ? AND check_out_date >= ?) OR
                (check_in_date < ? AND check_out_date >= ?) OR
                (check_in_date <= ? AND check_out_date > ?) OR
                (check_in_date < ? AND check_out_date > ?)
            )
        ''', (room_type, check_in_date, check_in_date, check_out_date, check_out_date, check_in_date, check_out_date, check_out_date, check_in_date))
        availability = self.cursor.fetchone() is None

        if availability:
            logging.info('Got availability')
        
        return availability

    def submit(self):
        """Submit the booking."""
        name = self.name_entry.get()
        email = self.email_entry.get()
        check_in_date = self.check_in_date_entry.get()
        check_out_date = self.check_out_date_entry.get()
        room_type = self.room_type_combobox.get()

        if check_in_date > check_out_date:
            messagebox.showerror("Invalid Dates", "Check-out date must be after check-in date.")
            return

        self.cursor.execute('''
            INSERT INTO bookings (name, email, check_in_date, check_out_date, room_type)
            VALUES (?, ?, ?, ?, ?)
        ''', (name, email, check_in_date, check_out_date, room_type))
        self.conn.commit()

        messagebox.showinfo("Booking submitted", "Booking submitted successfully.")
        logging.info('Submitted booking')

if __name__ == "__main__":
    root = tk.Tk()
    HotelBookingForm(root)
    root.mainloop()