from tkinter.font import BOLD
import sounddevice as sd
import soundfile as sf
import numpy as np
import threading
from tkinter import *
from tkinter import simpledialog, filedialog, messagebox
import pygame
import os

# Global vars
recording = False
recorded_data = []
fs = 48000
audio_file = None

bgcolor = "#90e0ef"
btcolor = "#0077b6"

#Start Voice Record
def Voice_rec_start():
    global recording, recorded_data
    recording = True
    recorded_data = []
    recording_label.config(text="Recording...", fg="red")
    
    def record():
        global recorded_data
        with sd.InputStream(samplerate=fs, channels=1) as stream:
            while recording:
                data, overflowed = stream.read(1024)
                recorded_data.append(data)
    
    thread = threading.Thread(target=record)
    thread.start()

#Stop Voice Record
def Voice_rec_stop():
    global recording
    recording = False
    recording_label.config(text="")
    
    file_name = simpledialog.askstring("Save File", "Enter the name of the audio file (without extension):")
    if file_name:
        file_path = os.path.join(os.getcwd(), f"recordings/{file_name}.wav")
        
        audio_data = np.concatenate(recorded_data, axis=0)
        sf.write(file_path, audio_data, fs)
        messagebox.showinfo("Success", f"Recording saved as '{file_path}'")
    else:
        messagebox.showwarning("Error", "File name not provided.")

#Open Audio File
def open_audio_player():
    global audio_file
    audio_file = filedialog.askopenfilename(filetypes=[("Audio Files", "*.wav")])

    player_window = Toplevel(master)
    player_window.title("Audio Player")
    player_window.geometry("360x220")
    player_window.configure(bg=bgcolor)

    if not audio_file:
        messagebox.showwarning("Error", "No audio file selected.")
        player_window.destroy()
        return

    play_button = Button(player_window, text="Play", bg=btcolor, fg="white", font=("Helvetica", 12))
    play_button.pack(pady=10, padx=10)

    pause_button = Button(player_window, text="Pause", bg=btcolor, fg="white", font=("Helvetica", 12))
    pause_button.pack(pady=5, padx=10)

    resume_button = Button(player_window, text="Resume", bg=btcolor, fg="white", font=("Helvetica", 12))
    resume_button.pack(pady=5, padx=10)

    progress = Scale(player_window, from_=0, to=100, orient="horizontal", length=200, showvalue=0, bg="#ffffff", fg="#000000", sliderlength=20, font=("Helvetica", 10))
    progress.pack(pady=10)

    pygame.mixer.init()

    #Play File
    def play_audio():
        pygame.mixer.music.load(audio_file)
        pygame.mixer.music.play()
        play_button.config(state=DISABLED)
        pause_button.config(state=NORMAL)
        update_progress()

    #Pause File Playing
    def pause_audio():
        pygame.mixer.music.pause()
        pause_button.config(state=DISABLED)
        resume_button.config(state=NORMAL)

    #Resume File Playing
    def resume_audio():
        pygame.mixer.music.unpause()
        resume_button.config(state=DISABLED)
        pause_button.config(state=NORMAL)

    #move bar as per file playing
    def update_progress():
        if pygame.mixer.music.get_busy():
            current_time = pygame.mixer.music.get_pos() / 1000
            sound_length = pygame.mixer.Sound(audio_file).get_length()
            progress.set((current_time / sound_length) * 100)
            player_window.after(1000, update_progress)

    play_button.config(command=play_audio)
    pause_button.config(command=pause_audio)
    resume_button.config(command=resume_audio)

#Main App
master = Tk()
master.title("Voice Recorder")
master.geometry("320x220")
master.configure(bg=bgcolor)

Label(master, text="Voice Recorder:", bg=bgcolor, font=("Helvetica", 14)).grid(row=0, sticky=W, padx=10, pady=10)

start_button = Button(master, text="Start Recording", command=Voice_rec_start, bg=btcolor, fg="white", font=("Helvetica", 12))
start_button.grid(row=1, column=0, padx=10, pady=10)

stop_button = Button(master, text="Stop Recording", command=Voice_rec_stop, bg=btcolor, fg="white", font=("Helvetica", 12))
stop_button.grid(row=1, column=1, padx=10, pady=10)

play_button = Button(master, text="Open Audio Player", command=open_audio_player, bg=btcolor, fg="white", font=("Helvetica", 12))
play_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

recording_label = Label(master, text="", bg=bgcolor, fg=btcolor ,font=("Helvetica", 12,BOLD))
recording_label.grid(row=3, column=0, columnspan=2, pady=10)

mainloop()