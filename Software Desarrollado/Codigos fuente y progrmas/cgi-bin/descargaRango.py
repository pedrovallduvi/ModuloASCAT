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

print "</br>"

form_input = cgi.FieldStorage()
ano = form_input["ano"].value
mes = form_input["mes"].value
diaFinal = int(form_input["diafinal"].value)
diaInicial = int(form_input["diainicial"].value)
diaInicial = int(diaInicial)

if diaInicial > diaFinal:
    print "<h3><p>Verifique los dias ingresados. EL dia de inicio debe ser menor al dia de fin.</p>"
    print "<h1><a href='/cgi-bin/portalAscat.py'><p>Click aquí para volver al menú principal.</p></a></h1>"
else:
    while diaInicial <= diaFinal:
        fecha = ano + " " + mes + " " + str(diaInicial)
        path = "archivosASCAT" + ano + "-" + mes + "-" + str(diaInicial)
        carpeta = str(os.getcwd()) + "/DiasAscat/" + path
        if (os.path.exists(carpeta)):
            print "<h3><p>Ya existe un directorio con archivos para la fecha", diaInicial, "/", mes, "/", ano, " . Por favor, controle dentro de la carpeta DiasAscat.</p> <p> Si desea volver a descargar el dia, primero debe eliminar la carpeta existente.</p></h3>"
            diaInicial += 1
        else:
	    print "<font color ='ffffff'>"
            os.system('sh descargar-podaac.sh ' + fecha)
            os.system('cd ' + path)
            path_dir = str(os.getcwd()) + "/DiasAscat/" + path
            unificarDia(path_dir)
            os.system('cd ..')
	    print "</font>"
            # os.system('python main.py')
	    print "<h5><p> Nueva Carpeta de archivos ASCAT: <u>ArchivosASCAT"+ano+"-"+str(mes)+"-"+str(diaInicial)+"</u></p></h5>" 

            diaInicial += 1
	   
	    
    print "<h3><p>Gracias por esperar. Se han descargado los archivos solicitados.</p></h3>"
    print "<h3><p>Se han creado las nuevas carpetas dentro del directorio 'DiasAscat'.</p></h3>"
    print "<h3><p>Podra encontrar los archivos NetCdf correspondietnes dentro de las misma.</p></h3>"
print "</br>"
print "<h1><a href='/cgi-bin/portalAscat.py'><p>Click aquí para volver al menú principal.</p></a></h1>"
print "</p>"
print "</br>"
print "</fieldset>"
print "</div>"

print "</body>"
print "</html>"
