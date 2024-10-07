from tkinter import Tk, Button
from conch_bot import magic_conch, stop_magic_conch

bot_running = False

def start_bot():
    global bot_running
    if not bot_running:
        magic_conch()
        bot_running = True

def stop_bot():
    global bot_running
    if bot_running:
        stop_magic_conch()
        bot_running = False
        root.quit()

def launch_gui():
    # Create the GUI window
    global root
    root = Tk()
    root.title("Magic Conch Bot")

    # Create the Start button
    start_button = Button(root, text= "Start", command = start_bot, bg = "#61d408", fg = "white")
    start_button.pack(pady = 20)

    # Create the Quit button
    quit_button = Button(root, text= "Quit", command = stop_bot, bg = "red", fg = "white")
    quit_button.pack(pady = 20)

    # Start the Tkinter
    root.mainloop()


