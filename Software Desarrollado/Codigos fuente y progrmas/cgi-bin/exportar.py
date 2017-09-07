#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cgi
import os

print "Content-type: text/html"
print ""
print """
<script language="javascript">
function copy_address() {
    document.getElementById('latMin2').value = document.getElementById('latMin').value;
    document.getElementById('latMax2').value = document.getElementById('latMax').value;
    document.getElementById('lonMin2').value = document.getElementById('lonMin').value;
    document.getElementById('lonMax2').value = document.getElementById('lonMax').value;
}
</script>
"""

print "<html>"

print """<head>
<title>Modulo ASCAT</title>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<link rel="stylesheet" type="text/css" href="/style.css" media="screen" />
</head>
<body>
<div id="wrap">
<div id="header">
<h1><a href="/cgi-bin/portalAscat.py">Modulo ASCAT</a></h1>
<h2> Bienvenidos... </h2>
<div id="subtitulo">
<h2></h2>
<h2>Autor: Pedro Vallduví (pedro.vallduvi@yahoo.com).</h2>
<h2>Trabajo Final Lic. Sistemas de Información.</h2>
<h2>Universidad Nacional del Nordeste - Corrientes, Argentina.</h2>
<h2>Facultad de Cs. Exactas, Naturales y Agrimensura.</h2>
</div>
</div>
</br>"""
print """
<div>
<a href="/cgi-bin/portalAscat.py">
<img src="../images/imagenFinal6.jpg" width="760" height="500"/>
</a>
</div>"""
netcdf = 'no'
bufr = 'no'
txt = 'no'
dat = 'no'
form_input = cgi.FieldStorage()

nombre = form_input["path"].value
try:
    netcdf = form_input["netcdf"].value
except KeyError:
    pass
try:
    bufr = form_input["bufr"].value
except KeyError:
    pass
try:
    txt = form_input["txt"].value
except KeyError:
    pass
try:
    dat = form_input["dat"].value
except KeyError:
    pass

if netcdf == 'no' and bufr == 'no' and txt == 'no' and dat == 'no':
    os.system('rm -r ArchivosProcesados/' + nombre)

if netcdf == 'no':
    ubicacion = os.getcwd()
    path1 = str(ubicacion) + '/ArchivosProcesados' + '/' + nombre + '/' + nombre + '.nc'
    os.system('rm' + ' ' + path1)

if bufr == 'no':
    ubicacion = os.getcwd()
    path1 = str(ubicacion) + '/ArchivosProcesados' + '/' + nombre + '/' + 'procesado-' + nombre + '.bufr'
    os.system('rm' + ' ' + path1)

if txt == 'no':
    ubicacion = os.getcwd()
    path1 = str(ubicacion) + '/ArchivosProcesados' + '/' + nombre + '/' + 'procesado-' + nombre + '.txt'
    os.system('rm' + ' ' + path1)

if dat == 'no':
    ubicacion = os.getcwd()
    path1 = str(ubicacion) + '/ArchivosProcesados' + '/' + nombre + '/' + 'procesado-' + nombre + '.dat'
    os.system('rm' + ' ' + path1)
