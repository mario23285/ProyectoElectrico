"""
UNIVERSIDAD DE COSTA RICA                       Escuela de Ingeniería Eléctrica

IE0499 | Proyecto Eléctrico
Mario Alberto Castresana Avendaño
A41267

Programa: BVH_TuneUp
-------------------------------------------------------------------------------

archivo: Foot.py
descripción:
Este archivo contiene las clase Foot, la cual se utiliza para implementar el
tobillo derecho y el izquierdo. Los estudios de goniometría para este hueso
se basan en los siguientes límites de los ángulos de Euler:
Z rotación sobre el eje del tobillo (el tobillo casi no se mueve en esta dirección)
X Flexión Plantar (hacia abajo) y dorsiflexión
Y Torsión hacia afuera y hacia adentro (hay poca movilidad en esta componente también)
"""
from Bone import Bone

class Foot(Bone):

    """
    Esta subclase implementa el estudio de goniometría para los tobillos en
    el esqueleto del BVH. La jerarquía los llama "Foot". Se manejan los
    siguientes ángulos:
    Z rotación
    X flexión plantar/Dorsiflexión
    Y torsión
    """

    def __init__(self, Zp=0, Xp=0, Yp=0):
        """
        Se inicializa este hueso con los siguientes parámentros

        Cada posición del hueso se define con un vector de ángulos de Euler
        (Z, X, Y) los cuales tienen una posición específica dentro del array
        de la sección MOTION del BVH
        Zp: índice del array MOTION que contiene el angulo de euler Z para ese hueso
        Xp: índice del array MOTION que contiene el angulo de euler X para ese hueso
        Yp: índice del array MOTION que contiene el angulo de euler Y para ese hueso
        """
        self.Zp = Zp
        self.Xp = Xp
        self.Yp = Yp
        #se llama al constructor de la super clase para acceder a todos los atributos
        #de goniometría
        Bone.__init__(self,
                      Name='Tobillo',
                      Zmin=-5.000000,
                      Zmax=5.000000,
                      Xmin=-30.000000,
                      Xmax=50.000000,
                      Ymin=0.000000,
                      Ymax=15.000000)

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

        #probamos límites en Z
        if Zeuler < self.Zmin:
            MOTION[self.Zp] = self.Zmin
            self.Report_glitch('Error de rotación, el tobillo no se mueve en esta dirección', frame)

        if Zeuler > self.Zmax:
            MOTION[self.Zp] = self.Zmax
            self.Report_glitch('Error de rotación, el tobillo no se mueve en esta dirección', frame)

        #aquí probamos límites en X
        if Xeluer < self.Xmin:
            MOTION[self.Xp] = self.Xmin
            self.Report_glitch('Error de dorsiflexión', frame)
        if Xeluer > self.Xmax:
            MOTION[self.Xp] = self.Xmax
            self.Report_glitch('Error de flexión plantar', frame)

        #aquí probamos límites en Y
        if Yeuler < self.Ymin:
            MOTION[self.Yp] = self.Ymin
            self.Report_glitch('Error de torsión, el tobillo no se mueve en esta dirección', frame)
        if Yeuler > self.Ymax:
            MOTION[self.Yp] = self.Ymax
            self.Report_glitch('Error de torsión, el tobillo no se mueve en esta dirección', frame)
#------------------------------------------------------
