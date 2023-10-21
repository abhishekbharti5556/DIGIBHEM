from tkinter import *
import os
import pygame
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

# Initialize the pygame mixer
pygame.mixer.init()

# Create the main window
root = tk.Tk()
root.title("Python Music Player")

# Create a list to store the playlist
playlist = []

# Create functions to control the player
def browse_music():
    global playlist
    file_paths = filedialog.askopenfilenames()
    for file_path in file_paths:
        playlist.append(file_path)
    playlist_box.delete(0, tk.END)
    for song in playlist:
        playlist_box.insert(tk.END, os.path.basename(song))

def play_music():
    if playlist:
        selected_song = playlist_box.curselection()[0]
        selected_song = playlist[int(selected_song)]
        pygame.mixer.music.load(selected_song)
        pygame.mixer.music.play()
        status_bar.config(text="Playing " + os.path.basename(selected_song))

def stop_music():
    pygame.mixer.music.stop()
    status_bar.config(text="Music Stopped")

def pause_music():
    pygame.mixer.music.pause()
    status_bar.config(text="Music Paused")

def unpause_music():
    pygame.mixer.music.unpause()
    status_bar.config(text="Playing " + os.path.basename(playlist_box.get(0)))

def set_volume(val):
    volume = int(val) / 100
    pygame.mixer.music.set_volume(volume)

def next_song():
    current_song_index = playlist_box.curselection()
    next_index = current_song_index[0] + 1
    if next_index < len(playlist):
        playlist_box.selection_clear(0, tk.END)
        playlist_box.select_set(next_index)
        play_music()

def previous_song():
    current_song_index = playlist_box.curselection()
    previous_index = current_song_index[0] - 1
    if previous_index >= 0:
        playlist_box.selection_clear(0, tk.END)
        playlist_box.select_set(previous_index)
        play_music()
def toggle_repeat():
    if pygame.mixer.music.get_busy():
        global repeat_mode
        repeat_mode = (repeat_mode + 1) % 3
        repeat_modes = ["Repeat Off", "Repeat One", "Repeat All"]
        repeat_button.config(text=repeat_modes[repeat_mode])

repeat_mode = 0  # 0: Off, 1: Repeat one, 2: Repeat all

# Create a "Repeat/Shuffle" button
def update_repeat_button():
    repeat_modes = ["Repeat Off", "Repeat One", "Repeat All"]
    repeat_button.config(text=repeat_modes[repeat_mode])

repeat_button = tk.Button(root, text="Repeat Off", width=15, height=3, font="Helvetica 12 bold", command=toggle_repeat, bg="grey", fg="red")
repeat_button.place(x=1200, y=200)

# Create a listbox to display the playlist
playlist_box = tk.Listbox(root, bg="black", fg="white", selectbackground="blue")
playlist_box.pack(fill="both")

# Create buttons for controls
Button1 = tk.Button(root, width=15, height=3, font="Helvetica 12 bold", text="PLAY", command=play_music, bg="black", fg="red")
Button1.place(x=10, y=200)

Button2 = tk.Button(root, width=15, height=3, font="Helvetica 12 bold", text="STOP", command=stop_music, bg="grey", fg="red")
Button2.place(x=180, y=200)

Button3 = tk.Button(root, width=15, height=3, font="Helvetica 12 bold", text="PAUSE", command=pause_music, bg="black", fg="red")
Button3.place(x=350, y=200)

Button4 = tk.Button(root, width=15, height=3, font="Helvetica 12 bold", text="UNPAUSE", command=unpause_music, bg="grey", fg="red")
Button4.place(x=520, y=200)

Button5 = tk.Button(root, width=15, height=3, font="Helvetica 12 bold", text="Previous", command=previous_song, bg="black", fg="red")
Button5.place(x=690, y=200)

Button6 = tk.Button(root, width=15, height=3, font="Helvetica 12 bold", text="Next", command=next_song, bg="grey", fg="red")
Button6.place(x=860, y=200)

Button7 = tk.Button(root, width=15, height=3, font="Helvetica 12 bold", text="Add Songs", command=browse_music, bg="black", fg="red")
Button7.place(x=1030, y=200)

# Create a status bar
status_bar = tk.Label(root, text="", bd=1, relief=tk.SUNKEN, anchor=tk.W)
status_bar.pack(side=tk.BOTTOM, fill=tk.X)
status_bar.place(x=0, y=167, relwidth=1)

# Create a volume slider
volume_scale = tk.Scale(root, from_=100, to=0, width=50, length=250, orient="vertical", label="Volume", command=set_volume, background="lightgray", troughcolor="black")
volume_scale.set(100)
pygame.mixer.music.set_volume(0.5)  # Set initial volume
volume_scale.pack()
volume_scale.place(x=1400, y=165)

root.mainloop()
