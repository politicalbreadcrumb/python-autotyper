import pyautogui
import tkinter
import time
from tkinter import *

#i know nothing impressive just coded for fun
#if anyone wants to actually use this use 'pip install pyautogui' to install neccessary packages

def type():
    text = entryField.get()
    userDelay = int(entryFieldTwo.get())


    time.sleep(userDelay)
    pyautogui.write(text)


root = Tk()

root.geometry("600x600")
root.title("Automatic text inputter ")

label = tkinter.Label(root, text="Enter your text in the text box and hit the button (enter your input delay and then select a entry field)")
label.pack()

entryField = Entry(root)
entryField.pack()


label2 = Label(root, text="Below me is the input delay field (integers only otherwise it wont work)")
label2.pack()

entryFieldTwo = Entry(root)
entryFieldTwo.pack()

btn = tkinter.Button(root, text="click me!", command=type)
btn.place(x=0, y=50)

root.mainloop()
