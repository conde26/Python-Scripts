# Descubrir IPv4 e IPv6 de un dominio
## Autor: Jose Conde 
### IPDiscover.py

Esta herramienta desarrolada en python, te permitirá obtener la Ipv4 y la Ipv6 de cualquier dominio que le indiques, por ejemplo de google.com. Para que la herramienta funcione debemos tener: 
- **Conexión a Internet**
- **Adaptador Ipv4 e Ipv6 Habilitados**

### Uso 
#### Parametros 
- -h) Muestra el panel de ayuda
- -n | --name) Indicamos el dominio a escanear

#### Ejemplo de uso
```Python
python3 IPDiscover.py -n google.com
```
##### El anterior ejemplo dara una salida similar a la siguiente 
```Python
Nombre canónico: GOOGLE.COM
Dirección IPv4: XXX.XXX.XXX.XXX
Dirección Ipv6: XXXX:XXXX:XXXX::XXXX
```
