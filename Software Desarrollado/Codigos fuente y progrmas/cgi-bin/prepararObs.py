# -*- coding: utf-8 -*-

from netCDF4 import Dataset
from PlotObs import *

def read_var(afile, variable):
    valores = afile.variables[variable][:][:]
    valoresVector = np.resize(valores, (valores.shape[0] * valores.shape[1]))
    # escala=afile.variables[variable].scale_factor
    # valoresVector=valoresVector*escala
    return valoresVector

def subSet(obs, latMax, latMin, lonMin, lonMax): #recorte Geografico
    obsReducido = []
    for i in range(len(obs)):
        if (long(obs[i][0]) < latMax) and (long(obs[i][1]) > lonMin):
            if (long(obs[i][0]) > latMin) and (long(obs[i][1]) < lonMax):
                obsReducido.append(obs[i])
    return obsReducido

def filtrarCalidad(obs): #elimina obs q no garanticen calidad
    obsDeCalidad = []
    for i in range(len(obs)):
        if (obs[i][6] == 0):  # flag en 0 es dato perfecto
            obsDeCalidad.append(obs[i])
    return obsDeCalidad

def prepararObs(nc_file, latMax, latMin, lonMin, lonMax):
    afile = Dataset(nc_file, "a")

    lats = read_var(afile, 'lat')
    lon = read_var(afile, 'lon')
    times = read_var(afile, 'time')
    wind_speeds = read_var(afile, 'wind_speed')
    wind_dirs = read_var(afile, 'wind_dir')
    flags = read_var(afile, 'wvc_quality_flag')
    # u = np.zeros(lats.size, np.float64)
    # v = np.zeros(lats.size, np.float32)
    # RMS = np.zeros(lats.size, np.float32)
    u = []
    v = []
    RMS = []
    # el RMS es fijo, ver pagina 18 ASCAT_Product_Manual 2.0
    lenOriginal = len(lats)
    for i in range(lats.size):
        u.append(0.0)
        v.append(0.0)
    for i in range(lats.size):
        # oceanographic convension
        u[i] = (float(wind_speeds[i] * np.sin(wind_dirs[i] * 3.14159 / 180.)))
        v[i] = (float(wind_speeds[i] * np.cos(wind_dirs[i] * 3.14159 / 180.)))
        # u.append(wind_speeds[i])
        # v.append(wind_dirs[i])
        RMS.append(2.0)

    obs = zip(lats, lon, times, u, v, RMS, flags)
    obsLatinoAmerica = subSet(obs, latMax, latMin, lonMin, lonMax)
    obsLatinoAmericaCalidad = filtrarCalidad(obsLatinoAmerica)

    lengFinal = lenOriginal - len(obsLatinoAmericaCalidad)
    print "Atencion! Se han descartado ", lengFinal, "mediciones, por no estar en el area de interes, o no poseer la calidad suficiente.", "</br>"

    return obsLatinoAmericaCalidad, obs, obsLatinoAmerica
