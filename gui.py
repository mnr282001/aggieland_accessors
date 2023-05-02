#from tkinter import *
from os import system, path, remove
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.title(" Aggieland Accessors ")

#root.title("Frame Example")
root.geometry("600x350")

audio_var = False

def audio_change():
    global audio_var
    audio_var = not audio_var

def save_log():
    if path.isfile("color_log.txt"):

        count = 1

        while path.isfile("color_log_"+str(count)+".txt"): count += 1

        f = open("color_log_"+str(count)+".txt", "a")
        g = open("color_log.txt")
        f.write(g.read())
        f.close()
        g.close()

    else:
        print("No available log")
def run():

    global audio_var


    open('audio_set.txt', 'w').close()

    f = open("audio_set.txt", "a")
    if audio_var: f.write("1")
    else: f.write("0")
    f.close()

    system('python background.py')

def end_program():
    global root
    if path.isfile("color_log.txt"):
        remove("color_log.txt")

    root.destroy()

btn_for_run = customtkinter.CTkButton(
    root, text="Click Me to Start Detecting Color on Click! When you are done, click Escape!", command=run)

btn_to_close = customtkinter.CTkButton(root, text='Close me!', command=end_program)
btn_for_run.pack(pady=15)
btn_to_close.pack(pady=15)

btn_save = customtkinter.CTkButton(root, text='Save current color log', command=save_log)
btn_save.pack(pady=15)

box_for_audio = customtkinter.CTkCheckBox(master=root, text="Turn On Audio", command=audio_change)
box_for_audio.pack(pady=15)

root.mainloop()
