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


lista = []
for i in range(50,200,10):
	lista.append(i)

def iniciar_reproduccion():
	global cancion_actual, direcion, pos, n, actualizar
	barra1['value'] = random.choice(lista)
	barra2['value'] = random.choice(lista)
	barra3['value'] = random.choice(lista)
	barra4['value'] = random.choice(lista)
	barra5['value'] = random.choice(lista)
	barra6['value'] = random.choice(lista)
	barra7['value'] = random.choice(lista)
	barra8['value'] = random.choice(lista)
	barra9['value'] = random.choice(lista)
	barra10['value'] = random.choice(lista)
	barra11['value'] = random.choice(lista)
	barra12['value'] = random.choice(lista)
	barra13['value'] = random.choice(lista)
	barra14['value'] = random.choice(lista)
	barra15['value'] = random.choice(lista)
	barra16['value'] = random.choice(lista)
	barra17['value'] = random.choice(lista)
	barra18['value'] = random.choice(lista)
	barra19['value'] = random.choice(lista)
	barra20['value'] = random.choice(lista)
