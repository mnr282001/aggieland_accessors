#from tkinter import *
from os import system
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.title(" Aggieland Accessors ")

#root.title("Frame Example")
root.geometry("600x350")


def run():
    system('py background.py')


btn_for_run = customtkinter.CTkButton(
    root, text="Click Me to Start Detecting Color on Click! When you are done, click Escape!", command=run)

btn_to_close = customtkinter.CTkButton(root, text='Close me!', command=root.destroy)
btn_for_run.pack(pady=15)
btn_to_close.pack(pady=15)


root.mainloop()
