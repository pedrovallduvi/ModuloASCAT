# -*- coding: utf-8 -*-
import os
from netCDF4 import Dataset

def clonarAscatReducido(nombreNuevo, rows, cells, path):
    if path[-1] != '/':
        path = path + "/"
    nc = Dataset(nombreNuevo, "w")
    nc.sync()
    nc.close()
    nc = Dataset(nombreNuevo, "a")
    # CREATE DIMENSIONS    ###############
    nc.createDimension('NUMROWS', rows)
    nc.createDimension('NUMCELLS', cells)
    # no deja incluir _FillValue da error: AttributeError: NetCDF: Not a valid data type or _FillValue type mismatch
    # print "Warning! el archivo generado sigue el formato de los file originales pero no es identico"
    # print ('WARNING: Some Variables has got an attribute named \'scale_factor\'.\n')
    # print ('This value is used by default when reading and assigning values to it, and might produce an error if this attribute is the wrong type.\n')
    # print ('If this is the case, use "nc.variables[\'VAR\'].set_auto_maskandscale(False)" to prevent scaling.\n')
    print '\n\n'

    # CREATE VARIABLES AND ATTRIBUTES    ###############
    nc.createVariable('time', 'i4', (u'NUMROWS', u'NUMCELLS'))
    # nc.variables['time'].setncattr('_FillValue', -2147483647)
    nc.variables['time'].setncattr('missing_value', -2147483647)
    nc.variables['time'].setncattr('valid_min', 0)
    nc.variables['time'].setncattr('valid_max', 2147483647)
    nc.variables['time'].setncattr('long_name', 'time')
    nc.variables['time'].setncattr('units', 'seconds since 1990-01-01 00:00:00')
    nc.variables['time'].setncattr('coordinates', 'lat lon')

    nc.createVariable('lat', 'i4', (u'NUMROWS', u'NUMCELLS'))
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

    nc.createVariable('lon', 'i4', (u'NUMROWS', u'NUMCELLS'))
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

    # TODO: se comentan todas las variables propias del ASCAT pero que no incluimos en el archivo.

    # nc.createVariable('wvc_index','i2',(u'NUMROWS', u'NUMCELLS'))
    # nc.variables['wvc_index'].setncattr('_FillValue', -32767)
    # nc.variables['wvc_index'].setncattr('missing_value', -32767)
    # nc.variables['wvc_index'].setncattr('valid_min', 0)
    # nc.variables['wvc_index'].setncattr('valid_max', 999)
    # nc.variables['wvc_index'].setncattr('long_name', 'cross track wind vector cell number')
    # nc.variables['wvc_index'].setncattr('units', '1')
    # nc.variables['wvc_index'].setncattr('coordinates', 'lat lon')

    # nc.createVariable('model_speed','i2',(u'NUMROWS', u'NUMCELLS'))
    # nc.variables['model_speed'].setncattr('_FillValue', -32767)
    # nc.variables['model_speed'].setncattr('missing_value', -32767)
    # nc.variables['model_speed'].setncattr('valid_min', 0)
    # nc.variables['model_speed'].setncattr('valid_max', 5000)
    # nc.variables['model_speed'].setncattr('long_name', 'model wind speed at 10 m')
    # nc.variables['model_speed'].setncattr('units', 'm s-1')
    # print ('WARNING: Variable model_speed has got an attribute named \'scale_factor\'.\n')
    # print ('This value is used by default when reading and assigning values to it, and might produce an error if this attribute is the wrong type.\n')
    # print ('If this is the case, use "nc.variables[\'model_speed\'].set_auto_maskandscale(False)" to prevent scaling.\n')
    # print  '\n\n\n'
    # nc.variables['model_speed'].setncattr('scale_factor', 0.01)
    # nc.variables['model_speed'].setncattr('add_offset', 0.0)
    # nc.variables['model_speed'].setncattr('coordinates', 'lat lon')

    # nc.createVariable('model_dir','i2',(u'NUMROWS', u'NUMCELLS'))
    # nc.variables['model_dir'].setncattr('_FillValue', -32767)
    # nc.variables['model_dir'].setncattr('missing_value', -32767)
    # nc.variables['model_dir'].setncattr('valid_min', 0)
    # nc.variables['model_dir'].setncattr('valid_max', 3600)
    # nc.variables['model_dir'].setncattr('long_name', 'model wind direction at 10 m')
    # nc.variables['model_dir'].setncattr('units', 'degree')
    # print ('WARNING: Variable model_dir has got an attribute named \'scale_factor\'.\n')
    # print ('This value is used by default when reading and assigning values to it, and might produce an error if this attribute is the wrong type.\n')
    # print ('If this is the case, use "nc.variables[\'model_dir\'].set_auto_maskandscale(False)" to prevent scaling.\n')
    # print  '\n\n\n'
    # nc.variables['model_dir'].setncattr('scale_factor', 0.1)
    # nc.variables['model_dir'].setncattr('add_offset', 0.0)
    # nc.variables['model_dir'].setncattr('coordinates', 'lat lon')

    # nc.createVariable('ice_prob','i2',(u'NUMROWS', u'NUMCELLS'))
    # nc.variables['ice_prob'].setncattr('_FillValue', -32767)
    # nc.variables['ice_prob'].setncattr('missing_value', -32767)
    # nc.variables['ice_prob'].setncattr('valid_min', 0)
    # nc.variables['ice_prob'].setncattr('valid_max', 1000)
    # nc.variables['ice_prob'].setncattr('long_name', 'ice probability')
    # nc.variables['ice_prob'].setncattr('units', '1')
    # print ('WARNING: Variable ice_prob has got an attribute named \'scale_factor\'.\n')
    # print ('This value is used by default when reading and assigning values to it, and might produce an error if this attribute is the wrong type.\n')
    # print ('If this is the case, use "nc.variables[\'ice_prob\'].set_auto_maskandscale(False)" to prevent scaling.\n')
    # print  '\n\n\n'
    # nc.variables['ice_prob'].setncattr('scale_factor', 0.001)
    # nc.variables['ice_prob'].setncattr('add_offset', 0.0)
    # nc.variables['ice_prob'].setncattr('coordinates', 'lat lon')

    # nc.createVariable('ice_age','i2',(u'NUMROWS', u'NUMCELLS'))
    # nc.variables['ice_age'].setncattr('_FillValue', -32767)
    # nc.variables['ice_age'].setncattr('missing_value', -32767)
    # nc.variables['ice_age'].setncattr('valid_min', -5000)
    # nc.variables['ice_age'].setncattr('valid_max', 5000)
    # nc.variables['ice_age'].setncattr('long_name', 'ice age (a-parameter)')
    # nc.variables['ice_age'].setncattr('units', 'dB')
    # print ('WARNING: Variable ice_age has got an attribute named \'scale_factor\'.\n')
    # print ('This value is used by default when reading and assigning values to it, and might produce an error if this attribute is the wrong type.\n')
    # print ('If this is the case, use "nc.variables[\'ice_age\'].set_auto_maskandscale(False)" to prevent scaling.\n')
    # print  '\n\n\n'
    # nc.variables['ice_age'].setncattr('scale_factor', 0.01)
    # nc.variables['ice_age'].setncattr('add_offset', 0.0)
    # nc.variables['ice_age'].setncattr('coordinates', 'lat lon')

    nc.createVariable('wvc_quality_flag', 'i4', (u'NUMROWS', u'NUMCELLS'))
    # nc.variables['wvc_quality_flag'].setncattr('_FillValue', -2147483647)
    nc.variables['wvc_quality_flag'].setncattr('missing_value', -2147483647)
    nc.variables['wvc_quality_flag'].setncattr('valid_min', 0)
    nc.variables['wvc_quality_flag'].setncattr('valid_max', 8388607)
    nc.variables['wvc_quality_flag'].setncattr('long_name', 'wind vector cell quality')
    nc.variables['wvc_quality_flag'].setncattr('coordinates', 'lat lon')
    nc.variables['wvc_quality_flag'].setncattr(
        'flag_masks',
        [64,
         128,
         256,
         512,
         1024,
         2048,
         4096,
         8192,
         16384,
         32768,
         65536,
         131072,
         262144,
         524288,
         1048576,
         2097152,
         4194304])
    nc.variables['wvc_quality_flag'].setncattr(
        'flag_meanings',
        'distance_to_gmf_too_large data_are_redundant no_meteorological_background_used rain_detected rain_flag_not_usable small_wind_less_than_or_equal_to_3_m_s large_wind_greater_than_30_m_s wind_inversion_not_successful some_portion_of_wvc_is_over_ice some_portion_of_wvc_is_over_land variational_quality_control_fails knmi_quality_control_fails product_monitoring_event_flag product_monitoring_not_used any_beam_noise_content_above_threshold poor_azimuth_diversity not_enough_good_sigma0_for_wind_retrieval')

    nc.createVariable('wind_speed', 'i4', (u'NUMROWS', u'NUMCELLS'))
    # nc.variables['wind_speed'].setncattr('_FillValue', -32767)
    nc.variables['wind_speed'].setncattr('missing_value', -32767)
    nc.variables['wind_speed'].setncattr('valid_min', 0)
    nc.variables['wind_speed'].setncattr('valid_max', 5000)
    nc.variables['wind_speed'].setncattr('long_name', 'wind speed at 10 m')
    nc.variables['wind_speed'].setncattr('units', 'm s-1')
    # print ('WARNING: Variable wind_speed has got an attribute named \'scale_factor\'.\n')
    # print ('This value is used by default when reading and assigning values to it, and might produce an error if this attribute is the wrong type.\n')
    # print ('If this is the case, use "nc.variables[\'wind_speed\'].set_auto_maskandscale(False)" to prevent scaling.\n')
    # print  '\n\n\n'
    nc.variables['wind_speed'].setncattr('scale_factor', 0.01)
    nc.variables['wind_speed'].setncattr('add_offset', 0.0)
    nc.variables['wind_speed'].setncattr('coordinates', 'lat lon')

    nc.createVariable('wind_dir', 'i4', (u'NUMROWS', u'NUMCELLS'))
    # nc.variables['wind_dir'].setncattr('_FillValue', -32767)
    nc.variables['wind_dir'].setncattr('missing_value', -32767)
    nc.variables['wind_dir'].setncattr('valid_min', 0)
    nc.variables['wind_dir'].setncattr('valid_max', 3600)
    nc.variables['wind_dir'].setncattr('long_name', 'wind direction at 10 m')
    nc.variables['wind_dir'].setncattr('units', 'degree')
    # print ('WARNING: Variable wind_dir has got an attribute named \'scale_factor\'.\n')
    # print ('This value is used by default when reading and assigning values to it, and might produce an error if this attribute is the wrong type.\n')
    # print ('If this is the case, use "nc.variables[\'wind_dir\'].set_auto_maskandscale(False)" to prevent scaling.\n')
    # print  '\n\n\n'
    nc.variables['wind_dir'].setncattr('scale_factor', 0.1)
    nc.variables['wind_dir'].setncattr('add_offset', 0.0)
    nc.variables['wind_dir'].setncattr('coordinates', 'lat lon')

    # nc.createVariable('bs_distance','i2',(u'NUMROWS', u'NUMCELLS'))
    # nc.variables['bs_distance'].setncattr('_FillValue', -32767)
    # nc.variables['bs_distance'].setncattr('missing_value', -32767)
    # nc.variables['bs_distance'].setncattr('valid_min', -500)
    # nc.variables['bs_distance'].setncattr('valid_max', 500)
    # nc.variables['bs_distance'].setncattr('long_name', 'backscatter distance')
    # nc.variables['bs_distance'].setncattr('units', '1')
    # print ('WARNING: Variable bs_distance has got an attribute named \'scale_factor\'.\n')
    # print ('This value is used by default when reading and assigning values to it, and might produce an error if this attribute is the wrong type.\n')
    # print ('If this is the case, use "nc.variables[\'bs_distance\'].set_auto_maskandscale(False)" to prevent scaling.\n')
    # print  '\n\n\n'
    # nc.variables['bs_distance'].setncattr('scale_factor', 0.1)
    # nc.variables['bs_distance'].setncattr('add_offset', 0.0)
    # nc.variables['bs_distance'].setncattr('coordinates', 'lat lon')

    # CREATE GLOBAL ATTRIBUTES    ###############
    nc.setncattr('title', 'MetOp-A ASCAT Level 2 25.0 km Ocean Surface Wind Vector Product')
    nc.setncattr('title_short_name', 'ASCAT-L2-25km')
    nc.setncattr('Conventions', 'CF-1.4')
    nc.setncattr('institution', 'EUMETSAT/OSI SAF/KNMI')
    nc.setncattr('source', 'MetOp-A ASCAT')
    nc.setncattr('software_identification_level_1', '801')
    nc.setncattr('instrument_calibration_version', '0')
    nc.setncattr('software_identification_wind', '2101')
    nc.setncattr('pixel_size_on_horizontal', '25.0 km')
    nc.setncattr('service_type', 'eps')
    nc.setncattr('processing_type', 'O')
    nc.setncattr('contents', 'ovw')
    nc.setncattr('granule_name', 'ascat_20121230_071202_metopa_32159_eps_o_250_2101_ovw.l2.nc')
    nc.setncattr('processing_level', 'L2')
    nc.setncattr('orbit_number', '32159')
    nc.setncattr('start_date', '2012-12-30')
    nc.setncattr('start_time', '07:12:02')
    nc.setncattr('stop_date', '2012-12-30')
    nc.setncattr('stop_time', '08:53:59')
    nc.setncattr('equator_crossing_longitude', ' 214.862')
    nc.setncattr('equator_crossing_date', '2012-12-30')
    nc.setncattr('equator_crossing_time', '07:10:14')
    nc.setncattr('rev_orbit_period', '6081.7')
    nc.setncattr('orbit_inclination', '98.7')
    nc.setncattr('history', 'N/A')
    nc.setncattr(
        'references',
        'ASCAT Wind Product User Manual, http://www.osi-saf.org/, http://www.knmi.nl/scatterometer/')
    nc.setncattr(
        'comment',
        'Orbit period and inclination are constant values. All wind directions in oceanographic convention (0 deg. flowing North)')

    nc.sync()
    nc.close()

    ubicacion = os.system('pwd')
    path1 = str(nombreNuevo)
    path2 = (path) + str(nombreNuevo)
    path2 = str(path2)
    print os.system('mv' + ' ' + path1 + ' ' + path2)
    return "Archivo clonado correctamente!"
