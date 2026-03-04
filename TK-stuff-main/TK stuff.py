import time
import math
import tkinter as tk
import sys
import webbrowser as web

#Imports required libraries (excluding math)

window = tk.Tk()

window.title("Experiment")
window.geometry("1200x800")
window.configure(background="white")

#Creates a main window, and defines it's properties

def exit():
    sys.exit()

#Simple function to close a window (specifically the main window, named window)

def open_tab():
    web.open_new_tab("https://www.youtube.com")

#Function to open a new tab to YouTube

def style_exit():
    open_tab()
    time.sleep(1)
    exit()

#Specific function for both, by opening YouTube and closing the main window (will be used later)

def open_win():
    replay = tk.Toplevel(window)
    replay.title("Are you sure?")
    replay.geometry("800x400")
    replay.configure(background="white")

    question = tk.Label(replay, text="Are you sure you want to quit?")
    question.place(rely=0.10, relx=0.50, anchor="center")
    
    Yes = tk.Button(replay, text="Yes", command=exit)
    Yes.place(relx=0.25, rely=0.50, anchor="center")

    No = tk.Button(replay, text="No", command=replay.destroy)
    No.place(relx=0.75, rely=0.50, anchor="center")

#Lil bit complex, but it's just a window that asks if you really want to close the main window
#Had to search up how to do this properly, and ran into so many issues

def both():
    replay = tk.Toplevel(window)
    replay.title("Are you sure?")
    replay.geometry("800x400")
    replay.configure(background="white")

    question = tk.Label(replay, text="Are you sure you want to quit?")
    question.place(rely=0.10, relx=0.50, anchor="center")
    
    Yes = tk.Button(replay, text="Yes", command=style_exit)
    Yes.place(relx=0.25, rely=0.50, anchor="center")

    No = tk.Button(replay, text="No", command=replay.destroy)
    No.place(relx=0.75, rely=0.50, anchor="center")

#Same as the previous one, but it also opens a YouTube tab :3

button = tk.Button(window, text="Open YouTube", command=open_tab)
button.pack(side=tk.TOP)

butto = tk.Button(window, text="Or both", command=both)
butto.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

butt = tk.Button(window, text="End process", command=open_win)
butt.pack(side=tk.BOTTOM)
butt.pack(pady=20)

#Rest of this code is just to create the buttons for the main window

window.mainloop()

#Loops the window until closed
