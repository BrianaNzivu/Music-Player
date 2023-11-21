import pygame
from pygame import mixer
from tkinter import *
import os
import random  # Import the random module

def playsong():
    currentsong = playlist.get(ACTIVE)
    print(currentsong)
    mixer.music.load(currentsong)
    songstatus.set("Playing")
    mixer.music.play()

def pausesong():
    songstatus.set("Paused")
    mixer.music.pause()

def stopsong():
    songstatus.set("Stopped")
    mixer.music.stop()

def resumesong():
    songstatus.set("Resuming")
    mixer.music.unpause()

def shufflesongs():
    # Get the current playlist and shuffle it
    current_playlist = list(playlist.get(0, END))
    random.shuffle(current_playlist)

    # Clear the current playlist and insert the shuffled songs
    playlist.delete(0, END)
    for s in current_playlist:
        playlist.insert(END, s)

root = Tk()
root.title('Music player project')

mixer.init()
songstatus = StringVar()
songstatus.set("Choosing")

# playlist---------------
playlist = Listbox(root, selectmode=SINGLE, bg="DodgerBlue2", fg="white", font=('arial', 15), width=40)
playlist.grid(columnspan=5)

os.chdir(r'C:\Users\Briana\Desktop\MyPlaylist')
songs = os.listdir()
for s in songs:
    playlist.insert(END, s)

playbtn = Button(root, text="Play", command=playsong)
playbtn.config(font=('arial', 20), bg="DodgerBlue2", fg="white", padx=7, pady=7)
playbtn.grid(row=1, column=0)

pausebtn = Button(root, text="Pause", command=pausesong)
pausebtn.config(font=('arial', 20), bg="DodgerBlue2", fg="white", padx=7, pady=7)
pausebtn.grid(row=1, column=1)

stopbtn = Button(root, text="Stop", command=stopsong)
stopbtn.config(font=('arial', 20), bg="DodgerBlue2", fg="white", padx=7, pady=7)
stopbtn.grid(row=1, column=2)

resumebtn = Button(root, text="Resume", command=resumesong)
resumebtn.config(font=('arial', 20), bg="DodgerBlue2", fg="white", padx=7, pady=7)
resumebtn.grid(row=1, column=3)

shufflebtn = Button(root, text="Shuffle", command=shufflesongs)
shufflebtn.config(font=('arial', 20), bg="DodgerBlue2", fg="white", padx=7, pady=7)
shufflebtn.grid(row=1, column=4)

mainloop()
