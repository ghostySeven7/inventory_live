import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # as 'pillow'
import live_inventory


# defining the master gui box
master = tk.Tk()
master.geometry('500x300')
master.title('Inventory-Live Application')


# creating run button image
run_image = Image.open('/Users/jamesbaxter/PycharmProjects/finances/run_pic.png')  # change at production
run_image = run_image.resize((300, 100), Image.ANTIALIAS)
run_image = ImageTk.PhotoImage(run_image)


# runs live_inventory.py
def run_button_click():
    messagebox.showinfo('System_Status:', 'Inventory has been updated')
    live_inventory.makes_ledger_live()


# RUN button properties
run_button = tk.Button(master, image=run_image, borderwidth=20,  command=run_button_click, compound=tk.TOP)
run_button.place(relx=0.5, rely=0.5, anchor='center')


tk.mainloop()



