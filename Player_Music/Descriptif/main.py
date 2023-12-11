
from tkinter import *
import pygame
from tkinter import filedialog
import os
from PIL import Image, ImageTk

root = Tk()
root.title("Player Music")
root.geometry("500x300")

pygame.mixer.init()

menubar = Menu(root)
root.config(menu=menubar)

songs = []
morceau_en_cours = ""
pause = False

def subir_musica():
    global morceau_en_cours
    root.directory = filedialog.askdirectory()

    for piste in os.listdir(root.directory):
        name, ext = os.path.splitext(piste)
        if ext == '.mp3':
            songs.append(piste)

    for piste in songs:
        songlist.insert("end", piste)

    songlist.select_set(0)
    morceau_en_cours = songs[songlist.curselection()[0]]

def play_music():
    global morceau_en_cours, paused

    if not paused:
        pygame.mixer.music.load(os.path.join(root.directory, morceau_en_cours))
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.play()
        paused = False

def stop_music():
    global paused
    pygame.mixer.music.pause()
    paused = True

def next_music():
    global morceau_en_cours, paused

    try:
        songlist.selection_clear(0, END)
        songlist.select_set(songs.index(morceau_en_cours) + 1)
        morceau_en_cours = songs[songlist.curselection()[0]]
        play_music()
    except:
        pass

def prev_music():
        global morceau_en_cours, paused

        try:
            songlist.selection_clear(0, END)
            songlist.select_set(songs.index(morceau_en_cours) - 1)
            morceau_en_cours = songs[songlist.curselection()[0]]
            play_music()
        except:
            pass

organisation_menu = Menu(menubar, tearoff=False)
organisation_menu.add_command(label='Choisir Piste', command=subir_musica)
menubar.add_cascade(label='Ajouter une Piste', menu=organisation_menu)

songlist = Listbox(root, bg="darkblue", fg="black", width=100, height=15)
songlist.pack()



# Cargar imágenes con PIL y convertirlas a PhotoImage
play_img = Image.open("C:/Users/maxyb/Player_Music/Player_Music/Descriptif/play.png")
stop_img = Image.open("C:/Users/maxyb/Player_Music/Player_Music/Descriptif/stop.png")
next_img = Image.open("C:/Users/maxyb/Player_Music/Player_Music/Descriptif/siguiente.png")
prev_img = Image.open("C:/Users/maxyb/Player_Music/Player_Music/Descriptif/anterior.png")

'''

# Obtener el directorio actual del script
script_directory = os.path.dirname(__file__)

# Cargar imágenes con rutas de archivo relativas
play_img = Image.open(os.path.join(script_directory, "Descriptif/play.png"))
stop_img = Image.open(os.path.join(script_directory, "Descriptif/stop.png"))
next_img = Image.open(os.path.join(script_directory, "Descriptif/siguiente.png"))
prev_img = Image.open(os.path.join(script_directory, "Descriptif/anterior.png"))

'''

play_btn_image = ImageTk.PhotoImage(play_img)
stop_btn_image = ImageTk.PhotoImage(stop_img)
next_btn_image = ImageTk.PhotoImage(next_img)
prev_btn_image = ImageTk.PhotoImage(prev_img)

control_frame = Frame(root)
control_frame.pack()

#Asignar imagenes a los botones
play_btn = Button(control_frame, image=play_btn_image, borderwidth=0, command=play_music)
stop_btn = Button(control_frame, image=stop_btn_image, borderwidth=0, command=stop_music)
next_btn = Button(control_frame, image=next_btn_image, borderwidth=0, command=next_music)
prev_btn = Button(control_frame, image=prev_btn_image, borderwidth=0, command=prev_music)

play_btn.grid(row=0, column=1, padx=7, pady=10)
stop_btn.grid(row=0, column=2, padx=7, pady=10)  
next_btn.grid(row=0, column=3, padx=7, pady=10)
prev_btn.grid(row=0, column=0, padx=7, pady=10)

root.mainloop()

# Esperar unos segundos antes de que el script termine
timesleep(5)