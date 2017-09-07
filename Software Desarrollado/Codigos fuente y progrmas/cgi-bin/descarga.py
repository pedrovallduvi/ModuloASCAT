#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cgi

from unificarDia import *

print "Content-type: text/html"
print ""

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
<h2>Autor: Pedro Vallduvi (pedro.vallduvi@yahoo.com).</h2>
<h2>Trabajo Final Lic. Sistemas de Informacion.</h2>
<h2>Universidad Nacional del Nordeste - Corrientes, Argentina.</h2>
<h2>Facultad de Cs. Exactas, Naturales y Agrimensura.</h2>
</div>
</div>
</br>"""

print "<div id=marco>"
print "<fieldset>"
print "<legend> <h2> Descarga FTP </h2> </legend>"
print "<div id=listo>"
#print "<h1> Listo!</h1>"
print "</div>"
print "</br>"

form_input = cgi.FieldStorage()
ano = form_input["ano"].value
mes = form_input["mes"].value 
dia = int(form_input["dia"].value) #se hace int para eliminar el 0 en casos como 01, 02, etc
fecha = str(ano) + " " + str(mes) + " " + str(dia)
path = "archivosASCAT" + ano + "-" + str(mes) + "-" + str(dia)
carpeta = str(os.getcwd()) + "/DiasAscat/" + path
if (os.path.exists(carpeta)):
    print "<h3><p>Ya existe un directorio con archivos para esta fecha. Por favor, controle dentro de la carpeta DiasAscat.</p> <p> Si desea volver a descargar el dia, primero debe eliminar la carpeta existente.</p></h3>"
else:
    print "<h3><p>Gracias por esperar. Se han descargado los archivos solicitados.</p></h3>"
    print "<h3><p>Se ha creado una nueva carpeta dentro del directorio 'DiasAscat'.</p></h3>"
    print "<h3><p> Nombre de la Carpeta: <u>ArchivosASCAT"+ano+"-"+str(mes)+"-"+str(dia)+"</u></p></h3>" 
    print "<font color ='ffffff'>"
    dia = os.system('sh descargar-podaac.sh ' + fecha)
    os.system('cd ' + path)
    path_dir = str(os.getcwd()) + "/DiasAscat/" + path
    unificarDia(path_dir)
    os.system('cd ..')
    # os.system('python main.py')
    dia = form_input["dia"].value
    print "</font>"
    print "<h3><p>Podra encontrar los archivos NetCdf correspondietnes al dia: ", str(dia), "/", str(mes), "/", ano, "  dentro de la misma.</p></h3>"
print "</br>"
print "<h1><a href='/cgi-bin/portalAscat.py'><p>Click aquí para volver al menú principal.</p></a></h1>"
print "</p>"
print "</br>"
print "</fieldset>"
print "</div>"

print "</body>"
print "</html>"
