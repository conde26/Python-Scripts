#!/usr/bin/python
#Autor: Jose Conde 
#Script en Python3 para modificar el hostname

#Importamos librerias necesarias 
from colorama import init, Fore, Style
import os
import signal
import subprocess
import sys
import socket
import time 


#Función ctrl + c 
def ctrl_c(sig, frame):
    os.system('cls')
    print(Fore.BLUE + "\n[!]" + Fore.RED +" Saliendo...\n" + Style.RESET_ALL)
    sys.exit(1)

signal.signal(signal.SIGINT, ctrl_c)

#Codigo para modificar el hostname
init(); os.system('cls')
print(Fore.BLUE + "[!]" + Fore.YELLOW + " El nombre actual de tu equipo es: " + Style.RESET_ALL,end='')
print(socket.gethostname())

print(Fore.BLUE + "\n\n[?]" + Fore.YELLOW + " Indica el nombre nuevo de tu equipo: " + Style.RESET_ALL,end='')
nombre_nuevo = input()

subprocess.call(['powershell.exe', 'Rename-Computer', nombre_nuevo, '3>$null'])
time.sleep(1); os.system('cls')
print(Fore.BLUE + "[!]" + Fore.YELLOW + "El nombre se cambio correctamente, quieres reinciar para aplicar los cambios? (s/n): " + Style.RESET_ALL,end='')
respuesta = input()

#Verificamos la respuesta para reinicio
if respuesta == "s":
        print(Fore.BLUE + "\n[*]" + Fore.YELLOW + "Vamos a reinciar el equipo en dos segundos" + Style.RESET_ALL)
        os.system('shutdown -r -t 2')
elif respuesta == "n":
        print(Fore.BLUE + "\n[*]" + Fore.YELLOW + "Okay, no te olvide de hacerlo luego!" + Style.RESET_ALL)
else:
    print(Fore.BLUE + "\n[!]" + Fore.RED + "Respuesta no valida...Saliendo!" + Style.RESET_ALL)
    sys.exit(0)
