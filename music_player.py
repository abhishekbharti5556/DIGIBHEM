# music_player.py
import tkinter as tk
from player_controls import PlayerControls

if __name__ == "__main__":
    root = tk.Tk()
    app = PlayerControls(root)
    root.mainloop()
