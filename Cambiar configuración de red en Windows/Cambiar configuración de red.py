#!/usr/bin/python
#Autor: Jose Conde 
#Script en Python3 para modificar la ip en Windows

#Importamos la librerías necesarias 
from colorama import init, Fore, Style
import os 
import time 
import socket
import signal 
import sys
import subprocess

#Función ctrl + c 
def ctrl_c(sig, frame):
    os.system('cls')
    print(Fore.BLUE + "\n[!]" + Fore.RED +" Saliendo...\n" + Style.RESET_ALL)
    sys.exit(1)

signal.signal(signal.SIGINT, ctrl_c)

#Inicio de init, para que funcionen los colores
init(); os.system('cls')

#Variables con hostname e ip privada
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

#Información y variables por 
print(Fore.BLUE + "[!]" + Fore.YELLOW + " Tarjetas de red disponibles en el equipo " + Style.RESET_ALL,end=''); subprocess.call(['powershell.exe', 'Get-NetAdapter | Select-Object Name'])

print(Fore.BLUE + "[!]" + Fore.YELLOW + " La IP privada de tu equipo es: " + Style.RESET_ALL + local_ip)

print(Fore.BLUE + "\n[!]" + Fore.YELLOW + " Indica tu adaptador: " + Style.RESET_ALL,end='')
adaptador = input()
print(Fore.BLUE + "\n[!]" + Fore.YELLOW + " Indica la ip nueva: " + Style.RESET_ALL,end='')
ip_nueva = input()
print(Fore.BLUE + "\n[!]" + Fore.YELLOW + " Indica la máscara en /CIDR: " + Style.RESET_ALL,end='')
mascara = input()
print(Fore.BLUE + "\n[!]" + Fore.YELLOW + " Indica la puerta de enlace: " + Style.RESET_ALL,end='')
puerta = input()
print(Fore.BLUE + "\n[!]" + Fore.YELLOW + " Indica el DNS: " + Style.RESET_ALL,end='')
dns = input()


#Código para modificar la ip
subprocess.call(['powershell.exe', 'New-NetIpAddress -InterfaceAlias' , adaptador , '-IPAddres' , ip_nueva, '-PrefixLength' , mascara , '-DefaultGateway' , puerta, '3>$null'])
subprocess.call(['powershell.exe', 'Set-DnsClientServerAddress -InterfaceAlias' , adaptador , '-ServerAddresses' , dns , '3>$null'])
time.sleep(1); os.system('cls')

#Comprobación 
print(Fore.BLUE + "[!]" + Fore.YELLOW + " La IP privada nueva de tu equipo es: " + Style.RESET_ALL + ip_nueva)
