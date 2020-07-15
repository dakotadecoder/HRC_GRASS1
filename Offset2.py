#!/usr/bin/env python3



import grass.script as gscript



ofs = '+ 1200300000'



list1 = gscript.list_strings('raster')

x = '2_swa_gr78_Win10_4326__1arc_22200c_streams'

b = '2_swa_gr78_Win10_4326__1arc_22200c_basins'

for i in list1 : 

    if x in i:

        def funcc():

            c = i[0:65] + '_ofs'

            gscript.run_command('r.mapcalc', expression = c + '=' + '(' + i + ')/2' + ofs)
            gscript.run_command('r.to.vect', input = c , output = c , type = 'area' , flags = 'v')
            gscript.run_command('r.out.ascii', input = c, output = 'E:\\HRC_Water\\Python\\Test_Outputs' + '\\' + c , flags = 'i')
            gscript.run_command('v.out.ogr' , input = c, output = 'E:\\HRC_Water\\Python\\Test_Outputs' + '\\' + c , format = 'ESRI_shapefile')
        funcc()

    elif b in i: 

        def funcc():

            c = i[0:64] + '_ofs' 

            gscript.run_command('r.mapcalc', expression = c + '=' + '(' + i + ')/2' + ofs)
            gscript.run_command('r.to.vect', input = c , output = c , type = 'area' , flags = 'v')
            gscript.run_command('r.out.ascii', input = c, output = 'E:\\HRC_Water\\Python\\Test_Outputs' + '\\' + c , flags = 'i')
            gscript.run_command('v.out.ogr' , input = c, output = 'E:\\HRC_Water\\Python\\Test_Outputs' + '\\' + c , format = 'ESRI_shapefile')
        funcc()

    else:

        continue

