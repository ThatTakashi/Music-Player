from tkinter import *
from customtkinter import *
from PIL import ImageTk, Image  
import ctypes as ct
from pygame import mixer

root = CTk()
x = root.winfo_screenwidth() - 420
y = root.winfo_screenheight() - 210

set_default_color_theme("colours.json")
set_appearance_mode("dark")

mixer.init()

width = 400
height = 120

def playlist_window():
    playlist_win = CTkToplevel()

root.geometry('%dx%d+%d+%d' % (width, height, x, y))
root.resizable(False, False)
root.title("Tuned")

img2 = ImageTk.PhotoImage(Image.open("icon.png"))
panel2 = Label(root, image = img2, borderwidth=0)
panel2.place(relx=0.03, rely=0.5, anchor=W)

artist = CTkLabel(root, text = "Artist", bg_color="transparent")
artist.place(rely = 0.4, relx = 0.6, anchor = "center")

title = CTkLabel(root, text = "Song Title", font=("Raleway", 20))
title.place(rely = 0.2, relx = 0.6, anchor = "center")


play = CTkImage(light_image=Image.open("play.png"), dark_image=Image.open("play.png"), size=(25, 25))
button1 = CTkButton(root, text='', width=5, image = play, command=lambda: [mixer.music.load('test.mp3'), mixer.music.play()])
button1.place(rely = 0.65, relx = 0.6, anchor = "center")

next = CTkImage(light_image=Image.open("next.png"), dark_image=Image.open("next.png"), size=(23, 23))
button2 = CTkButton(root, text='', width=5, image = next, command=mixer.music.pause())
button2.place(rely = 0.66, relx = 0.75, anchor = "center")

previous = CTkImage(light_image=Image.open("previous.png"), dark_image=Image.open("previous.png"), size=(23, 23))
button3 = CTkButton(root, text='', width=5, image = previous)
button3.place(rely = 0.66, relx = 0.45, anchor = "center")

add = CTkButton(root, text='+', width=5)
add.place(rely = 0.05, relx = 0.9, anchor = "ne")

settings = CTkButton(root, text='s', width=5)
settings.place(rely = 0.05, relx = 0.99, anchor = "ne")

root.mainloop()