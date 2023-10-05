import tkinter as tk
from tkinter import filedialog
from moviepy.editor import VideoFileClip

def convert_video_to_audio():
    file_path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4")])
    if file_path:
        video_clip = VideoFileClip(file_path)
        audio_clip = video_clip.audio
        output_audio_path = 'output_audio.mp3'
        audio_clip.write_audiofile(output_audio_path)
        video_clip.close()
        audio_clip.close()

# Create a tkinter window
root = tk.Tk()
root.title("Video to Audio Converter")

# Create a button to select the video file
select_button = tk.Button(root, text="Select Video File", command=convert_video_to_audio)
select_button.pack()

# Start the tkinter main loop
root.mainloop()
