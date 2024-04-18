import tkinter as tk
from tkinter import ttk

def get_booking_info(customer_id):
    # Fetch booking information from the database based on the customer_id
    # This is just a placeholder. Replace it with your actual database query.
    return {
        'booking_id': '123',
        'booking_date': '2022-01-01',
        'booking_details': 'Details about the booking...'
    }

def show_customer_info(customer_id):
    booking_info = get_booking_info(customer_id)

    window = tk.Tk()
    window.title("Customer Info")

    ttk.Label(window, text="Booking ID:").grid(column=0, row=0)
    ttk.Label(window, text=booking_info['booking_id']).grid(column=1, row=0)

    ttk.Label(window, text="Booking Date:").grid(column=0, row=1)
    ttk.Label(window, text=booking_info['booking_date']).grid(column=1, row=1)

    ttk.Label(window, text="Booking Details:").grid(column=0, row=2)
    ttk.Label(window, text=booking_info['booking_details']).grid(column=1, row=2)

    window.mainloop()

# Test the function with a customer_id
show_customer_info(1)