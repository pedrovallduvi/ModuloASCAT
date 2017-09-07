# -*- coding: utf-8 -*-

from time import *
from PlotObs import *

def superObbing(coordenadas, step, radioHorario=450):
    popers = []
    vectorLatsOb = []
    vectorLonOb = []
    vectorTimes = []
    vectorU = []
    vectorV = []
    vectorRMS = []
    vectorFlags = []
    auxLat = []
    auxLon = []
    auxU = []
    auxV = []
    print "========== SE HA APLICADO SUPER OBBING A LAS OBSERVACIONES ===========", "</br>"

    while (len(coordenadas)) != 0:

        if len(auxLat) != 0:
            vectorLatsOb.append(np.average(auxLat))
            vectorLonOb.append(np.average(auxLon))
            vectorTimes.append(timeParametro)
            vectorU.append(np.average(auxU))
            vectorV.append(np.average(auxV))
            vectorRMS.append(2.0)
            vectorFlags.append(0)

        auxLat = []
        auxLon = []
        auxU = []
        auxV = []

        # step = espacio
        retMin = (coordenadas[0][0] - step), (
            coordenadas[0][1] - step)
        retMax = (coordenadas[0][0] + step), (
            coordenadas[0][1] + step)
        timeParametro = coordenadas[0][2]
        popers = []

        for j in range(len(coordenadas)):
            if (coordenadas[j][0] > retMin[0]) and (coordenadas[j][0] < retMax[0]):
                if (coordenadas[j][1] > retMin[1]) and (coordenadas[j][1] < retMax[1]):
                    # if times[j] == timeParametro: #por cada instante, 42
                    # medidas. Aseguro que los promedios
                    # sean del mismo momento
                    if (timeParametro - radioHorario < coordenadas[j][2] < timeParametro + radioHorario):
                        auxLat.append(coordenadas[j][0])
                        auxLon.append(coordenadas[j][1])
                        auxU.append(coordenadas[j][3])
                        auxV.append(coordenadas[j][4])
                        popers.append(j)

        popers = popers[::-1]
        # NECESARIO NO MODIFICAR LAS UBICACIONES AL IR
        # BORRANDO.

        for k in range(len(popers)):  # elimino coords q ya fueron ubicdas en una celda
            coordenadas.pop(popers[k])

    ResultadoObs = zip(vectorLatsOb, vectorLonOb,
                       vectorTimes, vectorU, vectorV, vectorRMS, vectorFlags)
    print "Cantidad de Observaciones restantes despues de aplicar Super Obbing: ", len(ResultadoObs), "</br>"
    return ResultadoObs


def thining(coordenadas, step, radioHorario=450):
    popers = []
    vectorLatsOb = []
    vectorLonOb = []
    vectorTimes = []
    vectorU = []
    vectorV = []
    vectorRMS = []
    vectorFlags = []
    auxLat = []
    auxLon = []
    auxU = []
    auxV = []

    print "========== SE HA APLICADO THINING A LAS OBSERVACIONES ===========", "</br>"

    while (len(coordenadas)) != 0:
        if len(auxLat) != 0:  # tomo los elemtos centrales, descarto los otros. Consultar.
            vectorLatsOb.append(auxLat[(len(auxLat) / 2)])
            vectorLonOb.append(auxLon[(len(auxLon) / 2)])
            vectorTimes.append(timeParametro)
            vectorU.append(auxU[(len(auxU) / 2)])
            vectorV.append(auxV[(len(auxV) / 2)])
            vectorRMS.append(2.0)
            vectorFlags.append(0)

        auxLat = []
        auxLon = []
        auxU = []
        auxV = []

        # step = espacio
        retMin = (coordenadas[0][0] - step), (
            coordenadas[0][1] - step)
        retMax = (coordenadas[0][0] + step), (
            coordenadas[0][1] + step)
        timeParametro = coordenadas[0][2]
        popers = []

        for j in range(len(coordenadas)):
            if (coordenadas[j][0] > retMin[0]) and (coordenadas[j][0] < retMax[0]):
                if (coordenadas[j][1] > retMin[1]) and (coordenadas[j][1] < retMax[1]):
                    # if times[j] == timeParametro: #por cada instante, 42
                    # medidas. Aseguro que los promedios
                    # sean del mismo momento
                    if (timeParametro - radioHorario < coordenadas[j][2] < timeParametro + radioHorario):
                        auxLat.append(coordenadas[j][0])
                        auxLon.append(coordenadas[j][1])
                        auxU.append(coordenadas[j][3])
                        auxV.append(coordenadas[j][4])
                        popers.append(j)

        popers = popers[::-1]
        # NECESARIO NO MODIFICAR LAS UBICACIONES AL IR
        # BORRANDO.

        for k in range(len(popers)):  # elimino coords q ya fueron ubicdas en una celda
            coordenadas.pop(popers[k])
    ResultadoObs = zip(vectorLatsOb, vectorLonOb,
                       vectorTimes, vectorU, vectorV, vectorRMS, vectorFlags)
    print "Cantidad de Observaciones restantes despues de aplicar Thinig: ", len(ResultadoObs), "</br>"
    return ResultadoObs


def tecnicas(coordenadas, step, tecnica, radioHorario=450):
    tiempo_inicial = time()
    # print "ESPERE UN MOMENTO POR FAVOR... ESTO PUEDE DEMORAR ALGUNOS
    # MINUTOS..."
    # print coordenadas
    # coordPlot = coordenadas[:] #para plotear la diferencia
    # print "cant de puntos a analizar: ", len(lats)
    # lats = lats[0:1000] #reduir los vectores para probar funconamiento mas rapido.
    # lon = lon[0:1000]
    # coordenadas = zip(lats,lon,times)
    # print coordenadas
    print "Observaciones procesadas: ", len(coordenadas), "</br>"

    if tecnica == 'SO':
        ResultadoObs = superObbing(coordenadas, step, radioHorario)

    if tecnica == 'T':
        ResultadoObs = thining(coordenadas, step, radioHorario)

    tiempo_final = time()
    tiempo_ejecucion = tiempo_final - tiempo_inicial

    print 'El tiempo de ejecucion fue:', tiempo_ejecucion, " segundos", "</br>"
    # print "Fin de la tecnica"
    return ResultadoObs
