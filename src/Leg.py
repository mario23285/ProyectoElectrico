"""
UNIVERSIDAD DE COSTA RICA                       Escuela de Ingeniería Eléctrica

IE0499 | Proyecto Eléctrico
Mario Alberto Castresana Avendaño
A41267

Programa: BVH_TuneUp
-------------------------------------------------------------------------------

archivo: Leg.py
descripción:
Este archivo contiene la clase Leg, la cual se utiliza para implementar la
rodilla izquierda y la derecha. Los estudios de goniometría para este hueso
se basan en los siguientes límites de los ángulos de Euler:
Z torsión no válida
X Flexión + y extensión -
Y rotación no válida
"""
from Bone import Bone

class Leg(Bone):
    """
    Esta subclase implementa el estudio de goniometría para las rodillas en
    el esqueleto del BVH. La jerarquía los llama "Leg".
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
                      Name='Rodilla',
                      Zmin=-0.200000,
                      Zmax=0.200000,
                      Xmin=0.000000,
                      Xmax=150.000000,
                      Ymin=-1.000000,
                      Ymax=1.000000)

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
        #Exempt es una variable que se activa cuando detecta problemas de rotacion
        #de ejes Z y Y en las rodillas
        Exempt = False          
        ErrorMsg = ' existen glitches de '

        #Variables para probar si hubo rotación de ejes y el esqueleto está agachado
        rodilla_flex =  Xeluer > 13.0 or Xeluer < -15.0
        y_rot = Yeuler > 20.0 or Yeuler < -20.0
        z_rot = Zeuler > 40.0 or Zeuler < -40.0

        Rotacion_ejes = y_rot or z_rot

        if rodilla_flex and Rotacion_ejes:
            Exempt = True

        if Exempt:
            #Existen dos pruebas goniométricas distintas de acuerdo al nivel de flexión de las
            #rodillas.  En el caso de que las rodillas tengan un ángulo de flexión mayor a 45º o
            #exista una rotacion de los eje Z y Y, debemos incrementar los límites de movilidad.
            #en Z y Y. Esto debido al comportamiento de los huesos en el BVH, los cuales rotan
            #los ejes Y y Z para representar movimientos de un esqueleto agachado.

            #Esto ocurre debido a la pérdida de orientación del hueso,por parte de las cámaras
            #en los ejes Z y Y.

            #probamos límites nuevos en Z
            if Zeuler < -160.000000:
                #MOTION[self.Zp] no se le aplica restricción en Z
                glitch = True
                ErrorMsg += 'pérdida de orientación de los sensores en Z- | '

            if Zeuler > 160.000000:
                #MOTION[self.Zp] no se le aplica restricción en Z
                glitch = True
                ErrorMsg += 'pérdida de orientación de los sensores en Z+ | '

            #aquí probamos nuevos límites en X
            if Xeluer < -150.000000:
                #MOTION[self.Xp] no se le aplica restricción en X
                glitch = True
                ErrorMsg += 'pérdida de orientación de los sensores en X- | '
            if Xeluer > 150.000000:
                #MOTION[self.Xp] no se le aplica restricción en X
                glitch = True
                ErrorMsg += 'pérdida de orientación de los sensores en X+ | '

            #aquí probamos nuevos límites en Y
            if Yeuler < -105.000000:
                #MOTION[self.Yp] no se le aplica restricción en Y
                glitch = True
                ErrorMsg += 'pérdida de orientación de los sensores en Y- | '
            if Yeuler > 105.000000:
                #MOTION[self.Yp] no se le aplica restricción en Y
                glitch = True
                ErrorMsg += 'pérdida de orientación de los sensores en Y+ | '

        else:
            #probamos límites en Z
            if Zeuler < self.Zmin:
                MOTION[self.Zp] = self.Zmin
                glitch = True
                ErrorMsg += 'torsión | '

            if Zeuler > self.Zmax:
                MOTION[self.Zp] = self.Zmax
                glitch = True
                ErrorMsg += 'torsión | '

            #aquí probamos límites en X
            if Xeluer < self.Xmin:
                MOTION[self.Xp] = self.Xmin
                glitch = True
                ErrorMsg += 'extension | '
            if Xeluer > self.Xmax:
                MOTION[self.Xp] = self.Xmax
                glitch = True
                ErrorMsg += 'flexion | '

            #aquí probamos límites en Y
            if Yeuler < self.Ymin:
                MOTION[self.Yp] = self.Ymin
                glitch = True
                ErrorMsg += 'rotacion interna | '
            if Yeuler > self.Ymax:
                MOTION[self.Yp] = self.Ymax
                glitch = True
                ErrorMsg += 'rotacion externa | '

        if glitch:
            self.Report_glitch(ErrorMsg, frame)
