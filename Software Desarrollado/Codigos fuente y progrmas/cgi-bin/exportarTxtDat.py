#!/usr/bin/env python

def reformatArrays(resultado):
    rowU = []
    rowV = []
    for i in range(len(resultado)):
        auxU = []
        auxU.append(2819)  # id obs U
        auxU.append(resultado[i][0])  # lat
        auxU.append(resultado[i][1])  # lon
        auxU.append(1013)  # lev
        auxU.append(resultado[i][3])  # dato
        auxU.append(2.0)  # RMS
        auxU.append(20.0)  # id ascat
        rowU.append(auxU[:])

    for i in range(len(resultado)):
        auxV = []
        auxV.append(2820)  # id obs V
        auxV.append(resultado[i][0])  # lat
        auxV.append(resultado[i][1])  # lon
        auxV.append(1013)  # lev
        auxV.append(resultado[i][4])  # dato
        auxV.append(2.0)  # RMS
        auxV.append(20.0)  # id ascat
        rowV.append(auxV[:])

    newArray = zip(rowU, rowV)
    return newArray

def creacionTxt(nombreArchivo, resultado):
    nombreArchivo = nombreArchivo.replace("/DiasAscat/", "")
    nombreArchivo = 'procesado-' + nombreArchivo
    archi = open(nombreArchivo + '.txt', 'w')
    archi.close()
    # def grabartxt(resultados):
    componentes_separados = reformatArrays(resultado)  # u y v en lineas diferentes.
    for i in range(len(componentes_separados)):
        row = componentes_separados[i]
        for j in range(len(row)):
            archi = open(nombreArchivo + '.txt', 'a')
            archi.write("%d " % row[j][0])  # id_obs
            archi.write("%4.8f " % row[j][1])  # lat
            archi.write("%4.8f " % row[j][2])  # lon
            archi.write("%4.8f " % row[j][3])  # 1013
            archi.write("%4.8f " % row[j][4])  # dato
            archi.write("%4.8f " % row[j][5])  # rms
            archi.write("%4.8f \n" % row[j][6])  # 20
            archi.close()

def creacionDat(nombreArchivo, resultado):
    nombreArchivo = nombreArchivo.replace("/DiasAscat/", "")
    nombreArchivo = 'procesado-' + nombreArchivo
    archi = open(nombreArchivo + '.dat', 'w')
    archi.close()
    # def grabartxt(resultados):
    componentes_separados = reformatArrays(resultado)  # u y v en lineas diferentes.
    for i in range(len(componentes_separados)):
        row = componentes_separados[i]
        for j in range(len(row)):
            archi = open(nombreArchivo + '.dat', 'a')
            archi.write("%d " % row[j][0])  # id_obs
            archi.write("%4.8f " % row[j][1])  # lat
            archi.write("%4.8f " % row[j][2])  # lon
            archi.write("%4.8f " % row[j][3])  # 1013
            archi.write("%4.8f " % row[j][4])  # dato
            archi.write("%4.8f " % row[j][5])  # rms
            archi.write("%4.8f \n" % row[j][6])  # 20
            archi.close()
