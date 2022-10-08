import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk  # as 'pillow'
import time


# defining the master gui box
master = tk.Tk()
master.geometry('300x300')
master.title('Inventory-Live Application')


# creating start button image
start_image = Image.open('/Users/jamesbaxter/Desktop/tab_inven/start_pic.png')
start_image = start_image.resize((25, 25), Image.ANTIALIAS)
start_image = ImageTk.PhotoImage(start_image)


# creating kill button image
kill_image = Image.open('/Users/jamesbaxter/Desktop/tab_inven/stop_pic.png')
kill_image = kill_image.resize((25, 25), Image.ANTIALIAS)
kill_image = ImageTk.PhotoImage(kill_image)


# "Inventory-Live Application Interface Menu"
label_title = tk.Label(master, text='Inventory-Live Application Interface Menu')
label_title.place(relx=0.5, rely=0.2, anchor='center')


# Program status module (passive [dumb]... for now...)
def button_envr_callback():
    if label_envr['text'] == 'Ready':
        label_envr['text'] = 'Running'
        messagebox.showinfo('System_Status:', 'Envr Control Now Running.')
    else:
        label_envr['text'] = 'Ready'


# label and button entities
label_envr = tk.Label(master, text='Ready')
button_envr = tk.Button(master, text='  Envr Ctrl  ', image=start_image, command=button_envr_callback, compound=tk.TOP)

# label and button positions & plotting
label_envr.place(relx=0.7, rely=0.4, anchor='center')
button_envr.place(relx=0.4, rely=0.4, anchor='center')


# Auto-Harvest control interface #
def button_harvest_callback():
    if label_harvest['text'] == 'Ready':
        label_harvest['text'] = 'Running'
        messagebox.showinfo('System_Status:', 'Harvest Now Running.')
    else:
        label_envr['text'] = 'Ready'


# label and button entities
label_harvest = tk.Label(master, text='Ready')
button_harvest = tk.Button(master, text='  Harvest   ', image=start_image, command=button_harvest_callback, compound=tk.TOP)

# label and button positions & plotting
label_harvest.place(relx=0.7, rely=0.6, anchor='center')
button_harvest.place(relx=0.4, rely=0.6, anchor='center')


# Universal kill-switch button interface #
def button_kill_callback():
    label_envr['text'] = 'Ready'
    label_harvest['text'] = 'Ready'
    messagebox.showinfo('System_Status:', 'Process Killed Successfully')


# label and button entities
button_kill = tk.Button(master, text='Kill Switch ', image=kill_image, command=button_kill_callback, compound=tk.TOP)
# label_kill = tk.Label(master, text=' ')

# label and button positions & plotting
# label_kill.grid(row=2, column=1)
button_kill.place(relx=0.4, rely=0.8, anchor='center')


# the app mainloop
tk.mainloop()
