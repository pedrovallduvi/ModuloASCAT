#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Tkinter
import cgi
import tkFileDialog

from unificarDia import generearFranjaNC

print "Content-type: text/html"
print ""

print """<script type="text/javascript">
function imagen(){
imagen = '<img src="/images/loader.gif" alt="cargando..." />'
	document.getElementById('imagencargando').innerHTML = imagen;
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

print "<div id=marco>"
print "<fieldset>"
print "<legend> <h2> Preparación de los datos</h2> </legend>"
print "</br>"
print "<div id=listo>"

form_input = cgi.FieldStorage()

hora_inicio = form_input["hora_inicial"].value
hora_fin = form_input["hora_final"].value

startRed = "\033[91m"
end = "\033[0;0m"
habilitar = 'si'
root = Tkinter.Tk()  # esto se hace solo para eliminar la ventanita de Tkinter
root.withdraw()  # ahora se cierra
# file_path = tkFileDialog.askopenfilename()
dir_path = tkFileDialog.askdirectory()  # esta linea me devuelve el directorio

if len(dir_path) == 0 or (hora_inicio >= hora_fin):
    nombreArchivo = "<FONT COLOR='red'> Verifique los datos seleccionados, no son correctos. <a href='/cgi-bin/portalAscat.py'> Click Aquí </a> </FONT>"
    habilitar = 'no'
    dir_path = "archivosASCAT1990-01-01"

if habilitar == 'si':
    nombreArchivo = dir_path[(dir_path.index('T') + 1):(len(dir_path))]

print "<h2><big><u> Dia a procesar: ", nombreArchivo, "</u></big></h2>"
print "<h2><big><u> Entre las ", hora_inicio, " y las ", hora_fin, " horas. ", "</u></big></h2>"
print "</div>"
print "<div id=listo>"
print "</div>"
print """ <form action="/cgi-bin/procesar.py" method="post" target="_self" enctype="multipart/form-data">"""

print "<FONT COLOR='white'>"
if habilitar == 'si':
    generearFranjaNC(dir_path, int(hora_inicio), int(hora_fin), "archivoTemporal.nc")
print "</FONT>"  # hace print d eun 0 q no encuetro. Temporalm/ lo oculto asi.

print """<div class='box-gray2'><h3><u><big> Seleccione la técnica con la que desea procesar los datos: </big></u><h3><p></p>
<a onclick="return blmostrocult(this);" style="cursor: hand; cursor: pointer;">  <p>Informacion</p></a><div style="display: none;">
<p><h5> El fin de ambas técnicas es reducir la cantidad total de observaciones y reducir la correlación existente entre las mismas. Lo logra "unificando" las observaciones ubicadas lo suficientemente cerca.</br>
La técnica "superobbing" realiza múltiples promedios sobre los datos. En vez de tomar muchos datos en un área chica, se promedian todos esos datos, obteniendo como resultado una única observación, pero mas representativa. </br>
"Thining", por su parte, selecciona la observación central del area y descartando todas las demás. Las observaciones resultantes son un poco menos precisas pero el procesamiento de la información es mas veloz.</h5> </p>
</div>

	<input type="radio" name="tecnica" value='SO' checked> SuperObbing &nbsp &nbsp
	<input type="radio" name="tecnica" value='T'> Thining
	</div>
	<input type="hidden" name="dir_path" value=""", dir_path, """/>
	</br>
	<div class='box-gray2'>
	<h3><u><big>Indique el tamaño del área sobre la cual se consideran cercanas las observaciones (ej: 0.30): </big></u><h3> <p></p>
<a onclick="return blmostrocult(this);" style="cursor: hand; cursor: pointer;">  <p>Información</p></a><div style="display: none;">
<p><h5> De este valor depende fundamentalmente el procesamiento de los datos. </br> Indica la amplitud del área sobre la cual se consideraran cercanas las observaciones. Es decir, dada una observación se hallan todas aquellas que estén ubicadas geográficamente dentro del área generada por la suma y resta del valor ingresado a la latitud y la longitud. Sobre el conjunto de datos incluidos en esta área, se aplicara la técnica seleccionada anteriormente.</br>
Esta directamente relacionado a la tiempo que se demora en obtener los resultados. Mientras mayor sea la amplitud de área, mas rápido sera el proceso. Áreas demasiados grandes resultaran en observaciones poco precisas, áreas demasiado pequeñas no lograran el objetivo de las técnicas de procesamiento. </br>
La unidad del parámetro es: Grados.
Se sugiere el valor de 0.30 grados ya que con este se obtienen resultados equilibrados. </h5> </p>
</div>
	Radio de cercanía geográfico, grados: <input type="number" step="0.01" name="step" value ="0.30" min="0" style="width:67px;height:19px">
	</div></br>
	<div class='box-gray2'>
	<h3><u><big>  Indique el margen de tiempo aceptable para que se consideren cercanas las observaciones:  </u></big><h3><p></p>
<a onclick="return blmostrocult(this);" style="cursor: hand; cursor: pointer;">  <p>Información</p></a><div style="display: none;">
<p><h5> Además de encontrase suficientemente cerca desde el punto de vista geográfico, para poder procesar las observaciones, estas deben haberse tomado aproximadamente en el mismo momento. Ya que la información puede ser completamente diferente en distintos momentos del día.</br> Dada una observación, además de tener en cuenta el área de proximidad, se seleccionan como cercas aquellas donde el momento en que se han tomado se encuentra en un rango de +- los segundos indicados. </br>
Este parámetro es aun mas visual al procesar la información según rangos horarios. </h5> </p>
</div>
	Radio de cercanía temporal, segundos: <input type="number" name="radioHorario" value ="60" min="0" style="width:67px;height:19px">
         </div>

	</br>
	<div class='box-gray2'>
	<h3><u><big> Seleccione área geográfica que se desea procesar: </big></u><h3><p></p>
<a onclick="return blmostrocult(this);" style="cursor: hand; cursor: pointer;">  <p>Información</p></a><div style="display: none;">
<p><h5>Se deben indicar los limites geográficos a procesar. Luego de ingresar los parámetros puede pulsar el botón "Chekear area ingresada", ubicado en el extremo inferior derecho de la pantalla. Este le mostrara el mapa del área seleccionada.</br>
 Latitud mínima posible: -90 grados. Latitud máxima posible: 90 grados </br>
Longitud mínima posible: 0 grados. Longitud máxima posible: 360 grados </br>
Seleccionar el área especifica a procesar optimizara el tiempo de procesamiento y el tamaño de los archivos de salida; ya que se descartaran todos aquellos datos que excedan los limites indicados.
</h5> </p>
</div>

	Latitud Mínima (de -90 a 90): <input type="number" name="latMin" id="latMin" min="-90" max="90" value=-90.0 min="-90" max"90"/> &nbsp &nbsp
	Latitud Máxima (de -90 a 90): <input type="number" name="latMax" id="latMax" min="-90" max="90" value=0.0  /> &nbsp
	</br>
	Longitud Mínima (de 0 a 360): <input type="number" name="lonMin" id="lonMin" min="0" max="360" value=220.0 />  &nbsp &nbsp
	Longitud Máxima (de 0 a 360): <input type="number" name="lonMax" id="lonMax" min="0" max="360" value=360.0 /> &nbsp
	</div> """

print "</br>"
print "<div class='box-gray2'>"
print """
	<h3><big><u> Seleccione los gráficos que desea generar: </big></u><h3><p></p>
<a onclick="return blmostrocult(this);" style="cursor: hand; cursor: pointer;">  <p>Información</p></a><div style="display: none;">
<p><h5>Se presentan dos tipos de gráficos. Aquellos que presentan la ubicación geográfica de cada observación, sin tomar en cuenta sus componentes de vientos. Y aquellos que muestran la velocidad y dirección del viento, según las mediciones del archivo procesado.</br>
La velocidad del viento esta expresada en km/h y se representa según una barra de colores incluida en el mismo gráfico. </br>
La dirección, por su parte, es representada por flechas. Cada observación incluida en estos gráficos es una flecha que apunta hacia donde corría el viento. El tamaño de la flecha depende de la conglomeración de observaciones. Es decir, que dependiendo de el radio de cercanía geográfico que usted haya ingresado vera flechas mas o menos grandes. Recuerde que puede hacer zoom para verlas con mayor claridad.</br>
El instrumento ASCAT no incluye componentes de velocidad y dirección en todas sus observaciones. Ya que no es capaz de obtener la información en algunas ocasiones (Condiciones naturales adversas o superficies no oceánicas).
</h5> </p>
</div>
</h3><div id=cheks >
<h3>	<input type="checkbox" name="img_original" value="si" /> Ubicaciones de las observaciones en el recorrido del archivo original  <br />
         <input type="checkbox" name="img_original2" value="si_viento" /> Intensidad del viento en el archivo original  <br />
<p></p>
        	<input type="checkbox" name="img_recorte" value="si" /> Ubicación de las observaciones en el área geográfica seleccionada <br />
        	<input type="checkbox" name="img_recorte2" value="si_viento" /> Componentes del viento en el área geográfica seleccionada  <br />
<p></p>
	<input type="checkbox" name="img_filtro" value="si" /> Ubicaciones de las observaciones restantes luego de filtrar por calidad  <br />
         <input type="checkbox" name="img_filtro2" value="si_viento" /> Componentes del viento en las observaciones de calidad  <br />
<p></p>
	<input type="checkbox" name="img_proceso" value="si" /> Ubicación de las observaciones resultantes luego de aplicar SuperObbing / Thining <br />
<p></p>
	<input type="checkbox" name="img_antesYdesp" value="si" /> Comparación entre las ubicaciones de las observaciones antes y después de aplicar la técnica seleccionada<br/>
<p></p>
	<input type="checkbox" name="img_viento" value="si" /> Velocidad y dirección del viento en las observaciones procesadas  <br />
 <h3>
</div>
</div>"""

if habilitar == 'si':
    print """
	</br>
	<input class="btn" type="submit" value="Procesar" onclick='imagen()'/>
	<div id='imagencargando'></div>
	</form> """
else:
    print """
	</br>
	<input class="btn" type="submit" value="Procesar" disabled="true"/>
	<div id='imagencargando'></div>
	</form> """

print """
	<form target="_blank" action="/cgi-bin/mostrarArea.py" >

	<input type="hidden" name="latMin2" id="latMin2" min="-90" max="90"  min="-90" max"90"/>
	<input type="hidden" name="latMax2" id="latMax2" min="-90" max="90"  />
	<input type="hidden" name="lonMin2" id="lonMin2" min="0" max="360" />
	<input type="hidden" name="lonMax2" id="lonMax2" min="0" max="360"  />
	<p> </p>

<input class="btn2" type="submit" value="Chekear area ingresada" onclick="copy_address()">
</form>
"""
print "</br>"
print "</fieldset>"
print "</div>"
print "</div>"
print "</body>"
print "</html>"
