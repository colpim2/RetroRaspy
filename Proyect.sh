#!/bin/bash
# Licencia: MIT
# Creado por:
#   - Castillo Montes Pamela
#   - Cruz Cedillo Daniel Alejandro
# Fecha: 2023.12.05

#=== Update y descarga de proyecto === 
sudo apt update
cd /home/pi/
wget https://github.com/colpim2/RetroRaspy


#=== Emulador === 
#Libraries
sudo apt install libsdl2-dev libgtkmm-3.0-dev libepoxy-dev meson alsa-oss portaudio19-dev libminizip-dev
sudo apt-get install ninja-build

#Project
cd /home/pi/RetroRaspy/Emulador/
wget https://github.com/snes9xgit/snes9x/archive/refs/tags/1.60.tar.gz
tar -xzf 1.60.tar.gz
cd snes9x-1.60/gtk
meson build --buildtype=release –-strip
cd build
ninja

#=== Control ===
#Libraries 
sudo apt install xboxdrv
sudo apt install joystick
sudo cp /home/pi/RetroRaspy/snes9x.conf /home/pi/.config/snes9x/


#=== SplashScreen ===
#Libraries
sudo apt-get install fbi

#sudo nano /boot/config.txt
# Agregar disable_splash=1
#sudo nano /boot/cmdline.txt
# Agregar console=tty3 splash loglevel=3 logo.nologo vt.global_cursor_default=0 plymouth.enable=0
# Archivo splashscreen.service

#[Unit]
#Description=Splash screen
#DefaultDependences=no
#After=local-fs.target

#[Service]
#ExecStart=/usr/bin/fbi -d /dev/fb0 - -noverbose -a /home/pi/Emulador/src/bootLogo.png
#StandardInput=tty
#StandardOutut=tty

#[Install]
#WantedBy=sysinit.target

#sudo cp splashscreen.service /etc/systemd/system/
#sudo systemctl enable splashscreen

# === Interfaz === 
sudo apt-get install python3-pil python3-pil.imagetk