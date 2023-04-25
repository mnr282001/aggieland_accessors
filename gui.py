from tkinter import *
from os import system

root = Tk()  # Create a new Tkinter window
root.title("Aggieland Accessors")  # Set the title of the window
root.geometry("600x350")  # Set the initial dimensions of the window


def run():
    # Define a function to run the 'background.py' script when a button is clicked
    system('python3 background.py')


# Create a button with a text label and a command to run the 'run' function when clicked
btn_for_run = Button(
    root, text="Click Me to Start Detecting Color on Click! When you are done, click Escape!", command=run)

# Create a button with a text label, a border width of 5, and a command to close the window when clicked
btn_to_close = Button(root, text='Close me!', bd='5', command=root.destroy)
# Add the 'btn_for_run' button to the window with vertical padding of 15 pixels
btn_for_run.pack(pady=15)
# Add the 'btn_to_close' button to the window with vertical padding of 15 pixels
btn_to_close.pack(pady=15)

root.mainloop()  # Start the main event loop for the window, which handles user interactions and updates the window display
