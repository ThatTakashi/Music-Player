from tkinter import *
from customtkinter import *

root = CTk()
root.geometry("300x500")

frame1 = CTkFrame(root, width=150, height=100)
frame1.place(relx=0.5, rely=0.5, anchor="center")

button1 = CTkButton(frame1, text="test")
button1.place(rely=0.5, relx=0.5, anchor="center")

root.mainloop()
