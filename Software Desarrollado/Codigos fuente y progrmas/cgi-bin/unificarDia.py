#!/usr/bin/env python
# -*- coding: utf-8
# import numpy as np
import os
from clonarAscatReducido import *
from exportarNetCDF import *
from rangoHorario import *

def unificarDia(pathDirectorio):
    # Variable para la ruta al directorio
    path = pathDirectorio + '/'
    # Lista vacia para incluir los ficheros
    lstFiles = []

    archivoUnificado = "UnificacionDiaCompleto.nc"  # nombre q tendra el archivo de ouput
    # Lista con todos los ficheros del directorio:
    lstDir = os.walk(path)  # os.walk()Lista directorios y ficheros
    # Crea una lista de los ficheros jpg que existen en el directorio y los incluye a la lista.
    for root, dirs, files in lstDir:
        for fichero in files:
            (nombreFichero, extension) = os.path.splitext(fichero)
            if (extension == ".nc"):
                lstFiles.append(path + nombreFichero + extension)
                # print (nombreFichero+extension)
    seteados = []
    for i in range(len(lstFiles)):
        # print lstFiles[i]
        seteados.append(Dataset(lstFiles[i], "a"))
    rows = 0
    for i in range(len(lstFiles)):
        rows = rows + seteados[i].dimensions['NUMROWS'].size

    clonarAscatReducido(archivoUnificado, rows, 42, path)
    # genera un archivo identico al ascat, con las dimen necesarias para poder volvar los datos recortados
    # la unica difer entre los archivos es q el nuevo no tine el attr
    # _fill_Value. x algun motivo no me deja incluirlo. ver clonarAscat.py
    archivoUnificado = path + archivoUnificado

    nc_file_new = Dataset(archivoUnificado, "a")
    v_time = []
    v_lat = []
    v_lon = []
    # v_wvc_index = []
    # v_model_speed = []
    # v_model_dir = []
    # v_ice_prob = []
    # v_ice_age = []
    v_wvc_quality_flag = []
    v_wind_speed = []
    v_wind_dir = []
    # v_bs_distance = []

    for i in range(len(lstFiles)):
        v_time.extend(seteados[i].variables['time'][:])
        v_lat.extend(seteados[i].variables['lat'][:])
        v_lon.extend(seteados[i].variables['lon'][:])
        v_wind_speed.extend(seteados[i].variables['wind_speed'][:])
        v_wind_dir.extend(seteados[i].variables['wind_dir'][:])
        v_wvc_quality_flag.extend(seteados[i].variables['wvc_quality_flag'][:])

    nc_file_new.variables['time'][:] = v_time[:][:]
    nc_file_new.variables['lat'][:] = v_lat[:]
    nc_file_new.variables['lon'][:] = v_lon[:]
    # nc_file_new.variables['wvc_index'][:] = v_wvc_index[:]
    # nc_file_new.variables['model_speed'][:] = v_model_speed[:]
    # nc_file_new.variables['model_dir'][:] = v_model_dir[:]
    # nc_file_new.variables['ice_prob'][:] = v_ice_prob[:]
    # nc_file_new.variables['ice_age'][:] = v_ice_age[:]
    nc_file_new.variables['wvc_quality_flag'][:] = v_wvc_quality_flag[:]
    nc_file_new.variables['wind_speed'][:] = v_wind_speed[:]
    nc_file_new.variables['wind_dir'][:] = v_wind_dir[:]
    # nc_file_new.variables['bs_distance'][:] = v_bs_distance[:]

    nc_file_new.sync()
    nc_file_new.close

    afile = path + "UnificacionDiaCompleto.nc"
    nc_file_new2 = Dataset(afile, "a")

    nc_file_new2.sync()
    nc_file_new2.close

    return afile
    # print(lstFiles)

def generearFranjaNC(dir_path, horaIni, horaFin, nombreTemporal):
    segs = rangoHorario(dir_path, horaIni, horaFin)
    segIni = segs[0]
    segFin = segs[1]
    afile = dir_path + "/UnificacionDiaCompleto.nc"
    #    nombreTemporal="franjaHoraria.nc"
    if checkfile(afile):
        fileUnificado = Dataset(
            afile,
            "a")  # no aplanar el vector. Por cada cell, comparar el primer y
                  # ultimo elemento. si cumple, agregar toda la cell.
    else:
        unificarDia(dir_path)
        fileUnificado = Dataset(afile, "a")
    # fileUnificado = Dataset(afile,"a") #no aplanar el vector. Por cada cell,
    # comparar el primer y ultimo elemento. si cumple, agregar toda la cell.
    # print fileUnificado.variables['time'][:]
    latsFranja = []
    lonFranja = []
    timesFranja = []
    WSFranja = []
    WDFranja = []
    flagsFranja = []

    tiempos = fileUnificado.variables['time'][:]
    latitudes = fileUnificado.variables['lat'][:]
    longitudes = fileUnificado.variables['lon'][:]
    speeds = fileUnificado.variables['wind_speed'][:]
    dirs = fileUnificado.variables['wind_dir'][:]
    flags = fileUnificado.variables['wvc_quality_flag'][:]

    for i in range(len(tiempos)):
        if (tiempos[i][0] > segIni) and (tiempos[i][41] < segFin):
            # print i
            timesFranja.append(tiempos[i])
            latsFranja.append(latitudes[i])
            lonFranja.append(longitudes[i])
            WSFranja.append(speeds[i])
            WDFranja.append(dirs[i])
            flagsFranja.append(flags[i])

    rows = len(timesFranja)
    clonarAscatReducido(nombreTemporal, rows, 42, dir_path)
    # print "Por favor, aguarde un momento..."
    archivoFranja = dir_path + '/' + nombreTemporal
    # print archivoFranja
    # os.system('cd ..')
    nc_file_new = Dataset(archivoFranja, "a")

    nc_file_new.variables['time'][:] = timesFranja[:]
    nc_file_new.variables['lat'][:] = latsFranja[:]
    nc_file_new.variables['lon'][:] = lonFranja[:]
    # nc_file_new.variables['wvc_index'][:] = v_wvc_index[:]
    # nc_file_new.variables['model_speed'][:] = v_model_speed[:]
    # nc_file_new.variables['model_dir'][:] = v_model_dir[:]
    # nc_file_new.variables['ice_prob'][:] = v_ice_prob[:]
    # nc_file_new.variables['ice_age'][:] = v_ice_age[:]
    # nc_file_new.variables['wvc_quality_flag'][:] = v_wvc_quality_flag[:]
    nc_file_new.variables['wind_speed'][:] = WSFranja[:]
    nc_file_new.variables['wind_dir'][:] = WDFranja[:]
    nc_file_new.variables['wvc_quality_flag'][:] = flagsFranja[:]
    # nc_file_new.variables['bs_distance'][:] = v_bs_distance[:]
    nc_file_new.sync()
    nc_file_new.close
