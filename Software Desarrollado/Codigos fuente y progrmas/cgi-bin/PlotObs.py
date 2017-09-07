# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from matplotlib.pyplot import cm
from mpl_toolkits.basemap import Basemap


def plotAscat(obs, color, size, titImagen="Grafico Ascat", titulo="",
              latMin=-90, latMax=90, lonMin=0, lonMax=360, comparar=[],
              color2='bo', size2=0, bloquear=False, soloContar=False):  # color es 'bo' o 'ro'
    # comparar es un parametro opcional, si se queire plotear en el mismo mapa el antes y desp de SO

    lats = []
    lons = []
    for i in range(len(obs)):
        lats.append(obs[i][0])
        lons.append(obs[i][1])
    latsComp = []
    lonsComp = []
    for i in range(len(comparar)):
        latsComp.append(comparar[i][0])
        lonsComp.append(comparar[i][1])

    raw_data = {'latitude': lats,
                'longitude': lons}
    df = pd.DataFrame(raw_data, columns=['latitude', 'longitude'])
    df
    raw_data_comp = {'latitudeComp': latsComp,
                     'longitudeComp': lonsComp}

    dfComp = pd.DataFrame(raw_data_comp, columns=['latitudeComp', 'longitudeComp'])
    dfComp

    fig = plt.figure(titImagen, figsize=(14, 8))
    plt.title(titulo, fontsize=20)

    # Crea el mapa, usando Gall–Peters projection,
    mapa = Basemap(projection='gall',
                   llcrnrlon=lonMin,  # esquina inferior izquiereda - longitud
                   llcrnrlat=latMin,  # esquina inferior izquiereda - latitud
                   urcrnrlon=lonMax,  # esquina superior derecha longitude
                   urcrnrlat=latMax,  # esquina superior derecha latitude
                   # low resolution, l, resolucion baja. h es alta.
                   resolution='l',
                   # And threshold 100000
                   area_thresh=100000.0,
                   # Centered at 0,0 (i.e null island)
                   lat_0=0, lon_0=0)

    # Draw the coastlines on the map
    mapa.drawcoastlines()
    # Draw country borders on the map
    mapa.drawcountries()
    mapa.drawparallels(np.arange(latMin, latMax, 10), labels=[1, 1, 0, 0])
    mapa.drawmeridians(np.arange(lonMin, lonMax, 20), labels=[0, 0, 0, 1])
    # Fill the land with grey
    mapa.fillcontinents(color='gainsboro')
    # Draw the map boundaries
    mapa.drawmapboundary(fill_color='steelblue')
    # Definimos los punto de latitud y lingitud.
    # se tiene que usar values por un extraño bug en pandas pasando datos a basemap.
    x, y = mapa(df['longitude'].values, df['latitude'].values)
    xComp, yComp = mapa(dfComp['longitudeComp'].values, dfComp['latitudeComp'].values)
    cantidadObs = 'Cantidad de Obs: ' + str(len(obs))

    mapa.plot(x, y, color, markersize=size, label=(str(cantidadObs)))
    if soloContar == True:
	cantidadObs3 = 'Cantidad antes de la compresion: ' + str(len(latsComp))
	mapa.plot(0,0,color2,markersize=0.1,label=(str(cantidadObs3)))

    if len(latsComp) > 0:
        cantidadObs2 = 'Cantidad de Obs: ' + str(len(latsComp))
	if soloContar == False: 
        	mapa.plot(xComp, yComp, color2, markersize=size2, label=(str(cantidadObs2)))
		
    plt.legend()
    plt.show(block=bloquear)
    # Show the map
    return "Print, Graficas "


def plotWinds(obs, titulo="Intensidad y direcion del viento segun sus componentes U y V",
              latMin=-90, latMax=90, lonMin=0, lonMax=360, bloquear=False):  # color es 'bo' o 'ro'
    titImagen = "Grafico Ascat - Velocidad y Direccion"
    lats = []
    lons = []
    windu = []
    windv = []
    # obs = [lats, lon, times, u , v,RMS, flags]
    for i in range(len(obs)):
        lats.append(obs[i][0])
        lons.append(obs[i][1])
        windu.append(obs[i][3])
        windv.append(obs[i][4])

    raw_data = {'latitude': lats,
                'longitude': lons}

    df = pd.DataFrame(raw_data, columns=['latitude', 'longitude'])
    df
    fig = plt.figure(titImagen, figsize=(14, 8))
    plt.title(titulo, fontsize=20)
    # Crea el mapa, usando Gall–Peters projection,
    mapa = Basemap(projection='gall',
                   llcrnrlon=lonMin,  # esquina inferior izquiereda - longitud
                   llcrnrlat=latMin,  # esquina inferior izquiereda - latitud
                   urcrnrlon=lonMax,  # esquina superior derecha longitude
                   urcrnrlat=latMax,  # esquina superior derecha latitude
                   # with low resolution,
                   resolution='l',
                   # And threshold 100000
                   area_thresh=100000.0,
                   # Centered at 0,0 (i.e null island)
                   lat_0=0, lon_0=0)

    # Draw the coastlines on the map
    mapa.drawcoastlines()
    # Draw country borders on the map
    mapa.drawcountries()
    mapa.drawparallels(np.arange(latMin, latMax, 10), labels=[1, 1, 0, 0])
    mapa.drawmeridians(np.arange(lonMin, lonMax, 20), labels=[0, 0, 0, 1])
    # Fill the land with grey
    mapa.fillcontinents(color='gainsboro')
    # Draw the map boundaries
    mapa.drawmapboundary(fill_color='steelblue')
    # Definimos los punto de latitud y lingitud.
    # se tiene que usar values por un extraño bug en pandas pasando datos a basemap.
    x, y = mapa(df['longitude'].values, df['latitude'].values)
    u = []
    for i in windu:
        u.append(i * 3.600000)  # transformo de m/seg a km/hs
    v = []
    for i in windv:
        # v = windv
        v.append(i * 3.600000)  # transformo de m/seg a km/hs

    norm = []
    UN = []
    VN = []

    for i in range(len(u)):
        norm.append(np.sqrt(u[i] ** 2 + v[i] ** 2))  # Normalizando componentes u y v

    for i in range(len(u)):
        UN.append((u[i] / (norm[i])))
        VN.append((v[i] / (norm[i])))  # normaliza los valores para q las flechas sean de igual longitud

    plt.quiver(x, y, UN, VN,  # data
               norm, # colour the arrows based on this array
               cmap=cm.spectral,  # colour map
               headlength=6,headwidth=0.8,
	       units='x')  # length of the arrows

    mini = min(norm)
    maxi = max(norm)
    cbar = plt.colorbar(orientation="horizontal", fraction=0.050)
    cbar.set_clim(mini, maxi)
    cbar.set_label("Velocidad [km/h]")
    plt.show(block=bloquear)
    # Show the map


def plotArea(latMin, latMax, lonMin, lonMax, bloquear=True):
    fig = plt.figure("Area seleccionada", figsize=(20, 10))
    plt.title("Area geografica seleccioada \n Solo se procesaran los datos de esta region", fontsize=20)

    # Crea el mapa, usando Gall–Peters projection,
    mapa = Basemap(projection='gall',
                   llcrnrlon=lonMin,  # esquina inferior izquiereda - longitud
                   llcrnrlat=latMin,  # esquina inferior izquiereda - latitud
                   urcrnrlon=lonMax,  # esquina superior derecha longitude
                   urcrnrlat=latMax,  # esquina superior derecha latitude
                   # with low resolution,
                   resolution='l',
                   # And threshold 100000
                   area_thresh=100000.0,
                   # Centered at 0,0 (i.e null island)
                   lat_0=0, lon_0=0)

    # Draw the coastlines on the map
    mapa.drawcoastlines()
    # Draw country borders on the map
    mapa.drawcountries()
    # Fill the land with grey
    mapa.fillcontinents(color='gainsboro')
    # Draw the map boundaries
    mapa.drawmapboundary(fill_color='steelblue')

    mapa.drawparallels(np.arange(latMin, latMax, 10), labels=[1, 1, 0, 0])
    mapa.drawmeridians(np.arange(lonMin, lonMax, 20), labels=[0, 0, 0, 10])
    plt.show(block=bloquear)
