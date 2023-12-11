
import pygame
# from pygame import mixer
from tkinter import *


class lecteur():
    pygame.init()
    pygame.mixer.init()

    #Pasamos a crear una ventana
    win = pygame.display.set_mode((400, 300))
    pygame.display.set_caption("Lecteur Audio")

    #Definimos los colores
    Blanc = (255, 255, 255)
    Noir = (0, 0, 0)

    #Cargamos la fuente de caracteres
    pygame.font.init()
    fuente = pygame.font.SysFont(None, 24)

    #Variables
    piste_audio = None
    volume_audio = 0.5
    lecture_en_cours = False
    lecture_en_boucle = False
    file_queue = []

    #Elegimos una pista de audio
    def choisir_piste():
        global piste_audio
        file = pygame.filedialog.askopenfile(filetypes=[("Fichiers audio", "*.mp3;*.wav")])
        if file:
            piste_audio = pygame.mixer.music.load(file)

    #Leer el archivo
    def play(): 
        global lecture_en_cours
        if piste_audio:
            pygame.mixer.music.play()
            lecture_en_cours = True

    #Pausar el archivo
    def pausa():
        global lecture_en_cours
        if lecture_en_cours:
            pygame.mixer_music.pause()
            lecture_en_cours = False

    #Parar el archivo(stop)
    def stop():
        global lecture_en_cours
        if lecture_en_cours:
            pygame.mixer_music.stop()
            lecture_en_cours = False

    #Manipular el volumen
    def increase_volume():
        global volume_audio
        if volume_audio < 1.0:
            volume_audio += 0.1
            pygame.mixer.music.set_volume(volume_audio)

    def decrease_volume():
        global volume_audio
        if volume_audio > 0.0:
            volume_audio -= 0.1
            pygame.mixer.music.set_volume(volume_audio)

    #Leer en bucle un archivo
    def lire_en_boucle():
        global lecture_en_boucle
        if piste_audio:
            pygame.mixer_music.play(-1)
            lecture_en_boucle = False

    #Agregar una pista audio a la cola
    def ajouter_piste():
        file = pygame.filedialog.askopenfile(filetypes=[("Fichiers audio", "*.mp3;*.wav")])
        if file:
            file.queue.append(file)

    #Eliminar una pista audio
    def supprimer_piste():
        global piste_audio
        if piste_audio:
            pygame.mixer_music.stop()
            piste_audio = None

    #bucle principal
    running = True
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                #Verificar si el boton "choisir piste" se ha pulsado
                if 50 <= mouse_pos[0] <= 100 and 50 <= mouse_pos[1] <= 80:
                    choisir_piste()
                
                #Verificar si el boton "play" se ha pulsado
                elif 50 <= mouse_pos[0] <= 80 and 100 <= mouse_pos[1] <= 130:
                    play()

                #Lo mismo con "Pausa"
                elif 90 <= mouse_pos[0] <= 120 and 100 <= mouse_pos[1] <= 130:
                    pausa()

                #"Stop"
                elif 130 <= mouse_pos[0] <= 160 and 100 <= mouse_pos[1] <= 13:
                    stop()

                #Volumen
                elif 200 <= mouse_pos[0] <= 230 and 100 <= mouse_pos[1] <= 13:
                    increase_volume()
                elif 240 <= mouse_pos[0] <= 270 and 100 <= mouse_pos[1] <= 130:
                    decrease_volume()

                #Bucle
                elif 280 <= mouse_pos[0] <= 310 and 100 <= mouse_pos[1] <= 130:
                    lire_en_boucle()
                
                # Agregar pista
                elif 50 <= mouse_pos[0] <= 180 and 150 <= mouse_pos[1] <= 180:
                    ajouter_piste()

                # Eliminar pista
                elif 200 <= mouse_pos[0] <= 330 and 150 <= mouse_pos[1] <= 180:
                    supprimer_piste()

        #Borrar la pantalla
        win.fill(Blanc)

        #Montar los botones
        pygame.draw.rect(win, Noir, (50, 50, 130, 30))
        pygame.draw.rect(win, Noir, (50, 100, 30, 30))
        pygame.draw.rect(win, Noir, (90, 100, 30, 30))
        pygame.draw.rect(win, Noir, (130, 100, 30, 30))
        pygame.draw.rect(win, Noir, (200, 100, 30, 30))
        pygame.draw.rect(win, Noir, (240, 100, 30, 30))
        pygame.draw.rect(win, Noir, (280, 100, 30, 30))
        pygame.draw.rect(win, Noir, (50, 150, 130, 30))
        pygame.draw.rect(win, Noir, (200, 150, 130, 30))

        #Agregar el texto de los botones
        texto_pista = fuente.render("Choisir piste", True, Blanc)
        win.blit(texto_pista, (55, 55))

        stop_texto = fuente.render("Stop", True, Blanc)
        win.blit(stop_texto, (135, 105))

        text_increase_volume = fuente.render("V+", True, Blanc)
        win.blit(text_increase_volume, (205, 105))

        text_dicrease_volume = fuente.render("V-", True, Blanc)
        win.blit(text_dicrease_volume, (245, 105))

        text_ajouter_piste = fuente.render("+", True, Blanc)
        win.blit(text_ajouter_piste, (55, 105))

        text_supprimer_piste = fuente.render("Supprimer Piste", True, Blanc)
        win.blit(text_supprimer_piste, (205, 155))

        if lecture_en_cours:
            texto_parado = fuente.render("Pause", True, Blanc)
            win.blit(texto_parado, (95, 105))
        else:
            play_texto = fuente.render("Play", (95, 105), Blanc)
            win.blit(play_texto, (95, 105))

        if lecture_en_boucle:
            text_lire_en_boucle = fuente.render("Loop", True, Blanc)
            win.blit(text_lire_en_boucle, (285, 105))

        #Actualizar pantalla
        pygame.display.flip()

    #Ajustar la velocidad del bucle
    clock.tick(60)

    #Cerrar la ventana pygame
pygame.quit()

lecteur.running()