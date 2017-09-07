#!/usr/bin/env python

"""No esta dentro del alcance de este proyecto el estudio profundo en lo que refiere
a la codificacion, decodificacion y procesamiento de archivos de fromato bufr.
Para escribir este programa, que a su vez genera el archivo requerido, se sigueron
los tutoriales disponibles en:
    http://www.dtcenter.org/com-GSI/BUFR/docs/users_guide/BUFR_PrepBUFR_User_Guide_v1.pdf
    http://www.nco.ncep.noaa.gov/sib/decoders/BUFRLIB/toc/
    http://www.dtcenter.org/com-GSI/BUFR/tutorial/index.php

    Librerias Requeridas:
    http://www.dtcenter.org/met/users/support/online_tutorial/METv2.0/compilation/req_libs.php
"""

def escribirFortranBurf(nombreArchivo, obs):
    nombreArchivo = nombreArchivo.replace("/DiasAscat/", "")
    nombreArchivo = 'procesado-' + str(nombreArchivo)
    archi = open('encode_ASCAT' + '.f90', 'w')
    archi.close()
    archi = open('encode_ASCAT' + '.f90', 'a')
    archi.write("""program bufr_encode
!
! writing one value into a bufr file
!
 implicit none
 integer, parameter :: mxmn=35, mxlv=200
 character(80):: hdstr='XOB YOB DHR ' ! SQM | 011217 | WIND SPEED (SOB) (QUALITY) MARKER  !  DHR OBSERVATION TIME   					    !  WOE WIND OBSERVATION ERROR (RMS)
 character(80):: obstr='UOB VOB WOE SQM'
! THE FOLLOWING ARE TABLE B ENTRIES FOR THE REPORT HEADER: XOB YOB DHR
! THE FOLLOWING ARE TABLE B ENTRIES FOR THE REPORT LEVEL DATA : WOE UOB VOB SQM
 !real(8) :: hdr(3),obs(4,4)
 real(8) :: hdr(mxmn),obs(mxmn,mxlv)

 character(8) subset
 integer :: unit_out=10,unit_table=20,nlvl
 integer :: idate,iret

 open(unit_table,file='prepobs_prep_app.bufrtable')
 open(unit_out,file='""" + nombreArchivo + """.bufr',action='write' &
               ,form='unformatted')
 call datelen(10)
 call openbf(unit_out,'OUT',unit_table)

! set header values
   !idate=fecha  ! YYYYMMDDHH
   subset='ASCATW'   ! ASCAT reports
   call openmb(unit_out,subset,idate)

! set data values

""")  # ver como modificar idate   """+str(obs[i][])+"""
    for i in range(len(obs) - 1):
        archi.write("""
      hdr(1)=""" + str(obs[i][0]) + """;hdr(2)=""" + str(obs[i][1]) + """;hdr(3)=""" + str(obs[i][2]) + """
      obs(1,1)=""" + str(obs[i][3]) + """; obs(2,1)=""" + str(obs[i][4]) + """; obs(3,1)=2; obs(4,1)= 0
      nlvl=""" + str(i) + """
! encode
      call ufbint(unit_out,hdr,mxmn,1,iret,hdstr)
      call ufbint(unit_out,obs,mxmn,1,iret,obstr)
      call writsb(unit_out)
""")
    archi.write("""       """)
    archi.write("""   call closmg(unit_out)
 call closbf(unit_out)
end program""")
