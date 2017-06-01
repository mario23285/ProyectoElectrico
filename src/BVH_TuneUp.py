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
import csv

#módulos de la jerarquía de huesos
from Foot import Foot
from Leg import Leg
from Arm import Arm
from ForeArm import ForeArm
from UpLeg import UpLeg

#-------------------ESTRUCTURAS DE DATOS Y OBJETOS-------------------------
#Creación de la jerarquía de Bones del MoCap
#cada objeto se inicializa con un ID (nombre identificador) y las coordenadas
#dentro de la sección MOTION

#miembros inferiores
LeftUpLeg = UpLeg('Izquierda', 132, 133, 134)
RightUpLeg = UpLeg('Derecha', 144, 145, 146)

LeftLeg = Leg('Izquierda', 135, 136, 137)
RightLeg = Leg('Derecha', 147, 148, 149)

Leftfoot = Foot('Izquierdo', 138, 139, 140)
Rightfoot = Foot('Derecho', 150, 151, 152)

#tronco superior
LeftArm = Arm('Izquiero', 21, 22, 23)
RightArm = Arm('Derecho', 78, 79, 80)
LeftForeArm = ForeArm('Izquierdo', 24, 25, 26)
RightForeArm = ForeArm('Derecho', 81, 82, 83)

#-------------------FIN DE ESTRUCTURAS DE DATOS Y OBJETOS------------------

#Archivos de entrada (BVHfile) y salida (outputBVH)
BVHfile = open(sys.argv[1], 'r')
outputBVH = open(sys.argv[2], 'w')

#Archivo de Excel para analizar error cuadrático medio
ECM = open('ECM.csv', 'w+')
ecm_csv = csv.writer(ECM, dialect='excel')

#Contador de frames (cuadros del MoCap)
frame = 1

#Inicio-----------------------------------------------
print('Inicializando BVH TuneUp...\nCreando jerarquía de Bones...')


for line in BVHfile.readlines():
    if line[0].isdigit():

        #Aquí hay que separar la línea parseada y crear un arreglo de MOTION válido
        line = line.split('    ')
        #eliminar el ultimo elemento de line '\n' y convertir a float todo
        line.pop()
        MOTION = [float(nums) for nums in line]
        print('Procesando movimientos del frame: ' + str(frame))
        #Preservamos vector de MOTION orginal para su posterior análisis y validación
        ORIGIN = MOTION
        ecm_csv.writerow(ORIGIN)

        #Aquí se aplican los estudios de goniometría a cada Bone-----
        Leftfoot.Goniometry_check(MOTION, frame)
        Rightfoot.Goniometry_check(MOTION, frame)
        LeftLeg.Goniometry_check(MOTION, frame)
        RightLeg.Goniometry_check(MOTION, frame)
        LeftUpLeg.Goniometry_check(MOTION, frame)
        RightUpLeg.Goniometry_check(MOTION, frame)

        LeftArm.Goniometry_check(MOTION, frame)
        RightArm.Goniometry_check(MOTION, frame)
        LeftForeArm.Goniometry_check(MOTION, frame)
        RightForeArm.Goniometry_check(MOTION, frame)

        #escriba el vector de MOTION al ECM.csv para validación de datos
        ecm_csv.writerow(MOTION)

        #aqui se debe escribir el arreglo de MOTION al outputBVH conviertiéndolo en string
        outputMotion = [str(nums) for nums in MOTION]
        #se convierte el arreglo de una lista de floats a un string
        salida = '    '.join(outputMotion)
        outputBVH.write(salida + '\n')

        #incrementar el contador de frames
        frame += 1
    else:
        outputBVH.write(line)

#---final del script se libera la memoria---
print('Creando Glitch_Report...\nCreando archivo BVH corregido en este directorio...\n')
print('Liberando memoria...')
print('BVH_TuneUp finalizó con éxito. Que tenga un buen día.')
BVHfile.close()
outputBVH.close()
ECM.close()
