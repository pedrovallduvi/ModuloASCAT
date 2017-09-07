#!/bin/bash

cd $ModuloAscat
nombre=$1
tecnica=$2
step=$3
latMin=$4
latMax=$5
lonMin=$6
lonMax=$7

python procesarASCAT.py $nombre $tecnica $step $latMin $latMax $lonMin $lonMax

exit

