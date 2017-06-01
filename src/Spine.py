"""
UNIVERSIDAD DE COSTA RICA                       Escuela de Ingeniería Eléctrica

IE0499 | Proyecto Eléctrico
Mario Alberto Castresana Avendaño
A41267

Programa: BVH_TuneUp
-------------------------------------------------------------------------------

archivo: Spine.py
descripción:
Este archivo contiene la clase Spine, la cual se utiliza para implementar la
columna vertebral (sección lumbar-torácica). Los estudios de goniometría para este hueso
se basan en los siguientes límites de los ángulos de Euler:
Z flexión lateral derecha + e izquierda -
X flexión + y extensión -
Y rotación izquierda + y derecha -
"""
from Bone import Bone

class Spine(Bone):
    """
    Esta subclase implementa el estudio de goniometría para las muñecas en
    el esqueleto del BVH. La jerarquía los llama "Hand".
    """
    def __init__(self, ID=' ', Zp=0, Xp=0, Yp=0):
        """
        Se inicializa este hueso con los siguientes parámetros
        ID: identificador del bone. Ej: izquierdo/derecho

        Cada posición del hueso se define con un vector de ángulos de Euler
        (Z, X, Y) los cuales tienen una posición específica dentro del array
        de la sección MOTION del BVH
        Zp: índice del array MOTION que contiene el angulo de euler Z para ese hueso
        Xp: índice del array MOTION que contiene el angulo de euler X para ese hueso
        Yp: índice del array MOTION que contiene el angulo de euler Y para ese hueso
        """
        self.ID = ID
        self.Zp = Zp
        self.Xp = Xp
        self.Yp = Yp
        #se llama al constructor de la super clase para acceder a todos los atributos
        #de goniometría
        Bone.__init__(self,
                      Name='Espina',
                      Zmin=-25000000,
                      Zmax=25.000000,
                      Xmin=-25.000000,
                      Xmax=45.000000,
                      Ymin=-45.000000,
                      Ymax=45.000000)

    def Goniometry_check(self, MOTION, frame):
        """
        Descripción:
        Esta función se encarga de comparar el valor de los ángulos de Euler que
        un hueso posee en un frame determinado, con el valor de los límites
        goniométricos de ese hueso en particular.  Si algún ángulo de Euler excede
        los límites del movimiento humano, se reportará un glitch en ese frame
        y se procederá a corregirlo en el arreglo MOTION.

        argumentos:
        MOTION: arreglo de 156 posiciones que contiene todos los ángulos de Euler
        para cada hueso en un frame dado.  El orden de cada hueso viene dado por
        la sección HIERARCHY del BVH.
        frame: cuadro del video de MoCap que se está analizando
        """
        #Primero, definimos los valores de cada ángulo de Euler
        Zeuler = MOTION[self.Zp]
        Xeluer = MOTION[self.Xp]
        Yeuler = MOTION[self.Yp]
        glitch = False
        ErrorMsg = ' existen glitches de '

        #probamos límites en Z
        if Zeuler < self.Zmin:
            MOTION[self.Zp] = self.Zmin
            glitch = True
            ErrorMsg += 'flexion lateral | '

        if Zeuler > self.Zmax:
            MOTION[self.Zp] = self.Zmax
            glitch = True
            ErrorMsg += 'flexion lateral | '

        #aquí probamos límites en X
        if Xeluer < self.Xmin:
            MOTION[self.Xp] = self.Xmin
            glitch = True
            ErrorMsg += 'hiperextension | '
        if Xeluer > self.Xmax:
            MOTION[self.Xp] = self.Xmax
            glitch = True
            ErrorMsg += 'flexion | '

        #aquí probamos límites en Y
        if Yeuler < self.Ymin:
            MOTION[self.Yp] = self.Ymin
            glitch = True
            ErrorMsg += 'rotacion excesiva a la derecha | '
        if Yeuler > self.Ymax:
            MOTION[self.Yp] = self.Ymax
            glitch = True
            ErrorMsg += 'rotacion excesiva a la izquierda | '

        if glitch:
            self.Report_glitch(ErrorMsg, frame)
