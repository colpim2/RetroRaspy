# AUTORES:
- Castillo Montes Pamela
- Cruz Cedillo Daniel Alejandro
# RetroRaspy

Este archivo proporciona instrucciones detalladas sobre cómo configurar y utilizar RetroRaspy en tu Raspberry Pi. Sigue estos pasos para garantizar el correcto funcionamiento del proyecto.

## 1. Instalación del Sistema Operativo

- Instala Raspbian OS 64 bits con escritorio en tu Raspberry Pi.
  - **Recomendación:** Utiliza Raspberry Pi Imager para flashear una microSD de al menos 8 GB.
  - Configura el acceso a internet en tu dispositivo.

## 2. Configuración de Resolución de Pantalla

- Abre el menú principal.
- Navega a Preferences > Screen Resolution.
- Selecciona la pantalla a utilizar y configura la resolución adecuada.


## 3. Descargar RetroRaspy

- Ejecuta `wget https://github.com/colpim2/RetroRaspy` en la terminal.

## 4. Snes9x Emulator

- El emulador se descarga y compila automáticamente.
- Abre la terminal y ejecuta "Project.sh" para iniciar la instalación.

## 5. ROMs

- Si deseas descargar ROMs, asegúrate de que el nombre del archivo cumpla con las siguientes características:
  - De preferencia evitar que contenga espacios y caracteres especiales.
  - Debe tener la terminación .sfc o .srm.
  - Para agregarlas sera necesario hacerlo por USB
  - Viene precargada con 15 ROMs

## 6. Configuración del Control

- Se ha asignado automáticamente los botones para funcionar con un control de Xbox One conectado por cable.
  - **Nota:** Conecta el control antes de encender la Raspberry Pi.
- También es compatible con el uso de mouse y teclado.

## 7. Arranque Directo al Emulador
- Una vez instalada la consola la ejecucion se inicara de forma automatica al prenderla raspberry

## 8. Gestión de ROMs desde USB

- Inserta la USB despues de iniciar el sistema
- Debe tener la terminación .sfc o .srm.

## 9. Configuración de Animación de Arranque "RetroRaspy"

- La Raspberry tendra una pequeña imagen al encender que sera diferente a la que viene por default.
- Esta parte sera necesario realizarla de forma manual

- Desactiva el "rainbow splash".
  - Ejecuta `sudo nano /boot/config.txt` en la terminal.
  - Al final del archivo, agrega: `disable_splash=1`.
  - Guarda el archivo.
- Ejecuta `sudo nano /boot/cmdline.txt` en la terminal.
  - Agrega: `console=tty3 splash loglevel=3 logo.nologo vt.global_cursor_default=0 plymouth.enable=0`.
  - Guarda el archivo.
