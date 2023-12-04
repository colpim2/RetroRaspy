import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import subprocess
import os

def ejecutar_emulador():
    seleccion = lista.get(lista.curselection())
    if seleccion:
        etiqueta_juego.config(text=f"Ejecutando: {seleccion}")
        ruta_rom = f"~/Emulador/Roms/'{seleccion}.sfc'"
        ruta_ejecutable = "~/Emulador/snes9x-1.60/gtk/build/snes9x-gtk"

        # Agregar las opciones de pantalla completa y dimensiones de ventana al comando del emulador
        comando = f"{ruta_ejecutable} {ruta_rom} --fullscreen"

        # Ejecutar el emulador en pantalla completa en un nuevo proceso
        emulador = subprocess.Popen(comando, shell=True, cwd=os.path.join("snes9x-1.60", "gtk", "build"))

        # Configurar la detección de la tecla 'p' para cerrar el emulador
        keyboard.add_hotkey('p', lambda: emulador.terminate())

def mostrar_juego_seleccionado(event):
    seleccion = lista.get(lista.curselection())
    etiqueta_juego.config(text=f"El juego seleccionado es: {seleccion}")

def redimensionar_imagen(imagen_original, nuevo_ancho, nuevo_alto):
    return imagen_original.resize((nuevo_ancho, nuevo_alto), Image.ANTIALIAS)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Emulador de SNES")
ventana.geometry("800x600")

# Establecer un estilo para el botón
estilo = ttk.Style()
estilo.configure("Boton.TButton", font=("Helvetica", 12), padding=10, relief="raised", background="#D32F2F", foreground="white")

# Configurar la ventana para ocupar toda la pantalla
ventana.attributes('-fullscreen', True)

# Obtener las dimensiones de la pantalla
ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()

# Cargar la imagen de fondo y redimensionarla
imagen_fondo_original = Image.open(os.path.join("src", "bootLogo.png"))
imagen_fondo_redimensionada = redimensionar_imagen(imagen_fondo_original, ancho_pantalla, alto_pantalla)
imagen_fondo = ImageTk.PhotoImage(imagen_fondo_redimensionada)
label_fondo = tk.Label(ventana, image=imagen_fondo)
label_fondo.place(relwidth=1.0, relheight=1.0)

# Ruta de la carpeta que contiene los Roms
ruta_carpeta = "Roms"
# Crear una lista con los primeros cinco juegos
juegos = []
archivos_sin_extension = []
# Crear una lista con una fuente y altura más grandes
fuente_lista = ("Helvetica", 16)
altura_elemento_lista = 50

# Verificar si la carpeta existe
if os.path.exists(ruta_carpeta) and os.path.isdir(ruta_carpeta):
    # Iterar sobre los archivos en la carpeta
    for archivo in os.listdir(ruta_carpeta):
        # Verificar si el archivo termina con .sfc
        if archivo.endswith(".sfc"):
            # Obtener el nombre del archivo sin la extensión
            nombre_sin_extension = os.path.splitext(archivo)[0]
            archivos_sin_extension.append(nombre_sin_extension)

    # Crear una lista con los nombres de archivos sin la extensión .sfc
    juegos = archivos_sin_extension

# Crear una lista con una barra de desplazamiento
lista = tk.Listbox(ventana, font=fuente_lista, selectbackground="#4CAF50", selectforeground="white", borderwidth=0, relief="flat", activestyle="none", height=5)
for juego in juegos:
    lista.insert(tk.END, juego)
lista.place(relx=0.48, rely=0.5, anchor='center')  # Centrar la lista horizontal y ubicarla más a la derecha

# Crear una etiqueta para mostrar el juego seleccionado debajo de la lista centrada
etiqueta_juego = tk.Label(ventana, text="Selecciona un juego", bg="#D32F2F", fg="white", font=("Helvetica", 20), pady=10, padx=20, relief="raised")
etiqueta_juego.place(relx=0.5, rely=0.7, anchor='center')  # Centrar la etiqueta horizontalmente

# Crear una barra de desplazamiento
scrollbar = tk.Scrollbar(ventana, orient="vertical", command=lista.yview)
scrollbar.place(relx=0.6, rely=0.5, anchor='center', relheight=0.15)  # Establecer relheight a 0.3 y ubicar más a la derecha

# Vincular la barra de desplazamiento con la lista
lista.config(yscrollcommand=scrollbar.set)

# Configurar el evento de selección de la lista
lista.bind("<<ListboxSelect>>", mostrar_juego_seleccionado)

# Crear un botón para ejecutar el emulador con el juego seleccionado
boton_ejecutar_emulador = ttk.Button(ventana, text="Jugar", style="Boton.TButton", command=ejecutar_emulador)
boton_ejecutar_emulador.place(relx=0.5, rely=0.8, anchor='center')  # Centrar el botón horizontalmente

# Iniciar el bucle de eventos
ventana.mainloop()


