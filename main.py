# -*- coding: utf-8 -*-
import pyautogui as pg
import tkinter as tk
import threading
import time
import random

time.sleep(5)

# Crear ventana y elementos de la interfaz
ventana = tk.Tk()
ventana.title("Generador de Comentarios para Instagram")
ventana.geometry("1000x700")


comentarios_floripa = [
    "cosas que no pueden faltar en el cielo",
    "Mesa de pool",
    "Esparragos",
    "Una tuna seca",
    "Pistola de agua",
    "Pelota",
    "cosas que no pueden faltar en el paraíso",
    "LLeven mas de 2 calzoncillos",
    "LLeven mas de 2 medias",
    "Lleven ropa",
    "Cucharas luminosas",
    "Calcetines parlantes",
    "Paraguas saltarines",
    "Tostadora musical",
    "Pelota de boliche emplumada",
    "Planta beatbox",
    "Reloj aleatorio",
    "Espejo halagador",
    "Silla solar",
    "Piedra sonriente",
    "Sombrero saltarin",
    "Lapiz imborrable",
    "Cepillo que canta",
    "Panuelo flotante",
    "Boligrafo multicolor",
    "Libro que cambia",
    "Globo rebota",
    "Cama nube",
    "Sombrilla voladora",
    "Zapatos intercambiables",
    "Lampara bailarina",
    "Caja eco",
    "Martillo musical",
    "Papel autoadhesivo",
    "Taza autorecalentable",
    "Cinta metrica elastica",
    "Silla flotante",
    "Perfume hipnotico",
    "Reloj que adelanta horas",
    "Cama elastica",
    "Bolso interdimensional",
    "Espejo que muestra el futuro",
    "Cepillo magnetico",
    ]

instrucciones = """
Instrucciones:
1. Abre la publicación en Instagram donde deseas comentar.
2. Posiciónate en el campo de comentarios.
3. Haz clic en el botón 'Iniciar' para comenzar la generación de comentarios.
4. Tienes 5 segundos para ir a la publicacion y dejar el clickeado en agregar comentarios.
5. El programa escribirá automáticamente comentarios en intervalos aleatorios.
6. Si deseas detener la generación, haz clic en el botón 'Detener'.

7- llevar la vaca a floripa 

advertencia: si sacas el click del input va a dejar de funcionar
"""

instrucciones_label = tk.Label(ventana, text=instrucciones, justify="left")
instrucciones_label.pack()

# Variable para controlar la ejecución del programa
# contador
ejecucion_activa = False
contador_comentarios = 0
tiempo_restante = 5


def actualizar_contador_thread(texto):
    contador_label.config(text=texto)


def enviar_comentario():
    global tiempo_restante
    global ejecucion_activa
    global contador_comentarios
    estado_label.config(text="Ejecutando...")

    while tiempo_restante > 0 and ejecucion_activa:
        actualizar_contador_thread(f"Comenzando en: {tiempo_restante}")
        ventana.update()
        time.sleep(1)
        tiempo_restante -= 1

    actualizar_contador_thread("")  # Limpiar el contador de inicio
    estado_label.config(text="Ejecutando...")

    while ejecucion_activa:
        comb_emoticon = random.choice(comentarios_floripa)

        try:
            pg.write(comb_emoticon)
            pg.press("enter")
            contador_comentarios += 1
        except:
            print("Error al interactuar con Instagram, dale detener al programa y vuelve a iniciarlo")
        tiempo_espera = random.uniform(59, 120)
        time.sleep(tiempo_espera)

    estado_label.config(text="Detenido")


def iniciar_programa():
    global ejecucion_activa
    if not ejecucion_activa:
        ejecucion_activa = True
        threading.Thread(target=enviar_comentario).start()


def detener_programa():
    global ejecucion_activa
    ejecucion_activa = False
    contador_label.config(text="")
    estado_label.config(text="Detenido")


def actualizar_contador():
    while True:
        contador_comentarios_label.config(text=f"Comentarios realizados durante la ejecución: {contador_comentarios}")
        ventana.update()
        time.sleep(1)


iniciar_button = tk.Button(ventana, text="Iniciar", command=iniciar_programa, bg="green")
iniciar_button.pack()

detener_button = tk.Button(ventana, text="Detener", command=detener_programa, bg="red")
detener_button.pack()

# Resto de la interfaz y definiciones de botones

contador_label = tk.Label(ventana, text="", font=("Arial", 14))
contador_label.pack()

estado_label = tk.Label(ventana, text="Detenido", font=("Arial", 14))
estado_label.pack()

contador_comentarios_label = tk.Label(ventana, text="", font=("Arial", 14))
contador_comentarios_label.pack()

threading.Thread(target=actualizar_contador).start()

# Bucle de la interfaz
ventana.mainloop()
