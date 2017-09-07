#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Version resumida de Modulo ASCAT, en un comando.
Una vez en el directorio del Modulo ejecutar
>>> python procesarASCAT arg1 arg2 arg3 arg4 arg5 arg6 arg7
arg1: Path del archivo ascat a procesar. Ruta compelta.
arg2: tecnica con la cual procesar. SuperObbing: SO // Thinning : T
arg3: valor nuemrico del radio geografico, ej> 0.30
arg1, 2 y 3 siempre deben estar explicitos.

arg4 arg5 arg6 arg7 son opcionales, Para recortar el espacio geografico a procesar.
Correspondos a latitud minima, maxima, longitud minima, maxima.
Rangos aceptables. Latitude: -90 a 90. Longitude> 0 a 360

El comando incluye la generacion de dos graficas.

* Comparacion de ubicaciones antes y despues de procesar.
* Intensidad y direcion del viento segun sus componentes U y V Resultado del Proceso

Este archivo es una copia del que esta en la carpeta Modulo Ascat. Es practicamente igual, pero al estar en la misma carpeta de los demas codigos se puede ejecutar desde cualquier ubicacion haciendo "python /home/..../cgi-bin/procesarASCAT.py arg1 arg2 arg3.

No creea carpetas donde guardar los resultados, sino que que los archivos de salida los ubica desde el lugar donde se lo invoque.
Respecto al archivo en formato Bufr, no brinda el archivo sino el programa que codifica este archivo. Este debe ser compilado de la sgt forma para obtener el archivo final:
$FC -o encode_ASCAT.exe encode_ASCAT.o -L/PATH/DE/LIBBUFR -lbufr'
./encode_ASCAT.exe
"""

import sys

from PlotObs import *
from exportarBufr import *
from exportarNetCDF import *
from exportarTxtDat import *
from prepararObs import *
from tecnicas import *


def salir():
    print "Gracias por usar Modulo ASCAT"
    sys.exit(0)


cont = 0
for elements in sys.argv:
    cont += 1

if cont < 4:
    print "Numero de parametros insuficiente, Los prametros basicos requeridos son: File path, Tecnica y Step"
    salir()

file_path = sys.argv[1]  # path del file a procesar
nombreArchivo = file_path[(len(file_path) - 59):(len(file_path) - 3)]

if not checkfile(file_path):
    print "No se encuentra el archivo indicado. Asegurese de ingresar la ruta completa."
    salir()

tecnica = sys.argv[2]  # 'SO' o 'T'

if str(tecnica) != 'SO' and str(tecnica) != 'T':
    print "Revise los parametros. Tecnicas posibles SO: SuperObbing, T: Thinning"
    salir()

step = sys.argv[3]  # considera obs cercanas

try:
    step = float(step)
except ValueError:
    print "El radio geografico debe ser un NUMERO."
    salir()
if cont > 4:
    if cont != 8:
        print "Parametros Obligados: File Path, Tecnica, Step. Parametros opcionales: Latitud Minima, latitud Maxima, longitud Minima, longitud Maxima. Para mas infromacion procesarASCAT.py -h"

if cont == 8:
    latMin = sys.argv[4]
    latMax = sys.argv[5]
    lonMin = sys.argv[6]
    lonMax = sys.argv[7]
    try:
        latMin = float(latMin)
        latMax = float(latMax)
        lonMin = float(lonMin)
        lonMax = float(lonMax)
    except ValueError:
        print "El latitudes y longitudes deben ser NUMEROS (Lats -90 a 90 Lons 0 a 360)."
        salir()
    if latMin > latMax or lonMin > lonMax:
        print "Revisar latidudes y longitudes ingresadas."
        salir()
    if latMin < -90 or latMax < -90:
        print "Latitudes o longitudes fuera del rango posible"
        salir()
    if lonMin < 0 or lonMax < 0:
        print "Latitudes o longitudes fuera del rango posible"
        salir()
    if latMin > 90 or latMax > 90:
        print "Latitudes o longitudes fuera del rango posible"
        salir()
    if lonMin > 360 or lonMax > 360:
        print "Latitudes o longitudes fuera del rango posible"
        salir()
else:
    latMax = 0.0
    latMin = -90
    lonMin = 220.0
    lonMax = 360  # valores Default

radioHorario = 60

lugar = 'Lats' + str(latMin) + '_' + str(latMax) + 'Lon' + str(lonMin) + '_' + str(lonMax)
coordenadas, obsTotales, obsSubSet = prepararObs(file_path, latMax, latMin, lonMin, lonMax)
coordPlot = coordenadas[:]  # necesario para realizar graficas.
resultado = tecnicas(coordenadas, step, tecnica, radioHorario)
nombre = 'procesado-' + str(nombreArchivo) + '-' + tecnica + 'Geo-' + lugar
exportarNetCDF(resultado, nombre + '.nc', len(resultado))
creacionTxt(nombreArchivo, resultado)
creacionDat(nombreArchivo, resultado)

#os.system('mkdir ArchivosProcesados/' + nombre)
os.system('mv procesado-' + nombreArchivo + '.txt' + ' ArchivosProcesados/' + nombre)
os.system('mv procesado-' + nombreArchivo + '.dat' + ' ArchivosProcesados/' + nombre)
os.system('mv ArchivosProcesados/' + nombre + '.nc' + ' ArchivosProcesados/' + nombre)
escribirFortranBurf(nombreArchivo, resultado)
os.system('$FC -c encode_ASCAT.f90')
#path_bufrlib = str(os.getcwd()) + "/BUFRLIB_v10-2-3"
#os.system('$FC -o encode_ASCAT.exe encode_ASCAT.o -L/' + path_bufrlib + ' -lbufr')
#os.system('./encode_ASCAT.exe')
#os.system('mv procesado-' + nombreArchivo + '.bufr' + ' ArchivosProcesados/' + nombre)
#os.system('rm encode_ASCAT.f90')
#os.system('rm encode_ASCAT.o')
#os.system('rm encode_ASCAT.exe')
print "Proceso finalizado satisfactoriamente. Puede encontrar el resultado en la carpeta ArchivosProcesados"
print "Generando Graficos..."
plotAscat(
    resultado,
    'ro',
    5,
    'Comparacion antes y despues de procesar',
    'Comparativa.\n Ubicacion de las observaciones nuevas (Rojo) y las originales (Azul)',
    latMin,
    latMax,
    lonMin,
    lonMax,
    coordPlot,
    'bo',
    2)
plotWinds(
    resultado,
    "Intensidad y direcion del viento segun sus componentes U y V \n Resultado del Proceso",
    latMin,
    latMax,
    lonMin,
    lonMax,
    bloquear=True)  # aca debe ir resultados
salir()

import sys
# sys.path.append('cgi-bin')
# from unificarDia import unificarDia, generearFranjaNC
from prepararObs import *
from tecnicas import *
from PlotObs import *
from exportarNetCDF import *


def salir():
    print "Gracias por usar Modulo ASCAT"
    sys.exit(0)


cont = 0
for elements in sys.argv:
    cont += 1

if cont < 4:
    print "Numero de parametros insuficiente, Los prametros basicos requeridos son: File path, Tecnica y Step"
    salir()

file_path = sys.argv[1]  # path del file a procesar
nombreArchivo = file_path[(len(file_path) - 59):(len(file_path) - 3)]

if not checkfile(file_path):
    print "No se encuentra el archivo indicado. Asegurese de ingresar la ruta completa."
    salir()

tecnica = sys.argv[2]  # 'SO' o 'T'

if str(tecnica) != 'SO' and str(tecnica) != 'T':
    print "Revise los parametros. Tecnicas posibles SO: SuperObbing, T: Thinning"
    salir()

step = sys.argv[3]  # considera obs cercanas

try:
    step = float(step)
except ValueError:
    print "El radio geografico debe ser un NUMERO."
    salir()
if cont > 4:
    if cont != 8:
        print "Parametros Obligados: File Path, Tecnica, Step. Parametros opcionales: Latitud Minima, latitud Maxima, longitud Minima, longitud Maxima. Para mas infromacion procesarASCAT.py -h"

if cont == 8:
    latMin = sys.argv[4]
    latMax = sys.argv[5]
    lonMin = sys.argv[6]
    lonMax = sys.argv[7]
    try:
        latMin = float(latMin)
        latMax = float(latMax)
        lonMin = float(lonMin)
        lonMax = float(lonMax)
    except ValueError:
        print "El latitudes y longitudes deben ser NUMEROS (Lats -90 a 90 Lons 0 a 360)."
        salir()
    if latMin > latMax or lonMin > lonMax:
        print "Revisar latidudes y longitudes ingresadas."
        salir()
    if latMin < -90 or latMax < -90:
        print "Latitudes o longitudes fuera del rango posible"
        salir()
    if lonMin < 0 or lonMax < 0:
        print "Latitudes o longitudes fuera del rango posible"
        salir()
    if latMin > 90 or latMax > 90:
        print "Latitudes o longitudes fuera del rango posible"
        salir()
    if lonMin > 360 or lonMax > 360:
        print "Latitudes o longitudes fuera del rango posible"
        salir()
else:
    latMax = 0.0
    latMin = -90
    lonMin = 220.0
    lonMax = 360  # valores Default

radioHorario = 60

lugar = 'Lats' + str(latMin) + '_' + str(latMax) + 'Lon' + str(lonMin) + '_' + str(lonMax)
coordenadas, obsTotales, obsSubSet = prepararObs(file_path, latMax, latMin, lonMin, lonMax)
coordPlot = coordenadas[:]  # necesario para realizar graficas.
resultado = tecnicas(coordenadas, step, tecnica, radioHorario)
nombre = 'procesado-' + str(nombreArchivo) + '-' + tecnica + 'Geo-' + lugar + '.nc'
exportarNetCDF(resultado, nombre, len(resultado))
print "Proceso finalizado satisfactoriamente. Puede encontrar el resultado en la carpeta ArchivosProcesados"
print "Generando Graficos..."
plotAscat(
    resultado,
    'ro',
    5,
    'Comparacion antes y despues de procesar',
    'Comparativa.\n Ubicacion de las observaciones nuevas (Rojo) y las originales (Azul)',
    latMin,
    latMax,
    lonMin,
    lonMax,
    coordPlot,
    'bo',
    2)
plotWinds(
    resultado,
    "Intensidad y direcion del viento segun sus componentes U y V \n Resultado del Proceso",
    latMin,
    latMax,
    lonMin,
    lonMax,
    bloquear=True)  # aca debe ir resultados
salir()
