# SpongeBob Text Generator

# This will be the main program, mostly tkinter code.

from tkinter import *  # To import all the tkinter functions
from functions import *  # To import all the functions module functions
import pyperclip


# Functions to make the program work go here
def spongebob_conversion():
    text_input = entry_text.get('1.0', END)
    text_output = spongeBobTextConversion(text_input).rstrip('\n')
    entry_text.delete('1.0', END)
    entry_text.insert('1.0', text_output)


def copy_text():
    pyperclip.copy(entry_text.get('1.0', END))  # This will copy the text from the entry field into the user's clipboard


def paste_text():
    clipboard_text = pyperclip.paste()  # This will save the text from the users clipboard
    entry_text.delete('1.0', END)
    entry_text.insert('1.0', clipboard_text)


def clear_text():
    entry_text.delete('1.0', END)


# Constants for the tkinter layout here
padding_ext = 5
padding_int = 2

# Main window information here
window = Tk()
window.title('SpongeBob Text Conversion')

# Row and Column configurations
window.rowconfigure(1, weight=1)
window.columnconfigure(0, weight=1)

# Elements within the program, and their positioning
frame_title = Frame(master=window)
entry_text = Text(master=window)
frame_buttons = Frame(master=window)
label_title = Label(master=frame_title, text='SpongeBob Text Conversion')
button_conv = Button(master=frame_buttons, text='Convert', width=10, command=spongebob_conversion)
button_copy = Button(master=frame_buttons, text='Copy', width=10, command=copy_text)
button_paste = Button(master=frame_buttons, text='Paste', width=10, command=paste_text)
button_clear = Button(master=frame_buttons, text='Clear', width=10, command=clear_text)

frame_title.grid(row=0, column=0)
entry_text.grid(row=1, column=0, padx=padding_ext, pady=padding_ext)
frame_buttons.grid(row=1, column=1)
label_title.pack(padx=padding_ext, pady=(padding_ext, 0))
button_conv.pack(padx=(0, padding_ext), pady=(0, 30), ipadx=padding_int, ipady=padding_int)
button_copy.pack(padx=(0, padding_ext), pady=(padding_ext, 0), ipadx=padding_int, ipady=padding_int)
button_paste.pack(padx=(0, padding_ext), pady=(padding_ext, 0), ipadx=padding_int, ipady=padding_int)
button_clear.pack(padx=(0, padding_ext), pady=(padding_ext, 0), ipadx=padding_int, ipady=padding_int)

window.mainloop()

# End - 22/02/2021

# FUTURE WORK OR FURTHER ITERATIONS
# No new ideas for this one, might have taken this program about as far as it can go
