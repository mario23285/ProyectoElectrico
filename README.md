# ProyectoElectrico
IE0499 Proyecto Final de graduación | Universidad de Costa Rica

Mario A. Castresana Avendaño
A41267

Pattern Recognition and Intelligent Systems Lab. | I-2017



# Programa y modo de empleo

El programa implementa un algoritmo de corrección de glitches de MoCap, basado
en estudios de goniometría y fisiología articular.  Mediante dichos estudios, el script
es capaz de entender los movimientos de un ser humano y determinar si un archivo BVH
contiene errores de captura, los cuales se manifiestan como movimientos erráticos, quebraduras
de articulaciones o movimientos imposibles de ejecutar para un ser humano.

El script se localiza en la carpeta /src y no requiere de instalación o dependencias de software.
Simplemente copie el archivo bvh dañado a la carpeta /src y ejecute la siguiente linea de comando
en un PowerShell (Windows) [bash en Linux o Mac]


\> python .\BVH_TuneUP.py <BVH_a_corregir> <Nombre del BVH de salida>

Ejemplo:
    \src> python .\BVH_TuneUp.py .\escena2.2_esqueleto9.bvh .\escena_corregida.bvh


Se generará a la salida un reporte de Glitches (Errores), un archivo ECM.csv (que es usado para análisis y debugging) y el BVH con la escena corregida.