#!/usr/bin/env python
#Autor: Jose Conde
#Geolocalizar IP

import urllib.request
import json
import time

#Variables
print("[!] Indica la IP que deseas geolocalizar: ", end=' ')
ip = input()
url="https://ipinfo.io/" + ip + "/json"

#Obtenido infomración
print("[*] Obteniendo información \n")
abrir_url=urllib.request.urlopen(url)
cargar_url=json.load(abrir_url)

#Resultado
for i in cargar_url:
    time.sleep(0.3)
    print("\t" + i + " : " + cargar_url[i])

