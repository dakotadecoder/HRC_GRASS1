#!/usr/bin/env python3

import grass.script as gscript
from time import localtime, strftime
e = 'merged_dem'

#date is 8 characters long (eg 20200707 for 07/07/2020), GRASSver is in the terms gr78 for GRASS 7.8, OS is linux, Windows#, or OSX#, res is usually 1arc
#set the relevant variables to their respective values inside the single quoation marks

date = strftime("%Y%m%d_", localtime())

FFGS = 'CAFFGS' + '_'
Country = 'N' + '_'

Number = '2' + '_'

initials = 'swa' + '_'

GRASSVER = 'gr78' + '_'

OS = 'Win10' + '_'

EPSG = '4326' + '_'

Res = '1arc' + '_'

Thresh = '22200c'



j = 'wshd_' + date + FFGS + Country + Number + initials + GRASSVER + OS + EPSG + '_1arc_22200c'
a = j + '_accum'
d = j + '_aspect'
b = j + '_basins'
s = j + '_streams'





gscript.run_command('r.watershed', elevation = e , threshold = 22200, accumulation = a, drainage = d, basin = b, stream = s, flags='s4' )

