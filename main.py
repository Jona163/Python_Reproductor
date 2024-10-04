# Autor: Jonathan Hernández
# Fecha: 03 Octubre 2024
# Descripción: Código para Reproductor de musica.
# GitHub: https://github.com/Jona163


from tkinter import Button, Label,Tk,filedialog, ttk, Frame, PhotoImage
import pygame
import random
import mutagen

pygame.mixer.init()
pygame.mixer.init(frequency=44100)
cancion_actual =''
direcion = ''

def abrir_archivo():
	global direcion, pos, n,cancion_actual
	pos = 0
	n = 0
	direcion = filedialog.askopenfilenames(initialdir ='/', 
											title='Escoger la cancion(es)', 
										filetype=(('mp3 files', '*.mp3*'),('All files', '*.*')))
	n = len(direcion)
	cancion_actual = direcion[pos]

	nombre_cancion = cancion_actual.split('/')
	nombre_cancion = nombre_cancion[-1]
