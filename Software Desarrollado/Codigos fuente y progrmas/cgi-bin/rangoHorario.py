# -*- coding: utf-8 -*-

from datetime import datetime, timedelta

def dameFecha(dir_path, hora):
    fecha = []
    letra = ''

    while letra != 'T':
        fecha.insert(0, dir_path[-1])
        leng = len(dir_path)
        dir_path = dir_path[0:(leng - 1)]
        letra = dir_path[-1]

    anho = 0
    mes = 0
    dia = 0
    # print len(fecha)

    if len(fecha) == 10:
        # anho =  fecha[0:4]
        anho = int(''.join(map(str, fecha[0:4])))
        mes = int(''.join(map(str, fecha[5:7])))
        dia = int(''.join(map(str, fecha[8:10])))

    if (len(fecha) == 9) and (int(''.join(map(str, fecha[7:9]))) > 10):
        # anho =  fecha[0:4]
        anho = int(''.join(map(str, fecha[0:4])))
        mes = int(''.join(map(str, fecha[5])))
        dia = int(''.join(map(str, fecha[7:9])))

    if (len(fecha) == 9) and (int(''.join(map(str, fecha[7:9]))) < 10):
        anho = int(''.join(map(str, fecha[0:4])))
        mes = int(''.join(map(str, fecha[5:7])))
        dia = int(''.join(map(str, fecha[8])))

    if len(fecha) == 8:
        # anho =  fecha[0:4]
        anho = int(''.join(map(str, fecha[0:4])))
        mes = int(''.join(map(str, fecha[5])))
        dia = int(''.join(map(str, fecha[7])))

    if hora == 24:
        yourTime = datetime(anho, mes, dia, hora - 1)
        yourTime = yourTime + timedelta(seconds=900)
    else:
        yourTime = datetime(anho, mes, dia, hora)

    return yourTime

def dameSegundos(fecha):
    since = datetime(1990, 1, 1, 0, 0, 0)
    # mytime = datetime( 2016, 8, 18, 00, 18, 0 )
    diff_seconds = (fecha - since).total_seconds()
    return diff_seconds


def rangoHorario(dir_path, horaInicio, horaFin):
    # datetime epieza en 1970
    # seconds since 1990-01-01 00:00:00
    fechaInicio = dameFecha(dir_path, horaInicio)
    fechaFin = dameFecha(dir_path, horaFin)

    segIni = dameSegundos(fechaInicio)
    segFin = dameSegundos(fechaFin)

    return segIni, segFin

