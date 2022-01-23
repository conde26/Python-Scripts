#!/usr/bin/env python
#Autor: Jose Conde
#Script Información ipv4 e ipv6

import sys
import optparse
import socket


def argumentos():
    parser = optparse.OptionParser()
    parser.add_option("-n", "--name", dest = "dominio", help="Nombre de dominio" )
    (options, arguments) = parser.parse_args()
    if not options.dominio:
        parser.error("[-] Porfavor indica un dominio, usa --help para mas informacion")
    return options


def conex(dominio):
    try:
          #obtener Ipv4 e Ipv6
          Ipv4 = socket.gethostbyname(dominio)
          Ipv6 = (socket.getaddrinfo(dominio, None, socket.AF_INET6)[0][4][0])

          #Resultado Conexión
          print("Nombre canónico: " + dominio)
          print("Dirección IPv4: " + Ipv4)
          print("Dirección Ipv6: " + Ipv6)

    except:
          print("[!] Error")
          sys.exit(1)


options = argumentos()
conex(options.dominio)
