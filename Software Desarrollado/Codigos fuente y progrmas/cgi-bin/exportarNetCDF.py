#!/usr/bin/env python

from unificarDia import *
from netCDF4 import Dataset

def checkfile(archivo):
    # import os.path
    if os.path.exists(archivo):
        # print "El fichero existe"
        return True
    else:
        # print "El fichero no existe"
        return False

def exportarNetCDF(obs, nombreNuevo, rows):
    nombreNuevo = nombreNuevo.replace("/DiasAscat/", "")
    nc = Dataset(nombreNuevo, "w")
    nc.sync()
    nc.close()

    nc = Dataset(nombreNuevo, "a")

    # CREATE DIMENSIONS    ###############
    nc.createDimension('NUMROWS', rows)
    # nc.createDimension('longitude',lon)

    # print "Warning! el archivo generado es derivado de los originales ASCAt"
    # print ""
    # print ('WARNING: Some Variables has got an attribute named \'scale_factor\'.\n')
    # print ('WARNING: Some Variables has got an attribute named \'FillValue\'.\n')
    # print ('En el archivo se guardan los valores de viento, luego de realizado SO o thining')
    # print  '\n\n\n'

    # CREATE VARIABLES AND ATTRIBUTES    ###############
    nc.createVariable('time', 'i4', (u'NUMROWS'))
    # nc.variables['time'].setncattr('_FillValue', -2147483647)
    nc.variables['time'].setncattr('missing_value', -2147483647)
    nc.variables['time'].setncattr('valid_min', 0)
    nc.variables['time'].setncattr('valid_max', 2147483647)
    nc.variables['time'].setncattr('long_name', 'time')
    nc.variables['time'].setncattr('units', 'seconds since 1990-01-01 00:00:00')
    nc.variables['time'].setncattr('coordinates', 'lat lon')

    nc.createVariable('lat', 'i4', (u'NUMROWS'))
    # nc.variables['lat'].setncattr('_FillValue', -2147483647)
    nc.variables['lat'].setncattr('missing_value', -2147483647)
    nc.variables['lat'].setncattr('valid_min', -9000000)
    nc.variables['lat'].setncattr('valid_max', 9000000)
    nc.variables['lat'].setncattr('long_name', 'latitude')
    nc.variables['lat'].setncattr('units', 'degrees_north')
    # print ('WARNING: Variable lat has got an attribute named \'scale_factor\'.\n')
    # print ('This value is used by default when reading and assigning values to it, and might produce an error if this attribute is the wrong type.\n')
    # print ('If this is the case, use "nc.variables[\'lat\'].set_auto_maskandscale(False)" to prevent scaling.\n')
    # print  '\n\n\n'
    nc.variables['lat'].setncattr('scale_factor', 1e-05)
    nc.variables['lat'].setncattr('add_offset', 0.0)

    nc.createVariable('lon', 'i4', (u'NUMROWS'))
    # nc.variables['lon'].setncattr('_FillValue', -2147483647)
    nc.variables['lon'].setncattr('missing_value', -2147483647)
    nc.variables['lon'].setncattr('valid_min', 0)
    nc.variables['lon'].setncattr('valid_max', 36000000)
    nc.variables['lon'].setncattr('long_name', 'longitude')
    nc.variables['lon'].setncattr('units', 'degrees_east')
    # print ('WARNING: Variable lon has got an attribute named \'scale_factor\'.\n')
    # print ('This value is used by default when reading and assigning values to it, and might produce an error if this attribute is the wrong type.\n')
    # print ('If this is the case, use "nc.variables[\'lon\'].set_auto_maskandscale(False)" to prevent scaling.\n')
    # print  '\n\n\n'
    nc.variables['lon'].setncattr('scale_factor', 1e-05)
    nc.variables['lon'].setncattr('add_offset', 0.0)

    nc.createVariable('component_u', float, (u'NUMROWS'))
    nc.variables['component_u'].setncattr(
        'wind_component_u',
        'El comp U se obtiende la variale wind_speed y wind_dir del archivo ascat original')
    nc.variables['component_u'].setncattr('formula', 'u[i] = wind_speeds[i] *np.sin(wind_dirs[i]*3.14159/180.)')

    nc.createVariable('component_v', float, (u'NUMROWS'))
    nc.variables['component_v'].setncattr(
        'wind_component_v',
        'El comp V se obtiende la variale wind_speed y wind_dir del archivo ascat original')
    nc.variables['component_v'].setncattr('formula', '        v[i] = wind_speeds[i] *np.cos(wind_dirs[i]*3.14159/180.)')

    # CREATE GLOBAL ATTRIBUTES    ###############
    nc.setncattr('title', 'MetOp-A ASCAT Level 2 25.0 km Ocean Surface Wind Vector Product')
    nc.setncattr('title_short_name', 'ASCAT-L2-25km Solo Latino America con SuperObbing o Thining')
    nc.setncattr('Autor', 'Pedro Vallduvi')
    nc.setncattr(
        'Motivacion',
        'Se almacena informacion sobre archivos ascat, filtrados para LA, todos con flag de calidad = 0, desp de aplicarse Thinig o Super Obbing segun sea el caso.')
    nc.setncattr('source', 'MetOp-A ASCAT')
    nc.setncattr('pixel_size_on_horizontal', '25.0 km')
    nc.setncattr('service_type', 'eps')
    nc.setncattr('processing_type', 'O')
    nc.setncattr('contents', 'ovw')
    nc.setncattr('processing_level', 'L2')
    nc.setncattr('orbit_inclination', '98.7')
    nc.setncattr(
        'references',
        'ASCAT Wind Product User Manual, http://www.osi-saf.org/, http://www.knmi.nl/scatterometer/')
    nc.setncattr(
        'comment',
        'Orbit period and inclination are constant values. All wind directions in oceanographic convention (0 deg. flowing North)')

    nc.sync()
    nc.close()

    nc = Dataset(nombreNuevo, "a")
    time = []
    lat = []
    lon = []
    u = []
    v = []
    for i in range(len(obs)):
        time.append(obs[i][2])
        lat.append(obs[i][0])
        lon.append(obs[i][1])
        u.append(obs[i][3])
        v.append(obs[i][4])

    nc.variables['time'][:] = time[:]
    nc.variables['lat'][:] = lat[:]
    nc.variables['lon'][:] = lon[:]
    nc.variables['component_u'][:] = u[:]
    nc.variables['component_v'][:] = v[:]

    nc.sync()
    nc.close()

    ubicacion = os.getcwd()
    path1 = str(nombreNuevo)
    path2 = str(ubicacion) + '/ArchivosProcesados'
    os.system('mv' + ' ' + path1 + ' ' + path2)

