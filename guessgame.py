import customtkinter as ctk 
import random


ctk.set_appearance_mode("dark")
ctk.set_appearance_mode("blue")

numero_secreto = None
intentos_restantes = 0
intenos_realizados = 0

#Funciones del juego

def iniciar_juego(dificultad):
    global numero_secreto, intentos_restantes , intenos_realizados

    intentos_realizados = 0
    numero_secreto = random.randint(1, 100)

    if dificultad == "Fácil":
        intentos_restantes = 10
    elif dificultad == "Media":
        intentos_restantes = 5
    else:
        intentos_restantes = 3   


        etiqueta_estado.configure(
        text=f"Dificultad: {dificultad}\nIntentos restantes: {intentos_restantes}"
    )
    etiqueta_mensaje.configure(
        text="Adivina un número entre 1 y 100"
    )
    entrada_numero.delete(0, "end")
    boton_adivinar.configure(state="normal")
