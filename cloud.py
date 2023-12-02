import os
import tkinter as tk
from tkinter import filedialog
import pygame

class MusicPlayer:
    def __init__(self, master):
        self.master = master
        self.master.title("Music Player")
        self.master.geometry("400x200")

        self.playlist = []
        self.current_index = 0

        self.setup_ui()

    def setup_ui(self):
        # Create buttons
        self.play_button = tk.Button(self.master, text="Play", command=self.play_music)
        self.play_button.pack(pady=10)

        self.stop_button = tk.Button(self.master, text="Stop", command=self.stop_music)
        self.stop_button.pack(pady=10)

        self.next_button = tk.Button(self.master, text="Next", command=self.next_music)
        self.next_button.pack(pady=10)

        self.add_button = tk.Button(self.master, text="Add Song", command=self.add_song)
        self.add_button.pack(pady=10)

        # Create a listbox for the playlist
        self.listbox = tk.Listbox(self.master, selectmode=tk.SINGLE)
        self.listbox.pack(pady=10)

    def play_music(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.unpause()
        elif self.playlist:
            pygame.mixer.music.load(self.playlist[self.current_index])
            pygame.mixer.music.play()

    def stop_music(self):
        pygame.mixer.music.stop()

    def next_music(self):
        self.current_index = (self.current_index + 1) % len(self.playlist)
        self.play_music()

    def add_song(self):
        file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3;*.wav")])
        if file_path:
            self.playlist.append(file_path)
            song_name = os.path.basename(file_path)
            self.listbox.insert(tk.END, song_name)

def main():
    pygame.mixer.init()

    root = tk.Tk()
    app = MusicPlayer(root)
    root.mainloop()

if __name__ == "__main__":
    main()
