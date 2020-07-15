#!/usr/bin/env python3

import grass.script as gscript

b = gscript.list_strings('raster')





gscript.run_command('g.region', raster = b)



gscript.run_command('r.patch', input = b , output = 'merged_dem')

