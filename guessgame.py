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

def comprobar_intento():
    global intentos_restantes, intentos_realizados

    try:
        intento = int(entrada_numero.get())
    except ValueError:
        etiqueta_mensaje.configure(
            text="Por favor ingresa un número válido"
        )
        return

    intentos_realizados += 1
    intentos_restantes -= 1

    if intento == numero_secreto:
        etiqueta_mensaje.configure(
            text=f" ¡Ganaste! Adivinaste el número en {intentos_realizados} intentos"
        )
        boton_adivinar.configure(state="disabled")
        return

    if intentos_restantes == 0:
        etiqueta_mensaje.configure(
            text=f"Juego terminado. El número era {numero_secreto}"
        )
        boton_adivinar.configure(state="disabled")
        return

    if intento < numero_secreto:
        etiqueta_mensaje.configure(
            text="El número es mayor"
        )
    else:
        etiqueta_mensaje.configure(
            text="El número es menor"
        )

    etiqueta_estado.configure(
        text=f"Intentos restantes: {intentos_restantes}"
    )

#Ventana principal
app = ctk.CTk()
app.title("Adivina el Número")
app.geometry("420x500")
app.resizable(False, False)

#Interfaz de la app
titulo = ctk.CTkLabel(
    app,
    text="Adivina el Número",
    font=("Arial", 20, "bold")
)
titulo.pack(pady=20)

etiqueta_dificultad = ctk.CTkLabel(
    app,
    text="Selecciona la dificultad"
)
etiqueta_dificultad.pack()

menu_dificultad = ctk.CTkOptionMenu(
    app,
    values=["Fácil", "Medio", "Difícil"],
    command=iniciar_juego
)
menu_dificultad.set("Fácil")
menu_dificultad.pack(pady=10)

etiqueta_estado = ctk.CTkLabel(app, text="")
etiqueta_estado.pack(pady=10)

entrada_numero = ctk.CTkEntry(
    app,
    width=200,
    justify="center",
    placeholder_text="Ingresa tu número"
)
entrada_numero.pack(pady=10)

boton_adivinar = ctk.CTkButton(
    app,
    text="Adivinar",
    command=comprobar_intento,
    state="disabled"
)
boton_adivinar.pack(pady=10)

etiqueta_mensaje = ctk.CTkLabel(
    app,
    text="Selecciona una dificultad para comenzar",
    wraplength=300
)
etiqueta_mensaje.pack(pady=15)

boton_reiniciar = ctk.CTkButton(
    app,
    text="Reiniciar juego",
    command=lambda: iniciar_juego(menu_dificultad.get())
)
boton_reiniciar.pack(pady=10)

app.mainloop()

