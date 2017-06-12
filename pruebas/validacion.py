"""
UNIVERSIDAD DE COSTA RICA                       Escuela de Ingeniería Eléctrica

IE0499 | Proyecto Eléctrico
Mario Alberto Castresana Avendaño
A41267

Programa: Validacion
-------------------------------------------------------------------------------

archivo: validacion.py
descripción:
Este es un script que compara dos archivos BVH y calcula el error cuadrático medio
entre cada frame del video representado en sus arreglos de MOTION.  Note que este
script usa la función zip() la cual viene por default incluida en python 3.

https://github.com/mario23285/ProyectoElectrico.git

"""

"""
Primero debemos abrir los dos BVH de interés, los cuales se pasan por consola en el 
orden específico

$ python validacion.py <BVH_corregido_por_BVHTuneUP> <BVH_corregido_manual> <salida_CSV>

Donde la salida_CSV es un archivo de formato Comma Separated Values que se puede analizar
en Excel o LibreOffice Calc.

"""
import sys
import csv
import re

#Abrir files necesarios
BVH_corregido = open(sys.argv[1], 'r')
BVH_manual = open(sys.argv[2], 'r')
CSV = open('CSVfile.csv', 'w+')
ecm_csv = csv.writer(CSV, dialect='excel')
#Contador de frames (cuadros del MoCap)
frame = 1


for c, m in zip(BVH_corregido, BVH_manual):

    if m[0].isdigit() or m[1].isdigit():

        #crear array de 156 posiciones para Error Cuadrático Medio
        MSE = [frame, 0]
        #Aquí hay que separar la línea parseada y crear un arreglo de MOTION válido
        m = re.split('\s+|\n', m)
        #eliminar el ultimo elemento de m (la linea MOTION manual) '\n'
        #y convertir a float todo
        m.pop()
        MANUAL = [float(nums) for nums in m]
        print('Procesando BVH MANUAL >> frame: ' + str(frame))
        #ecm_csv.writerow(MANUAL)
    else:
        pass

    if c[0].isdigit() or c[1].isdigit():

        #Aquí hay que separar la línea parseada y crear un arreglo de MOTION válido
        c = re.split('\s+|\n', c)
        #eliminar el ultimo elemento de m (la linea MOTION manual) '\n'
        #y convertir a float todo
        c.pop()
        CORREGIDO = [float(nums) for nums in c]
        print('Procesando BVH CORREGIDO >> frame: ' + str(frame))
        #ecm_csv.writerow(CORREGIDO)

        #Si existe un arreglo de MOTION en esta línea, sacarle el error cuadráticos medio
        #en este frame
        for i in range(len(MANUAL)):
            #cambiar ángulos excesivamente grandes por sus equivalentes < 360º
            if MANUAL[i] > 180.000000:
                MANUAL[i] = (360-MANUAL[i])*(-1)

            if MANUAL[i] < -180.000000:
                MANUAL[i] = MANUAL[i]+360

            MSE[1] += ((CORREGIDO[i]-MANUAL[i])*(CORREGIDO[i]-MANUAL[i]))*(1/len(MANUAL))

        #guardar vector de error cuadrático medio en el CSV
        ecm_csv.writerow(MSE)
        #incrementar el contador de frames
        frame += 1

    else:
        pass

#liberar memoria
BVH_corregido.close()
BVH_manual.close()
CSV.close()
