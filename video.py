import tkinter as tk
from tkinter import ttk
from moviepy.editor import VideoFileClip

def play_video(filename):
    video = VideoFileClip(filename)
    video.preview()

root = tk.Tk()
frame = ttk.Frame(root)
frame.pack()

filename = "Images/lower_left.mp4"  # Replace with your MP4 file path

# Create a button to play the video
button = ttk.Button(frame, text="Play Video", command=lambda: play_video(filename))
button.pack()

root.mainloop()
