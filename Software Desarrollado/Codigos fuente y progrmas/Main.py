#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import sys
sys.path.append('cgi-bin')
from unificarDia import unificarDia, generearFranjaNC
from prepararObs import *
from tecnicas import *
from PlotObs import *
import Tkinter
import tkFileDialog
from exportarNetCDF import *
from exportarTxtDat import *
from exportarBufr import *

print "   "
print "   "
print"*******************************************************************************"
print"*      __  ___          __      __             ___   _____ _________  ______  *"
print"*     /  |/  /___  ____/ /_  __/ /___         /   | / ___// ____/   |/_  __/  *"
print"*    / /|_/ / __ \/ __  / / / / / __ \       / /| | \__ \/ /   / /| | / /     *"
print"*   / /  / / /_/ / /_/ / /_/ / / /_/ /      / ___ |___/ / /___/ ___ |/ /      *"
print"*  /_/  /_/\____/\__,_/\__,_/_/\____/      /_/  |_/____/\____/_/  |_/_/       *"
print"*                                                                             *"
print"*                                                                             *"
print"*                                                                             *"
print"*    Modulo ASCAT  Versión 1.0                                                *"
print"*    Autor: Pedro Vallduvi (pedro.vallduvi@yahoo.com)                         *"
print"*    Trabajo Final Lic. Sistemas de Informacion                               *"
print"*    Universidad Nacional del Nordeste - Corrientes, Argentina                *"
print"*******************************************************************************"

startGreen = "\033[92m"
startRed = "\033[91m"
end = "\033[0;0m"


def menuOpciones(op1=startGreen, op2=startGreen, op3=startGreen, op4=startGreen,
                 op5=startGreen, op6=startGreen, op7=startGreen, op8=startGreen):
    print "   "
    print "   "
    print "   "
    print op1 + " 1 ==> Descargar archivos ASCAT via FTP. " + end
    print op2 + " 2 ==> Seleccionar un archivo especifico a porcesar. " + end
    print op3 + " 3 ==> Seleccionar rango horario de un dia, para procesar." + end
    print op4 + " 4 ==> Aplicar SuperObbing. " + end
    print op5 + " 5 ==> Aplicar Thining. " + end
    print op6 + " 6 ==> Generear archivos de salida. (NetCDF, .txt, .dat y PrepBUFR)." + end
    print op7 + " 7 ==> Ver opciones graficas relacionadas." + end
    print op8 + " 8 ==> Salir." + end
    print "   "
    print "   "


def salir():
    print "Gracias por usar Modulo ASCAT"
    sys.exit(0)


def reiniciar():
    rta = -1
    while rta != 0 and rta != 1:
        try:
            rta = input("Desea continuar trabajando con el modulo? (1 => SI / 0 => NO): ")
        except Exception as e:
            areas = -1
    if rta == 1:
        os.system('python Main.py')
    else:
        salir()


def descargarAscat():
    cantDias = -1
    while cantDias != 1 and cantDias != 2:
    	cantDias = input ("Descargar un solo dia ==> 1 / Descargar multiples fechas ==> 2  :") 
	
	if cantDias == 1 : 
	
	    print "========== Ingresar Fecha se la cual se descargaran los archivos ========="
	    ano = input("Ingrese el año (yyyy): ")
	    ano = str(ano)
	    mes = raw_input("Ingres el mes (mm): ")
	    mes = str(mes)
	    dia = raw_input("ingrese el dia (dd): ")
	    dia = str(dia)
	    fecha = ano + " " + mes + " " + dia
	    path = "archivosASCAT" + ano + "-" + mes + "-" + dia
	    dia = os.system('sh descargar-podaac.sh ' + fecha)
	    os.system('cd ' + path)
	    path_dir = str(os.getcwd()) + "/DiasAscat/" + path
	    unificarDia(path_dir)
	    os.system('cd ..')
	    # os.system('python Main.py')
	    reiniciar()
	
	if cantDias == 2 :
	    print "========== Ingresar Fecha desde la cual se comenzara adescargar los archivos ========="
	    ano = input("Ingrese el año (yyyy): ")
	    ano = str(ano)
	    mes = raw_input("Ingres el mes (mm): ")
	    mes = str(mes)
	    dia = raw_input("Ingrese el dia (dd): ")
	    dia = str(dia)
	    rangoDias = raw_input("Idique la cantidad de dias que desea descargar partiendo de la fecha ingresada: ")
 	    diaFinal = int(dia)+int(rangoDias)
	    while diaFinal > 31 :
		rangoDias = raw_input("Asegurese de no exceder al mes ingresado. Re-ingrese cantidad de dias: ")
		diaFinal = int(dia)+int(rangoDias)
	    while int(dia) <= diaFinal:
		fecha = ano + " " + mes + " " + str(dia)
	        path = "archivosASCAT" + ano + "-" + mes + "-" + str(dia)
	        dia1 = os.system('sh descargar-podaac.sh ' + fecha)
	        os.system('cd ' + path)
	        path_dir = str(os.getcwd()) + "/DiasAscat/" + path
	        unificarDia(path_dir)
	        os.system('cd ..')
		dia = int(dia)
		dia = dia + 1
	    reiniciar()
		

def habilitarBotones(uno=None, dos=None,
                     tres=None, cuatro=None, cinco=None, seis=None,
                     siete=None, ocho=None):
    """ Esta funcion hablitia el ingreso de ciertas respuestas.
    Al invocar de debe hacer con numero=True sobre los valores que se cuentas como validos"""

    if uno:
        uno = 1
    if dos:
        dos = 2
    if tres:
        tres = 3
    if cuatro:
        cuatro = 4
    if cinco:
        cinco = 5
    if seis:
        seis = 6
    if siete:
        siete = 7
    if ocho:
        ocho = 8
    resp = -1
    while resp != uno and resp != dos and resp != tres and resp != cuatro and resp != cinco and resp != seis and resp != siete and resp != ocho:
        resp = input('Ingrese una de las opciones en verde: ')
    return resp


def seleccionarArchivo():
    root = Tkinter.Tk()  # esto se hace solo para eliminar la ventanita de Tkinter
    root.withdraw()  # ahora se cierra
    file_path = tkFileDialog.askopenfilename()
    print file_path
    nombreArchivo = file_path[(len(file_path) - 59):(len(file_path) - 3)]
    return file_path, nombreArchivo


def seleccionarDirectorio():
    print "Previemente usted debe haber descargado el dia completo (Opcion 1)"
    print "Seleccione el directorio donde se han almacenado los archivos correspondientes al dia."
    root = Tkinter.Tk()  # esto se hace solo para eliminar la ventanita de Tkinter
    root.withdraw()  # ahora se cierra
    dir_path = tkFileDialog.askdirectory()  # esta linea me devuelve el directorio

    horaInicio = input("Ingrese hora desde la cual desea obtener datos. 0 a 23 : ")
    horaFin = input("Ingrese hora hasta la cual desea obtener datos. 1 a 24 : ")
    while horaFin <= horaInicio or horaInicio < 0 or horaInicio > 23 or horaFin < 0 or horaInicio > 23:
        print "Verifique los horarios ingresados."
        horaInicio = input("Ingrese hora desde la cual desea obtener datos. 0 a 23 : ")
        horaFin = input("Ingrese hora hasta la cual desea obtener datos. 1 a 24 : ")

    generearFranjaNC(dir_path, horaInicio, horaFin, "archivoTemporal.nc")
    file_path = dir_path + '/archivoTemporal.nc'
    nombreArchivo = dir_path[(len(dir_path) - 10):] + 'Desde' + str(horaInicio) + 'Hasta' + str(horaFin)
    print "Directorio del dia: ", dir_path
    return file_path, dir_path, nombreArchivo


def seleccionarTecnica(latMin, latMax, lonMin, lonMax, file_path, step, nombreArchivo):
    menuOpciones(op1=startRed, op2=startRed, op3=startRed, op6=startRed, op7=startRed)
    nombre = " "
    resp = 0
    while resp != 4 and resp != 5 and resp != 8:
        try:
            resp = input("Se ha seleccinado el archivo, indique el modo de procesamiento: ")
        except Exception as e:
            resp = 0
    if resp == 4:
        tecnica = 'SO'
        radioHorario = 60
        print "Radio horario: 60 segundos"
        lugar = 'Lats' + str(latMin) + '_' + str(latMax) + 'Lon' + str(lonMin) + '_' + str(lonMax)
        coordenadas, obsTotales, obsSubSet = prepararObs(file_path, latMax, latMin, lonMin, lonMax)
        coordPlot = coordenadas[:]  # necesario para realizar graficas.
        resultado = tecnicas(coordenadas, step, tecnica, radioHorario)
    elif resp == 5:
        tecnica = 'T'
        radioHorario = 60
        print "Radio horario: 60 segundos"
        lugar = 'Lats' + str(latMin) + '_' + str(latMax) + 'Lon' + str(lonMin) + '_' + str(lonMax)
        coordenadas, obsTotales, obsSubSet = prepararObs(file_path, latMax, latMin, lonMin, lonMax)
        coordPlot = coordenadas[:]  # necesario para realizar graficas.
        resultado = tecnicas(coordenadas, step, tecnica, radioHorario)
    nombre = 'procesado-' + str(nombreArchivo) + '-' + tecnica + 'Geo-' + lugar + '.nc'
    return tecnica, radioHorario, lugar, coordenadas, obsTotales, obsSubSet, coordPlot, resultado, nombre


def definirLugar():
    latMax = 0.0
    latMin = -90
    lonMin = 220.0
    lonMax = 360  # valores Default

    print "Area geografica de procesamiento por defalut: LAT: (-90 a 0) LON: (220 a 360)"
    # step = step/2
    areas = -1
    while areas != 0 and areas != 1:
        try:
            areas = input("Desea cambiar el area geografica a calcular? (1 => SI / 0 => NO): ")
        except Exception as e:
            areas = -1

    if areas == 1:
        error = 0
        while error == 0:
            aux = None
            while aux != True:
                try:
                    latMax = input('Ingrese latitud maxima (-90 a 90): ')
                    aux = True
                except Exception as e:
                    aux = None
            aux = None
            while aux != True:
                try:
                    latMin = input('Ingrese latitud minima (-90 a 90): ')
                    aux = True
                except Exception as e:
                    aux = None
            if latMax < latMin:
                print "Latitud Maxima debe ser MAYOR a Latitud Minima."
            else:
                error = 1

        error = 0
        while error == 0:
            aux = None
            while aux != True:
                try:
                    lonMax = input('Ingrese longitud maxima (0 a 360): ')
                    aux = True
                except Exception as e:
                    aux = None
            aux = None
            while aux != True:
                try:
                    lonMin = input('Ingrese longitud minima (0 a 360): ')
                    aux = True
                except Exception as e:
                    aux = None
            if lonMax < lonMin:
                print "Longitud Maxima debe ser MAYOR a Longitud Minima."
            else:
                error = 1
    return latMin, latMax, lonMin, lonMax


def definirRadio():
    step = 0
    while step == 0:
    # while type(step) != float  or type(step) != int:
        try:
            step = input("Ingrese RADIO sobre el cual se concideran cercanas las observaciones (ej:0.30): ")
        except Exception as e:
            step = 0
    return step


def inicializar():
    file_path = " "
    dir_path = " "
    nombreArchivo = " "
    tecnica = " "
    lugar = " "
    nombre = " "

    step = 0
    latMin = 0
    latMax = 0
    lonMin = 0
    lonMax = 0
    radioHorario = 0

    coordenadas = []
    obsTotales = []
    obsSubSet = []
    coordPlot = []
    resultado = []


def menuGraficos(
    obsTotales,
    obsSubSet,
    coordPlot,
    resultado,
    latMin,
    latMax,
    lonMin,
    lonMax,
    nombreArchivo,
    tecnica,
    lugar,
        dir_path):
    cont = 1
    while cont == 1:
        print " "
        print startGreen, '1 ==> Recorrido del archivo original', end
        print startGreen, '2 ==> Componentes del viento en el archivo original', end
        print startGreen, '3 ==> Ubicacion de las observaciones en el area georafica seleccionada', end
        print startGreen, '4 ==> Componenetes del viento en el area georafica seleccionada', end
        print startGreen, '5 ==> Ubicaciones restantes luego de filtrar calidad', end
        print startGreen, '6 ==> Componentes del viento en las observaciones de calidad', end
        print startGreen, '7 ==> Ubicacion de las observaciones resultantes luego de aplicar SuperObbing / Thining', end
        print startGreen, '8 ==> Comparacion antes y despues de aplicar la tecnica seleccionada', end
        print startGreen, '9 ==> Componenetes del viento resultantes', end
        print startGreen, '0 ==> Volver al menu principal', end
        print " "
        opcion = input("Seleccione una de las opciones: ")

        if opcion == 1:
            plotAscat(
                obsTotales,
                'ro',
                3,
                'Observaciones totales',
                'Ubicacion de las mediciones en el archivo original')
        elif opcion == 2:
            plotWinds(obsTotales, "Intensidad del viento \n Archivo Original ")
        elif opcion == 3:
            plotAscat(
                obsSubSet,
                'ro',
                3,
                'Obeservaciones dentro del area seleccionada',
                'Posicion de las observaciones incluidas dentro del area geografica selecionada',
                latMin,
                latMax,
                lonMin,
                lonMax)
        elif opcion == 4:
            plotWinds(
                obsSubSet,
                "Intensidad y direcion del viento segun sus componentes U y V \n Archivo Recortado",
                latMin,
                latMax,
                lonMin,
                lonMax)
        elif opcion == 5:
            plotAscat(
                coordPlot,
                'ro',
                3,
                'Observaciones de calidad',
                'Posicion de las observaciones con calidad suficeinte para ser procesadas',
                latMin,
                latMax,
                lonMin,
                lonMax)
        elif opcion == 6:
            plotWinds(
                coordPlot,
                "Intensidad y direcion del viento segun sus componentes U y V \n Observaciones de calidad ",
                latMin,
                latMax,
                lonMin,
                lonMax)
        elif opcion == 7:
             plotAscat(
        	resultado,
        	'bo',
        	3,
        	'Observaciones resultantes',
        	'Ubicacion de las observaciones procesadas ',
        	latMin,
        	latMax,
        	lonMin,
        	lonMax,
 		coordPlot,
        	soloContar=True)
        elif opcion == 8:
            plotAscat(
                resultado,
                'ro',
                5,
                'Comparacion antes y despues de procesar',
                'Comparativa.\n Ubicacion de las observaciones procesadas (Rojo) y las originales (Azul)',
                latMin,
                latMax,
                lonMin,
                lonMax,
                coordPlot,
                'bo',
                2)
        elif opcion == 9:
            plotWinds(
                resultado,
                "Intensidad y direcion del viento segun sus componentes U y V \n Resultado del Proceso",
                latMin,
                latMax,
                lonMin,
                lonMax)  # aca debe ir resultados
        elif opcion == 0:
            segundaPantalla(
                obsTotales,
                obsSubSet,
                coordPlot,
                resultado,
                latMin,
                latMax,
                lonMin,
                lonMax,
                nombreArchivo,
                tecnica,
                lugar,
                dir_path)
        rta = -1
        while rta != 0 and rta != 1:
            try:
                rta = input("Desea generar otro grafico? (1 => SI / 0 => NO): ")
            except Exception as e:
                areas = -1
        if rta == 1:
            cont = 1
        elif rta == 0:
            segundaPantalla(
                obsTotales,
                obsSubSet,
                coordPlot,
                resultado,
                latMin,
                latMax,
                lonMin,
                lonMax,
                nombreArchivo,
                tecnica,
                lugar,
                dir_path)


def pantallaInicial():
    inicializar()
    menuOpciones(op4=startRed,
                 op5=startRed, op6=startRed, op7=startRed)
    resp = habilitarBotones(uno=True, dos=True, tres=True, ocho=True)
    if resp == 1:
        descargarAscat()
    elif resp == 2:
        file_path, nombreArchivo = seleccionarArchivo()
        step = definirRadio()
        latMin, latMax, lonMin, lonMax = definirLugar()
        tecnica, radioHorario, lugar, coordenadas, obsTotales, obsSubSet, coordPlot, resultado, nombre = seleccionarTecnica(
            latMin, latMax, lonMin, lonMax, file_path, step, nombreArchivo)
        segundaPantalla(
            obsTotales,
            obsSubSet,
            coordPlot,
            resultado,
            latMin,
            latMax,
            lonMin,
            lonMax,
            nombreArchivo,
            tecnica,
            lugar,
            dir_path=" ")
    elif resp == 3:
        file_path, dir_path, nombreArchivo = seleccionarDirectorio()
        step = definirRadio()
        latMin, latMax, lonMin, lonMax = definirLugar()
        tecnica, radioHorario, lugar, coordenadas, obsTotales, obsSubSet, coordPlot, resultado, nombre = seleccionarTecnica(
            latMin, latMax, lonMin, lonMax, file_path, step, nombreArchivo)
        segundaPantalla(
            obsTotales,
            obsSubSet,
            coordPlot,
            resultado,
            latMin,
            latMax,
            lonMin,
            lonMax,
            nombreArchivo,
            tecnica,
            lugar,
            dir_path)
    elif resp == 8:
        salir()


def segundaPantalla(
    obsTotales,
    obsSubSet,
    coordPlot,
    resultado,
    latMin,
    latMax,
    lonMin,
    lonMax,
    nombreArchivo,
    tecnica,
    lugar,
        dir_path):
    resp = -1
    menuOpciones(op1=startRed,
                 op2=startRed, op3=startRed, op4=startRed, op5=startRed)
    resp = habilitarBotones(seis=True, siete=True, ocho=True)
    if resp == 8:
        salir()
    if resp == 7:
        menuGraficos(
            obsTotales,
            obsSubSet,
            coordPlot,
            resultado,
            latMin,
            latMax,
            lonMin,
            lonMax,
            nombreArchivo,
            tecnica,
            lugar,
            dir_path)
    if resp == 6:
        print "Se generará el archivo en formato NetCDF para su almacenamiento"
    # nombre = raw_input("Ingrese  un nombre para el archivo:  ")
        nombre = 'procesado-' + nombreArchivo + '-' + tecnica + 'Geo-' + lugar
        print "Archivo salvado: ", nombre
    # os.system('cd '+ 'ArchivosProcesados')
        exportarNetCDF(resultado, nombre + '.nc', len(resultado))
        afile = dir_path + '/archivoTemporal.nc'
        if checkfile(afile):
            os.system('rm ' + afile)
        creacionTxt(nombreArchivo, resultado)
        creacionDat(nombreArchivo, resultado)
        os.system('mkdir ArchivosProcesados/' + nombre)
        os.system('mv procesado-' + nombreArchivo + '.txt' + ' ArchivosProcesados/' + nombre)
        os.system('mv procesado-' + nombreArchivo + '.dat' + ' ArchivosProcesados/' + nombre)
        os.system('mv ArchivosProcesados/' + nombre + '.nc' + ' ArchivosProcesados/' + nombre)
        escribirFortranBurf(nombreArchivo, resultado)
        os.system('$FC -c encode_ASCAT.f90')
        path_bufrlib = str(os.getcwd()) + "/BUFRLIB_v10-2-3"
        os.system('$FC -o encode_ASCAT.exe encode_ASCAT.o -L/' + path_bufrlib + ' -lbufr')
        os.system('./encode_ASCAT.exe')
        os.system('mv procesado-' + nombreArchivo + '.bufr' + ' ArchivosProcesados/' + nombre)
        os.system('rm encode_ASCAT.f90')
        os.system('rm encode_ASCAT.o')
        os.system('rm encode_ASCAT.exe')
        print "Todos los archivos de salida han sido generados y guardados en ArchivosProcesados/", nombre

    reiniciar()

pantallaInicial()
