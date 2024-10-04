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


	cancion_actual = direcion[pos]
	nombre_cancion = cancion_actual.split('/')
	nombre_cancion = nombre_cancion[-1]
	nombre['text']= nombre_cancion

	time = pygame.mixer.music.get_pos()
	x = int(int(time)*0.001)
	tiempo['value']= x  #posicion de la cancion

	y = float(int(volumen.get())*0.1)
	pygame.mixer.music.set_volume(y)
	nivel['text']= int(y*100)

	audio = mutagen.File(cancion_actual)	
	log = audio.info.length
	minutos, segundos = divmod(log, 60)

	minutos, segundos = int(minutos), int(segundos)
	tt = minutos*60 + segundos
	tiempo['maximum']= tt  # tiempo total de la cancion
	texto['text']= str(minutos) + ":" + str(segundos)
	
	actualizar = ventana.after(100 , iniciar_reproduccion)


	if x == tt:
		ventana.after_cancel(actualizar)
		texto['text']= "00:00"
		detener_efecto()
		if pos != n:
			pos = pos + 1
			ventana.after(100 , iniciar_reproduccion)
			pygame.mixer.music.play()
		if pos == n:
			pos = 0

def iniciar():
	global cancion_actual
	pygame.mixer.music.load(cancion_actual)
	pygame.mixer.music.play()
	iniciar_reproduccion()


def retroceder():
	global pos,n

	if pos >0:
		pos = pos-1
	else:
		pos = 0
	cantidad['text'] = str(pos)+'/'+str(n)

def adelantar():
	global pos, n

	if pos == n-1:
		pos = 0
	else:
		pos = pos + 1
	cantidad['text'] = str(pos)+'/'+str(n)



def detener_efecto():
	barra1['value'] = 50
	barra2['value'] = 60
	barra3['value'] = 70
	barra4['value'] = 80
	barra5['value'] = 90
	barra6['value'] = 100
	barra7['value'] = 90
	barra8['value'] = 80
	barra9['value'] = 70
	barra10['value'] = 60
	barra11['value'] = 60
	barra12['value'] = 70
	barra13['value'] = 80
	barra14['value'] = 90
	barra15['value'] = 100
	barra16['value'] = 90
	barra17['value'] = 80
	barra18['value'] = 70
	barra19['value'] = 60
	barra20['value'] = 50


def stop():
	global actualizar
	pygame.mixer.music.stop()
	ventana.after_cancel(actualizar)
	detener_efecto()   
def pausa():
	global actualizar
	pygame.mixer.music.pause()
	ventana.after_cancel(actualizar)
	detener_efecto()
def continuar():
	pygame.mixer.music.unpause()
	ventana.after(100 , iniciar_reproduccion)
