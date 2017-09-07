#!/bin/bash


############################## 1 DESTINO ###################################
if [ 1 -ge $# ] ; then
   echo "falta algun paramétro: uso get-podaac.sh yyyy mm dd"
   exit 1
fi

year=$1
month=$2
day=$3
guion="-"
pass="/n"
user=anonymous



numeroDeDia=`cat <<EOF | python -
import sys
from datetime import datetime, timedelta

yyyy=int("$year")
mm=int("$month")
d=int("$day")

fecha=datetime(yyyy,mm,d)

print (fecha.strftime("%j") )

EOF`


#source ~/work/scripts/config.inc.sh
cd DiasAscat

mkdir archivosASCAT$year$guion$month$guion$day
#cd data/metop_a
cd archivosASCAT$year$guion$month$guion$day


echo /$year/$numeroDeDia

ftp -n -vi podaac-ftp.jpl.nasa.gov << EOF_1
  user $user $pass
  cd /allData/ascat/preview/L2/metop_a/25km/$year/$numeroDeDia
  hash
  bin
  mget *.nc.gz
  close
  bye
EOF_1

gzip -d *

#CDIR=`pwd`

#<<EOF_2 | python -
    #from unificarDia inport *
    #unificarDia($CDIR)
#EOF_2
echo "=============================================================================="
echo "Se han descargado los archivos correspondientes al día indicado."
echo "Puede encontrarlos en la carpeta archivosASCAT$year$guion$month$guion$day"
echo "=============================================================================="

#dir = pwd


#return  $dir




