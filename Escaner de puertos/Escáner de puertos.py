#!/usr/bin/python
#Autor: Jose Conde 
#Escaner de puertos

import signal 
import queue
import sys
import socket
import threading
import os 
from queue import Queue

#Función ctrl + c 
def ctrl_c(sig, frame):
    limpiar()
    print("\n[!] Saliendo...\n")
    sys.exit(1)

signal.signal(signal.SIGINT, ctrl_c)

#Función limpiar pantalla
def limpiar():
    if os.name == "posix":
       os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
       os.system("cls")

#Llamada a la función
limpiar()

ip = "8.8.8.8" #\\IP
queue = Queue()
puertos_abiertos = []

#Función escaner
def portscan(puerto):
    try:
        #Entablamos conexión con el puerto(ip,puerto)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(( ip, puerto ))
        return True
    except:
        return False

def f_queue(lista_puertos):
    for puerto in lista_puertos:
        queue.put(puerto)

#Verificación
def escaneo():
    while not queue.empty():
        puerto = queue.get()
        if portscan(puerto):
            print("Puerto {} abierto".format(puerto))
            puertos_abiertos.append(puerto)

#Variables puertos
lista_puertos = range(1, 65535)
f_queue(lista_puertos)

#Trabajando con hilos 
hilos = []

for h in range(250):
    hilo = threading.Thread(target=escaneo)
    hilos.append(hilo)

for hilo in hilos:
    hilo.start()

for hilo in hilos:
    hilo.join()

print("\nLos puertos abiertos son: ", puertos_abiertos)
