#!/usr/bin/env python
#Autor: Jose Conde
#Script Información ipv4 e ipv6

import sys
import getopt
import socket
from colorama import init, Fore, Style
import os


#Funciones Ayuda, Limpiar y Conexión
def ayuda():
    print(Fore.GREEN + "[!] USO: " + Fore.YELLOW + "python3 " + sys.argv[0] + Style.RESET_ALL)
    print(Fore.GREEN + "\n\t -n) " + Fore.YELLOW + "Nombre del dominio\n" + Style.RESET_ALL)
    print(Fore.GREEN + "\t [!] Ejemplo: " + Fore.YELLOW + sys.argv[0] +  " -n www.google.es" + Style.RESET_ALL)

def limpiar():
    if os.name == "posix":
       os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
       os.system("cls")

def conexion():
    ip = None
    argv = sys.argv[1:]
    nombre = sys.argv[2]

    try:
        opts, args = getopt.getopt(argv, "n:")

    except:
        print(Fore.RED + "[!] Error" + Style.RESET_ALL)

    for opt, arg in opts:

        if opt in ['-n']:
          #obtener Ipv4 e Ipv6
          Ipv4 = socket.gethostbyname(str(nombre))
          Ipv6 = socket.getaddrinfo(str(nombre), None, socket.AF_INET6)
          Ipv6_1 = Ipv6[0]
          Ipv6_2 = Ipv6_1[4]
          Ipv6_3 = Ipv6_2[0]

          #Resultado Conexión
          print(Fore.RED + "[!] Información sobre " + str(nombre).upper() + Style.RESET_ALL + "\n")
          print(Fore.GREEN + "\t[!] Nombre canónico: " + Style.RESET_ALL + str(nombre))
          print(Fore.GREEN + "\t[!] Dirección IPv4: " + Style.RESET_ALL + str(Ipv4))
          print(Fore.GREEN + "\t[!] Dirección Ipv6: " + Style.RESET_ALL + str(Ipv6_3))

#Funciones y panel ayuda
if len(sys.argv) < 3:
    init()
    limpiar()
    ayuda()
else:
    init()
    limpiar()
    conexion()















