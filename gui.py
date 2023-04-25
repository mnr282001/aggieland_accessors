from tkinter import *
from os import system


root = Tk()
root.title(" Aggieland Accessors ")

root.title("Frame Example")
root.geometry("600x350")


def run():
    system('python3 background.py')


btn_for_run = Button(
    root, text="Click Me to Start Detecting Color on Click! When you are done, click Escape!", command=run)

btn_to_close = Button(root, text='Close me!', bd='5', command=root.destroy)
btn_for_run.pack(pady=15)
btn_to_close.pack(pady=15)


root.mainloop()
