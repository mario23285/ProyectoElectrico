"""
UNIVERSIDAD DE COSTA RICA                       Escuela de Ingeniería Eléctrica

IE0499 | Proyecto Eléctrico
Mario Alberto Castresana Avendaño
A41267

Programa: BVH_TuneUp
-------------------------------------------------------------------------------

archivo: Bone.py
descripción:
Este archivo contiene la clase Bone, utilizada para manejar toda la información
contenida en el archivo BVH.

A partir de esta clase, se definen todos los huesos con el nombre
correspondiente dentro de la sección HIERARCHY del BVH y se agregan las
características goniométricas de cada hueso del esqueleto humano, utilizando
un esquema de herencia.

La instanciación de cada hueso basado en esta clase, da como resultado la
construcción de todo el esqueleto representado por la sección HIERARCHY del BVH.
"""

class Bone:
    """
    Esta  clase contiene todos los métdos necesarios para manipular la
    información de cualquier hueso de la jerarquía proveniente de la sección
    HIERARCHY del archivo BVH.
    """
    def __init__(self,
                 Name='GenericBone',
                 Zmin=0,
                 Zmax=0,
                 Xmin=0,
                 Xmax=0,
                 Ymin=0,
                 Ymax=0):
        """
        Se inicializa cada hueso con sus valores por default:
        Name: nombre del hueso
        Valores Goniométricos para este hueso:
        Zmax, Zmin : valores máximos y mínimos en Z
        Xmax, Xmin : valores máximos y mínimos en X
        Ymax, Ymin : valores máximos y mínimos en Y
        """
        self.Name = Name
        self.Zmin = Zmin
        self.Zmax = Zmax
        self.Xmin = Xmin
        self.Xmax = Xmax
        self.Ymin = Ymin
        self.Ymax = Ymax

    def Report_glitch(self, errorMsg='Hay un glitch de movimiento aquí', frame=0):
        """
        Descripción:
        Esta función se encarga de reportar los glitches que se encuentra y en
        qué frame en específico está. Cada glitch se reporta en un archivo de
        texto llamado Glitch_Report

        argumentos:
        errorMsg: string que contiene un mensaje de error
        frame: cuadro donde se produce el glitch
        """
        #creamos el archivo de reporte
        glitch = open('Glitch_Report', 'a')
        errorString = 'Frame: ' + str(frame) + 'bone: '+ self.Name + ' | ' + errorMsg
        #se escribe el string de error y se libera la memoria
        glitch.write(errorString)
        glitch.close()
