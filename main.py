import os
from pytube import YouTube
from pytube import Playlist
import tkinter as tk
from tkinter import *
  

def get_a_song():
    music_to_dl = musique_entry.get()
    song_to_dl = YouTube(music_to_dl)
    destination = path_entry.get().strip()
    os.makedirs(destination, exist_ok=True)
    out_file = song_to_dl.streams.first().download(output_path=destination)
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)


def get_playlist():
    playlist_to_dl = musique_entry.get()
    p = Playlist(playlist_to_dl)
    destination = path_entry.get().strip()
    os.makedirs(destination, exist_ok=True)
    for video in p.videos:
        video.streams.get_audio_only(subtype='mp3')
        video.streams.get_highest_resolution()
        out_file = video.streams.get_audio_only().download(output_path=destination)

        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)


root = tk.Tk()
root.config(bg='#F9B78B')
root.title('Youtube To Mp3 converter')
root.minsize(720, 480)

frame1 = tk.Frame(root, bg='#F9B78B')
frame2 = tk.Frame(root, bg='#F9B78B')
frame3 = tk.Frame(root, bg='#F9B78B')
frame4 = tk.Frame(root, bg='#F9B78B')
frame5 = tk.Frame(root, bg='#F9B78B')

width = 500
height = 480
image = tk.PhotoImage(file="mp2.png")
canvas = tk.Canvas(frame5, height=height, width=width, bg='#F9B78B', bd=0, highlightthickness=0)
canvas.create_image(width / 2, height / 2, image=image)
canvas.pack()

label_title = tk.Label(frame1, text='Bienvenue sur Youtube to Mp3 converter, veuillez choisir une options : ',
                       font=('Courrier', 20), fg='black', bg='#F9B78B')
label_title.pack()

label_title2 = tk.Label(frame2, text='Coller le lien de votre média : ', font=('Courrier', 30), fg='black',
                        bg='#F9B78B', pady=20)
label_title2.pack()

musique_entry = Entry(frame2, bg='white')
musique_entry.pack()

label_title3 = tk.Label(frame2, text='Renseigner le chemin du dossier où stocker les fichiers : ',
                        font=('Courrier', 12), fg='black', bg='#F9B78B', pady=8)
label_title3.pack()

path_entry = Entry(frame2, bg='white')
path_entry.pack()

musique_button = tk.Button(frame3, text='Télécharger une seul musique', font=('Courrier', 15), bg='#F9B78B', fg='black', padx=10, command=get_a_song)
musique_button.pack(side=LEFT)

playlist_button = tk.Button(frame3, text='Télécharger Playlist', font=('Courrier', 15), bg='#F9B78B', fg='black', command=get_playlist)
playlist_button.pack(side=RIGHT)

frame1.pack(side=TOP)
frame5.pack()
frame2.pack(side=TOP)
frame3.pack(side=BOTTOM)

root.mainloop()
