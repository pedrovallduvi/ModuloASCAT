#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cgi

from prepararObs import *

form_input = cgi.FieldStorage()

latMax2 = form_input["latMax2"].value
latMin2 = form_input["latMin2"].value
lonMax2 = form_input["lonMax2"].value
lonMin2 = form_input["lonMin2"].value

latMax = float(latMax2[:])
latMin = float(latMin2[:])
lonMax = float(lonMax2[:])
lonMin = float(lonMin2[:])

plotArea(latMin, latMax, lonMin, lonMax)

print """
<script type="text/javascript">
//<![CDATA[
function cerrar(){
self.close();
}
var cierre = setTimeout('cerrar()', 1);
//]]>
</script>
"""
