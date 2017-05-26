"""
UNIVERSIDAD DE COSTA RICA                       Escuela de Ingeniería Eléctrica

IE0499 | Proyecto Eléctrico
Mario Alberto Castresana Avendaño
A41267

Programa: BVH_TuneUp
-------------------------------------------------------------------------------

archivo: BVH_TuneUp.py
descripción:
Este es el programa principal.  Su función consiste en reparar un archivo BVH
que tenga glitches de MoCap.  Para tal efecto, se vale de las estructuras de
datos contenidas en la sección HIERARCHY del archivo BVH y un algoritmo que
compara estudios de goniometría con los movimientos descritos en los vectores
de MOTION del archivo de MoCap.

La documentación del algoritmo se puede encontrar en el github

https://github.com/mario23285/ProyectoElectrico.git

"""
#Lista de clases y módulos a importar

#módulos de sistema
import sys

#módulos de la jerarquía de huesos
from Foot import Foot

print('Inicializando BVH TuneUp...\nCreando jerarquía de Bones...')
#-------------------Creación de la jerarquía de Bones del MoCap------------
Leftfoot = Foot(138, 139, 140)

#-------------------FIN de la jerarquía---------------
#Creando el archivo de salida: BVH corregido


#Parsear archivo línea por línea
BVHfile = open(sys.argv[1], 'r')
outputBVH = open(sys.argv[2], 'w')

for line in BVHfile.readlines():
    if line[0].isdigit():
        print(line)
    else:
        outputBVH.write(line)

#---final del script se libera la memoria---
BVHfile.close()
outputBVH.close()
