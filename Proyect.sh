#!/bin/bash

#Permisos de Ejecución 
#chmod u+rwx primer_script

#Raspbian OS

#Update
sudo apt update

#=== Seccion para que descargue nuestro proyecto desde github
#wget https://github.com/


#=== Emulador === 
#Libraries
sudo apt install libsdl2-dev libgtkmm-3.0-dev libepoxy-dev meson alsa-oss portaudio19-dev libminizip-dev
sudo apt-get install ninja-build

#Project
wget https://github.com/snes9xgit/snes9x/archive/refs/tags/1.60.tar.gz
tar -xzf 1.60.tar.gz
cd snes9x-1.60/gtk
meson build --buildtype=release –-strip
cd build
ninja
#./snes9x-gtk

#=== Control ===

#Libraries 
sudo apt install xboxdrv
sudo apt install joystick

sudo xboxdrv --detach-kernel-driver --silent --mouse --mimic-xpad --mimic-xpad-wireless \
  --axismap -Y1=Y1,-Y2=Y2 \
  --buttonmap A=BTN_A,B=BTN_B,X=BTN_X,Y=BTN_Y,TL=BTN_TL,TR=BTN_TR,DU=KEY_UP,DD=KEY_DOWN,DL=KEY_LEFT,DR=KEY_RIGHT \
  --trigger-as-button --trigger-buttonmap RT=BTN_LEFT \
  --evdev-absmap ABS_X=X1,ABS_Y=Y1,ABS_Z=X2,ABS_RZ=Y2


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

sudo cp splashscreen.service /etc/systemd/system/
sudo systemctl enable splashscreen


# === Interfaz === 
sudo apt-get install python3-pil python3-pil.imagetk