#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cgi

from PlotObs import *
from exportarBufr import *
from exportarNetCDF import *
from exportarTxtDat import *
from prepararObs import *
from tecnicas import *

print "Content-type: text/html"
print ""
print """ <script type='text/JavaScript'>
function blmostrocult(blconted) {
var c=blconted.nextSibling;
if(c.style.display=='none') {
c.style.display='block';
} else {
c.style.display='none';
}
return false;
}
</script>"""
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
<div class="alert">
  <span class="closebtn" onclick="this.parentElement.style.display='none';">&times;</span>
   <h4>Asegurese de seleccionar una de las opciones y luego presionar 'Continuar' </br>
        De no ser asi, es probable que archivos no deseados queden en su sistema .</h4>
</div>


<div id="wrap">

<div id="header">
<h1><a>Modulo ASCAT</a></h1>
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

form_input = cgi.FieldStorage()
tecnica = form_input["tecnica"].value
step = form_input["step"].value
latMax = form_input["latMax"].value
latMin = form_input["latMin"].value
lonMax = form_input["lonMax"].value
lonMin = form_input["lonMin"].value

dir_path = ""

try:
    file_path = form_input["path"].value
    nombreArchivo = file_path[(len(file_path) - 59):(len(file_path) - 3)]
except KeyError:
    pass

try:
    dir_path = form_input["dir_path"].value
    file_path = dir_path + '/archivoTemporal.nc'
    nombreArchivo = "franjaHoraia-" + (dir_path[(dir_path.index('T') + 1):(len(dir_path))])
except KeyError:
    pass

radioHorario = form_input["radioHorario"].value

lugar = 'Lats' + str(latMin) + '_' + str(latMax) + 'Lon' + str(lonMin) + '_' + str(lonMax)

latMax = float(latMax[:])
latMin = float(latMin[:])
lonMax = float(lonMax[:])
lonMin = float(lonMin[:])
step = float(step[:])
radioHorario = int(radioHorario[:])

print "<div id=marco>"
print "<fieldset>"
print "<legend> <h2> Resumen del procesamiento </h2> </legend>"

print "<h4>"
print "<p>"
coordenadas, obsTotales, obsSubSet = prepararObs(file_path, latMax, latMin, lonMin, lonMax)

coordPlot = coordenadas[:]  # necesario para realizar graficas.
resultado = tecnicas(coordenadas, step, tecnica, radioHorario)
nombre = str(nombreArchivo) + '-' + tecnica + 'Geo-' + lugar
creacionTxt(nombre, resultado)
creacionDat(nombre, resultado)
escribirFortranBurf(nombreArchivo, resultado)
exportarNetCDF(resultado, nombre + '.nc', len(resultado))
afile = dir_path + '/archivoTemporal.nc'
if checkfile(afile):
    os.system('rm ' + afile)

ubicacion = os.getcwd()
nombre = nombre.replace("/DiasAscat/", "")
nombreArchivo = nombreArchivo.replace("/DiasAscat/", "")
newUbicacion = ubicacion.replace('cgi-bin', '')
os.system('mkdir ArchivosProcesados/' + nombre)
os.system('mv ' + newUbicacion + '/' + 'procesado-' + nombre + '.txt' + ' ArchivosProcesados/' + nombre)
os.system('mv ' + newUbicacion + '/' + 'procesado-' + nombre + '.dat' + ' ArchivosProcesados/' + nombre)
os.system('mv ArchivosProcesados/' + nombre + '.nc' + ' ArchivosProcesados/' + nombre)
# comandos para BUFR.
os.system('$FC -c encode_ASCAT.f90')
path_bufrlib = str(os.getcwd()) + "/BUFRLIB_v10-2-3"
os.system('$FC -o encode_ASCAT.exe encode_ASCAT.o -L/' + path_bufrlib + ' -lbufr')
os.system('./encode_ASCAT.exe')
os.system('mv procesado-' + nombreArchivo + '.bufr' + ' ArchivosProcesados/' + nombre)
os.system('rm encode_ASCAT.f90')
os.system('rm encode_ASCAT.o')
os.system('rm encode_ASCAT.exe')

print "</p>"
print "</h4>"
print "</filedset>"
print "</div>"
print "</br>"

print "<div id=marco>"
print "<fieldset>"
print "<legend> <h2> Exportar resultados </h2> </legend>"

print """ <form action="/cgi-bin/exportar.py" method="post" target="_self" enctype="multipart/form-data" >"""
print """ <div class='box-gray2'>
	<h3> <big><u> Seleccione las opciones de su interes: </big></u> <h3>  <p></p>

</h3>

<a onclick="return blmostrocult(this);" style="cursor: hand; cursor: pointer;">  <p>Información</p></a><div style="display: none;">
<p><h5>El proceso genera cuatro archivos de salida. Todos contienen la misma información procesada, pero cada uno es codificado en un formato diferente. Aprovechando las ventajas que presenta cada uno y para posibilitar la visualización, almacenamiento y posterior asimilación de los datos. </br>
Seleccione los archivos que desea conservar y podrá encontrarlos en una carpeta especifica creada dentro del directorio '/ArchivosProcesados'.
 </h5></p>
</div>
<div id=cheks2 >

<h3>	<input type="checkbox" name="netcdf" value="si" /> Conservar el archivo para almacenamiento. Formato NetCDF  <br />

	<input type="checkbox" name="bufr" value="si" /> Conservar archivo  de salida en formato BUFR <br />

         <input type="checkbox" name="txt" value="si" /> Conservar archivo de salida en formato  ASCII  (.txt)   <br />

         <input type="checkbox" name="dat" value="si" /> Conservar archivo de salida en formato binario, para procesamiento (.dat)  <br />
<input type="hidden" name="path" value=""", nombre, """ >
</br> </div>
<input class="btn3" type="submit" value="Continuar" />
</h3>

</form>
</br>"""

print "</div>"

print "</filedset>"
print "</div>"

img_original = 'no'
img_recorte = 'no'
img_filtro = 'no'
img_proceso = 'no'
img_antesYdesp = 'no'
img_viento = 'no'
img_original2 = 'no'
img_recorte2 = 'no'
img_filtro2 = 'no'

try:
    img_original = form_input["img_original"].value
except KeyError:
    pass
try:
    img_recorte = form_input["img_recorte"].value
except KeyError:
    pass
try:
    img_filtro = form_input["img_filtro"].value
except KeyError:
    pass
try:
    img_original2 = form_input["img_original2"].value
except KeyError:
    pass
try:
    img_recorte2 = form_input["img_recorte2"].value
except KeyError:
    pass
try:
    img_filtro2 = form_input["img_filtro2"].value
except KeyError:
    pass
try:
    img_proceso = form_input["img_proceso"].value
except KeyError:
    pass
try:
    img_antesYdesp = form_input["img_antesYdesp"].value
except KeyError:
    pass
try:
    img_viento = form_input["img_viento"].value
except KeyError:
    pass

if img_original == "si":
    plotAscat(
        obsTotales,
        'ro',
        3,
        'Observaciones totales',
        'Ubicacion de las observaciones en el recorrido del archivo original',
        bloquear=True)
if img_original2 == "si_viento":
    plotWinds(obsTotales, "Intensidad del viento \n Archivo Original ", bloquear=True)

if img_recorte == "si":
    plotAscat(
        obsSubSet,
        'ro',
        3,
        'Obeservaciones dentro del area seleccionada',
        'Posicion de las observaciones incluidas dentro del area geografica selecionada',
        latMin,
        latMax,
        lonMin,
        lonMax,
        bloquear=True)

if img_recorte2 == "si_viento":
    plotWinds(
        obsSubSet,
        "Intensidad y direcion del viento segun sus componentes U y V \n Archivo Recortado",
        latMin,
        latMax,
        lonMin,
        lonMax,
        bloquear=True)

if img_filtro == "si":
    plotAscat(
        coordPlot,
        'ro',
        3,
        'Observaciones de calidad',
        'Ubicaciones de las observaciones con calidad suficeinte para ser procesadas',
        latMin,
        latMax,
        lonMin,
        lonMax,
        bloquear=True)
if img_filtro2 == "si_viento":
    plotWinds(
        coordPlot,
        "Intensidad y direcion del viento segun sus componentes U y V \n Observaciones de calidad ",
        latMin,
        latMax,
        lonMin,
        lonMax,
        bloquear=True)

if img_proceso == "si":
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
        bloquear=True,
	soloContar=True)
if img_antesYdesp == "si":
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
        1,
        bloquear=True)
if img_viento == "si":
    plotWinds(
        resultado,
        "Intensidad y direcion del viento segun sus componentes U y V \n Resultado del Proceso",
        latMin,
        latMax,
        lonMin,
        lonMax,
        bloquear=True)
print """
</br>
</fieldset>
</div>
</br>

"""
