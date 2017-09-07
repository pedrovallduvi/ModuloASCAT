#!/usr/bin/env python
# -*- coding: utf-8 -*-

print "Content-type: text/html"
print ""

print """<script type="text/javascript">
function imagen(){
imagen = '<img src="/images/loader.gif" alt="cargando..." />'
	document.getElementById('imagencargando').innerHTML = imagen;
}
</script>"""
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
</br>

<div class="box-gray">
<p>Esta aplicación fue desarrollada en el marco del proyecto final de la carrera Lic. en Sistemas de Información.
A su vez forma parte de las actividades previstas en el PIDDEF 1614.  Proyecto de Investigación y Desarrollo del  Ministerio de Defensa, titulado “Sistema de asimilación de datos y pronóstico por ensambles en alta resolución para el alerta de fenómenos severos”. </p>
<p>Usted podrá descargar automáticamente los archivos generados por el satélite metop-a. Ubicándolos en carpetas individuales diarias, con los archivos correspondientes descomprimidos y un archivo adicional donde se unifican los anteriores.</br>
Podrá procesar cada uno de estos en forma individual, o según un rango horario. Lo hará de forma totalmente parametrizable, intuitiva y sencilla. </p>
<p> Grupo de Investigación en Ciencias Atmosféricas. Muchas gracias. </p>

</div>

<div id=marco>
<fieldset>
<legend> <h2> Descargar archivos ASCAT via FTP </h2></legend>
<a onclick="return blmostrocult(this);" style="cursor: hand; cursor: pointer;">  <p>Información</p></a><div style="display: none;">
<p> Este modulo permite la descarga automatizada de los archivos ASCAT publicados por PO.DAAC (Physical Oceanography Distributed Active Archive Center). Diariamente PO.DAAC publica la información obtenida por el instrumento ASCAT. Son 14 archivos de datos, de aproximadmente 2 MB cada uno luego de ser descomprimidos y junto con 14 pequeños archivos de control. Pueden ser descargados en forma manual desde: ftp://podaac-ftp.jpl.nasa.gov/allData/ascat/preview/L2/metop_a/25km/ </br>
Por cada día descargado, automáticamente se creara una nueva carpeta dentro del directorio '/DiasAscat'. El nombre de esta carpeta sera: '/archivosASCATYYYY-MM-DD'. Tamaño aproximado: 55 MB.  Dentro de la misma encontrara únicamente los archivos de datos. Descomprimidos y listos para ser procesados. Vera también un archivo extra, el cual unifica los anteriores. </br>
Asegúrese de ingresar fechas validas.
</p>
</div>
<div class="box-gray">
<h3> Descargar archivos de un día completo </3>
<form action="/cgi-bin/descarga.py" method="post">
	Dia: <select name="dia" type="text">
	<option>01</option>
	<option>02</option>
	<option>03</option>
	<option>04</option>
	<option>05</option>
	<option>06</option>
	<option>07</option>
	<option>08</option>
	<option>09</option>
	<option>10</option>
	<option>11</option>
	<option>12</option>
	<option>13</option>
	<option>14</option>
	<option>15</option>
	<option>16</option>
	<option>17</option>
	<option>18</option>
	<option>19</option>
	<option>20</option>
	<option>21</option>
	<option>22</option>
	<option>23</option>
	<option>24</option>
	<option>25</option>
	<option>26</option>
	<option>27</option>
	<option>28</option>
	<option>29</option>
	<option>30</option>
	<option>31</option>
	</select>

	&nbsp; &nbsp; Mes: <select type="text" name="mes" />
	<option>01</option>
	<option>02</option>
	<option>03</option>
	<option>04</option>
	<option>05</option>
	<option>06</option>
	<option>07</option>
	<option>08</option>
	<option>09</option>
	<option>10</option>
	<option>11</option>
	<option>12</option>
</select>
	&nbsp;&nbsp; Año: <select type="text" name="ano">
	<option>2009</option>
	<option>2010</option>
	<option>2009</option>
	<option>2010</option>
	<option>2011</option>
	<option>2012</option>
	<option>2013</option>
	<option>2014</option>
	<option>2015</option>
	<option>2016</option>
	<option>2017</option>
</select>
	</br>
	<input class="btn4" type="submit" value="Descargar Dia" onclick='imagen()'/>
	</form>
</div>
<p></p>

<div class="box-gray">
<h3> Descargar archivos de un rango de fechas </3>
	<form action="/cgi-bin/descargaRango.py" method="post">
	Desde el Día: <select name="diainicial" type="text" />
	<option>01</option>
	<option>02</option>
	<option>03</option>
	<option>04</option>
	<option>05</option>
	<option>06</option>
	<option>07</option>
	<option>08</option>
	<option>09</option>
	<option>10</option>
	<option>11</option>
	<option>12</option>
	<option>13</option>
	<option>14</option>
	<option>15</option>
	<option>16</option>
	<option>17</option>
	<option>18</option>
	<option>19</option>
	<option>20</option>
	<option>21</option>
	<option>22</option>
	<option>23</option>
	<option>24</option>
	<option>25</option>
	<option>26</option>
	<option>27</option>
	<option>28</option>
	<option>29</option>
	<option>30</option>
	<option>31</option>
	</select>

	&nbsp; &nbsp; Hasta el Día: <select name="diafinal" type="text" />
	<option>01</option>
	<option>02</option>
	<option>03</option>
	<option>04</option>
	<option>05</option>
	<option>06</option>
	<option>07</option>
	<option>08</option>
	<option>09</option>
	<option>10</option>
	<option>11</option>
	<option>12</option>
	<option>13</option>
	<option>14</option>
	<option>15</option>
	<option>16</option>
	<option>17</option>
	<option>18</option>
	<option>19</option>
	<option>20</option>
	<option>21</option>
	<option>22</option>
	<option>23</option>
	<option>24</option>
	<option>25</option>
	<option>26</option>
	<option>27</option>
	<option>28</option>
	<option>29</option>
	<option>30</option>
	<option>31</option>
	</select>


	&nbsp; &nbsp; Del Mes : <select type="text" name="mes" />
	<option>01</option>
	<option>02</option>
	<option>03</option>
	<option>04</option>
	<option>05</option>
	<option>06</option>
	<option>07</option>
	<option>08</option>
	<option>09</option>
	<option>10</option>
	<option>11</option>
	<option>12</option>
</select>
	&nbsp;&nbsp; Del Año: <select type="text" name="ano" />
	<option>2009</option>
	<option>2010</option>
	<option>2009</option>
	<option>2010</option>
	<option>2011</option>
	<option>2012</option>
	<option>2013</option>
	<option>2014</option>
	<option>2015</option>
	<option>2016</option>
	<option>2017</option>
</select>
	</br>  <p></p>
	<input class="btn4" type="submit" value="Descargar Periodo" onclick='imagen()'/>
	</form>
</div>
<div id=listo>
<h3>
<div id='imagencargando'></div>
</h3></div>
</br>
</fieldset>
</br>
</div>

<div id=marco>
<fieldset>

<legend> <h2> Procesar un archivo especifico </h2></legend>
<a onclick="return blmostrocult(this);" style="cursor: hand; cursor: pointer;">  <p>Información</p></a><div style="display: none;">
<p> Desde aquí podrá seleccionar el archivo ASCAT, previamente descargado, que desea procesar.
 Al pulsar 'Procesar archivo' se desplegará una ventana que le permitirá seleccionar el mismo y luego presentará el menú de opciones de parametrización. Los archivos descargados por este sistema se encuentran dentro de '/DiasAscat/archivosASCATYYYY-MM-DD''. El archivo original no se vera afectado por le procesamiento del mismo. La convención los nombres de estos archivos es la siguiente:
ascat_YYYYMMDD_HHMMSS_SAT_ORBIT_SRV_T_SMPL_VERS(_CONT).l2.nc (Más información en la documentación).  </p>
</div>
<div class="box-gray">
    <h3> Haciendo click en 'Procesar Archivo' podrá seleccionar uno de los archivos ASCAT descargados y proceder al ingreso de parámetros:  </3>
         <form action="/cgi-bin/asignarTecnica.py">
	<input class="btn4" type="submit" value="Procesar archivo">
	</form>
</div>
</br>
</fieldset>
</div>
</br>

<div id=marco>
<fieldset>
<legend><h2>Seleccionar rango horario a procesar </h2></legend>
<a onclick="return blmostrocult(this);" style="cursor: hand; cursor: pointer;">  <p>Información</p></a><div style="display: none;">
<p>Para procesar las observaciones obtenidas en un rango horario especifico de un día, antes usted debió haber descargado ese día completo con este mismo software.
Seleccione hora de inicio y hora de fin y luego, al pulsar el botón de acceso, se desplegará la ventada desde la cual podrá seleccionar el directorio con los archivos del día ('/DiasAscat/archivosASCATYYYY-MM-DD'). Asegúrese de ingresar dentro de la carpeta antes de confirmar pulsando 'Ok'. Entonces se presentara el menú de opciones de parametrización. </p>
</div>
<div class="box-gray">
    <h3> Primero elija el rango horario sobre el cual se seleccionara la información, luego pulsando en 'Procesar Rango Horario' podrá seleccionar uno de los directorios ASCAT descargados y proceder al ingreso de parámetros:  </3>

        <form action="/cgi-bin/tecnicaRango.py" method="post">
	Hora Inicial:  <select type="text" name="hora_inicial" />

	<option>00</option>
	<option>01</option>
	<option>02</option>
	<option>03</option>
	<option>04</option>
	<option>05</option>
	<option>06</option>
	<option>07</option>
	<option>08</option>
	<option>09</option>
	<option>10</option>
	<option>11</option>
	<option>12</option>
	<option>13</option>
	<option>14</option>
	<option>15</option>
	<option>16</option>
	<option>17</option>
	<option>18</option>
	<option>19</option>
	<option>20</option>
	<option>21</option>
	<option>22</option>
	<option>23</option>
	</select>

	&nbsp; &nbsp; Hora Final: <select type="text" name="hora_final" />

	<option>01</option>
	<option>02</option>
	<option>03</option>
	<option>04</option>
	<option>05</option>
	<option>06</option>
	<option>07</option>
	<option>08</option>
	<option>09</option>
	<option>10</option>
	<option>11</option>
	<option>12</option>
	<option>13</option>
	<option>14</option>
	<option>15</option>
	<option>16</option>
	<option>17</option>
	<option>18</option>
	<option>19</option>
	<option>20</option>
	<option>21</option>
	<option>22</option>
	<option>23</option>
	<option>24</option>
	</select>

	<input class="btn4" type="submit" value="Procesar rango horario" />
	</form>
</div>
</br>
</fieldset>
</div>"""

print "</br>"
print "</body>"
print "</html>"
