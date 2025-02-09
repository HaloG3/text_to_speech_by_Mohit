import os
import pygame
import glob
import tkinter as tk
from tkinter import messagebox
from gtts import gTTS

def text_to_speech():
    text = entry.get()
    if not text.strip():
        messagebox.showwarning("Warning", "Please enter some text!")
        return
    
    first_word = text.split()[0] if text.strip() else "audio"
    filename = f"{first_word}.mp3"
    tts = gTTS(text)
    tts.save(filename)
    messagebox.showinfo("Success", f"Audio saved as {filename}")

def play_audio():
    text = entry.get()
    if not text.strip():
        messagebox.showwarning("Warning", "Please enter some text first!")
        return
    
    first_word = text.split()[0] if text.strip() else "audio"
    filename = f"{first_word}.mp3"
    
    if not os.path.exists(filename):
        messagebox.showerror("Error", "Audio file not found!")
        return
    
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

def reset_text():
    entry.delete(0, tk.END)
    entry.insert(0, "Enter text")

def show_audio_files():
    audio_files = glob.glob("*.mp3")
    if audio_files:
        messagebox.showinfo("Recorded Audio Files", "\n".join(audio_files))
    else:
        messagebox.showinfo("No Files", "No audio files found!")

# GUI Setup
root = tk.Tk()
root.title("Text to Voice")
root.geometry("400x300")

entry = tk.Entry(root, width=40)
entry.insert(0, "Enter text")
entry.pack(pady=20)

btn_speak = tk.Button(root, text="Convert to Speech", command=text_to_speech)
btn_speak.pack(pady=5)

btn_play = tk.Button(root, text="Play", command=play_audio)
btn_play.pack(pady=5)

btn_reset = tk.Button(root, text="Reset", command=reset_text)
btn_reset.pack(pady=5)

btn_audio_list = tk.Button(root, text="Audio Files", command=show_audio_files)
btn_audio_list.pack(pady=5)

footer = tk.Label(root, text="Mohit Rao", font=("Arial", 10))
footer.pack(side=tk.BOTTOM, pady=10)

root.mainloop()
