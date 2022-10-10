import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk  # as 'pillow'
import time


# defining the master gui box
master = tk.Tk()
master.geometry('500x500')
master.title('Inventory-Live Application')


# creating start button image
start_image = Image.open('/Users/jamesbaxter/Desktop/tab_inven/start_pic.png')
start_image = start_image.resize((100, 80), Image.ANTIALIAS)
start_image = ImageTk.PhotoImage(start_image)


# creating kill button image
kill_image = Image.open('/Users/jamesbaxter/Desktop/tab_inven/stop_pic.png')
kill_image = kill_image.resize((100, 80), Image.ANTIALIAS)
kill_image = ImageTk.PhotoImage(kill_image)


# creating status graphic image
status_image = Image.open('/Users/jamesbaxter/Desktop/tab_inven/status_pic.png')
status_image = status_image.resize((300, 60), Image.ANTIALIAS)
status_image = ImageTk.PhotoImage(status_image)


# Program status module (passive [dumb]... for now...)
def start_button_click():
    start_status['text'] = 'Running'


# Universal kill-switch button interface #
def stop_button_click():
    start_status['text'] = 'Ready'


# START button properties
start_button = tk.Button(master, image=start_image, borderwidth=20,  command=start_button_click, compound=tk.TOP)
start_button.place(relx=0.3, rely=0.2, anchor='center')


# STOP button properties
stop_button = tk.Button(master, image=kill_image, borderwidth=20, command=stop_button_click, compound=tk.TOP)
stop_button.place(relx=0.7, rely=0.2, anchor='center')


# STATUS text properties
start_status = tk.Label(master, text='Ready')
start_status.place(relx=0.5, rely=0.6, anchor='center')


# STATUS graphic properties
status_graphic = tk.Label(master, image=status_image, compound=tk.TOP)
status_graphic.place(relx=0.5, rely=0.5, anchor='center')


# the app mainloop
tk.mainloop()
