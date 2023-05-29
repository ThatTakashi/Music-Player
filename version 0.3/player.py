from tkinter import *
from tkinter import filedialog
from customtkinter import *
from PIL import ImageTk, Image  
from pygame import mixer

root = CTk()
x = root.winfo_screenwidth() - 420
y = root.winfo_screenheight() - 210

set_default_color_theme("colours.json")
set_appearance_mode("dark")

mixer.init()

music_list = []

width = 400
height = 120

def add_music():
    file_path = filedialog.askopenfilename(filetypes=[("MP3 Music files", "*.mp3"), ("Wave Audio files", "*.wav")])
    music_list.append(file_path)
    print(music_list)

def playlist_window():
    playlist_win = CTkToplevel()

    playlist_win.title("Playlist | Tuned")

    x = playlist_win.winfo_screenwidth() / 2 - 200
    y = playlist_win.winfo_screenheight() / 2 - 200

    playlist_win.geometry('400x400+%d+%d' % (x,y))

    title = CTkLabel(playlist_win, text = "Queue", font=("Raleway", 20))
    title.pack(fill="x", anchor = "center", pady = 50)

    test = 4

    add_button = CTkButton(playlist_win, text="+", command=add_music)
    add_button.pack()

    for i in range(test):
        label = CTkLabel(playlist_win, text = f"song No {i}")
        label.pack()

def settings_window():
    settings_win = CTkToplevel()

    settings_win.title("Settings | Tuned")

    x = settings_win.winfo_screenwidth() / 2 - 200
    y = settings_win.winfo_screenheight() / 2 - 200

    settings_win.geometry('400x400+%d+%d' % (x,y))
    settings_win.resizable(False, False)

    title = CTkLabel(settings_win, text = "Application Settings", font=("Raleway", 20))
    title.place(relx = 0.5, rely = 0.1, anchor="center")

    volume = CTkLabel(settings_win, text = "Player Volume")
    volume.place(relx = 0.5, rely = 0.2, anchor="center")

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
button1 = CTkButton(root, text='', width=5, image = play, command=lambda: [mixer.music.load('test.mp3'), mixer.music.play(), print("Music Playing!")])
button1.place(rely = 0.65, relx = 0.6, anchor = "center")

next = CTkImage(light_image=Image.open("next.png"), dark_image=Image.open("next.png"), size=(23, 23))
button2 = CTkButton(root, text='', width=5, image = next, command=mixer.music.pause())
button2.place(rely = 0.66, relx = 0.75, anchor = "center")

previous = CTkImage(light_image=Image.open("previous.png"), dark_image=Image.open("previous.png"), size=(23, 23))
button3 = CTkButton(root, text='', width=5, image = previous)
button3.place(rely = 0.66, relx = 0.45, anchor = "center")

add = CTkButton(root, text='+', width=5, command = playlist_window)
add.place(rely = 0.05, relx = 0.9, anchor = "ne")

settings = CTkButton(root, text='s', width=5, command = settings_window)
settings.place(rely = 0.05, relx = 0.99, anchor = "ne")

root.mainloop()