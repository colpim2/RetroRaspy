# RetroRaspy

Este archivo proporciona instrucciones detalladas sobre cómo configurar y utilizar RetroRaspy en tu Raspberry Pi. Sigue estos pasos para garantizar el correcto funcionamiento del proyecto.

## 1. Instalación del Sistema Operativo

- Instala Raspbian OS 64 bits con escritorio en tu Raspberry Pi.
  - **Recomendación:** Utiliza Raspberry Pi Imager para flashear una microSD de al menos X GB.
  - Configura el acceso a internet en tu dispositivo.

## 2. Configuración de Resolución de Pantalla

- Abre el menú principal.
- Navega a Preferences > Screen Resolution.
- Selecciona la pantalla a utilizar y configura la resolución adecuada.

## 3. Snes9x Emulator

- El emulador se descarga y compila automáticamente.
- Abre la terminal y ejecuta "Project.sh" para iniciar la instalación.

## 4. ROMs

- Si deseas descargar ROMs, asegúrate de que el nombre del archivo cumpla con las siguientes características:
  - No debe contener espacios.
  - Debe tener la terminación .sfc o .srm.

## 5. Configuración del Control

- Se ha asignado automáticamente los botones para funcionar con un control de Xbox One conectado por cable.
  - **Nota:** Conecta el control antes de encender la Raspberry Pi.
- También es compatible con el uso de mouse y teclado.

## 6. Arranque Directo al Emulador

## 7. Gestión de ROMs desde USB

## 8. Configuración de Animación de Arranque "RetroRaspy"

- Desactiva el "rainbow splash".
  - Ejecuta `sudo nano /boot/config.txt` en la terminal.
  - Al final del archivo, agrega: `disable_splash=1`.
  - Guarda el archivo.
- Ejecuta `sudo nano /boot/cmdline.txt` en la terminal.
  - Agrega: `console=tty3 splash loglevel=3 logo.nologo vt.global_cursor_default=0 plymouth.enable=0`.
  - Guarda el archivo.