from tkinter import *
import os



root = Tk()
root.title(" Aggieland Accessors ")
root.geometry("600x400")

btn = Button(root, text='Close me!', bd='5', command=root.destroy)

def run():
    os.system('python3 background.py')

btn2 = Button(root, text="Click Me",command=run)
btn.pack(pady=15)
btn2.pack(pady=15)

root.mainloop()
