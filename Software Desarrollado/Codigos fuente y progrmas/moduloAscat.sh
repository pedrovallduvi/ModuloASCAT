#!/bin/bash

cd $ModuloAscat

gnome-terminal -x bash -c "echo 'NO cierre esta terminal hasta haber finalizado el uso del modulo.' && python -m CGIHTTPServer" 

gnome-terminal -x bash -c "xdg-open http://localhost:8000/cgi-bin/portalAscat.py & echo 'Presiona enter para cerrar esta terminal. Si experimenta algun tipo de error, pruebe tener abierto su navegador por defecto antes de iniciar el programa.' & read year "

exit 
