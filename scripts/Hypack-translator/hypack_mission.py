# python hypack .lnw file to Mavproxy mission file converter
# Jacob Walser September 2016

from optparse import OptionParser

import pyproj

wgs84 = pyproj.Proj("+init=EPSG:4326")
fl_east_ft = pyproj.Proj("+init=EPSG:6438")

parser = OptionParser()
parser.add_option("--in", dest="in_file", help="Input .lnw file")
parser.add_option("--out", dest="out_file", default="mission.wp", help="Output .wp file (mission.wp by default)")
parser.add_option("--depth", dest="depth", default=-0.25, help="depth of all waypoints")
parser.add_option("--alt-frame", dest="alt-frame", default=0, help="alt frame, 0=relative, 3=above terrain")
parser.add_option("--delay", dest="delay", default=1.0, help="time to wait at each waypoint before proceeding with mission")
parser.add_option("--noflip", dest="flip", action="store_false", default=True, help="disable automatically flipping every other waypoint for proper navigation behavior")
parser.add_option("--reverse", dest="reverse", action="store_true", default=False, help="Reverse waypoint order")
(options,args) = parser.parse_args()

in_file = open(options.in_file, "r")
out_file = open(options.out_file, "w")

# header
out_file.write("QGC WPL 110\n")

# file out = open(output, w)
lines = in_file.readlines()

count = 0
wps = []

for line in lines:

    first_space = line.find(' ')
    second_space = line[first_space + 1:].find(' ') + first_space + 1

    if line[:first_space] == 'PTS':
        print '#',
        easting = float(line[first_space+1:second_space]) * 0.3048006096
        northing = float(line[second_space:]) * 0.3048006096
        lat, lng = pyproj.transform(fl_east_ft, wgs84, easting, northing)
        if(options.reverse):
            wps.insert(0, (lat,lng))
        else:
            wps.append((lat,lng))
	'''
        if count == 0:
            out_file.write(str(count) + '\t0\t0\t16\t0.000000\t0.000000\t0.000000\t0.000000\t' + str(lng) + '\t' + str(lat) + '\t25.000000\t1\n')
        else :
        '''
	
        # out_file.write(str(count) + '\t0\t3\t16\t'+str(options.delay)+'\t0.000000\t0.000000\t0.000000\t' + str(lng) + '\t' + str(lat) + '\t'+str(options.depth)+'\t1\n')
        
        count = count + 1


if options.flip:
    for i in range(len(wps)/4):
        # 2, 6, 10...
        idx = i*4 + 2
        temp = wps[idx]
        wps[idx] = wps[idx+1]
        wps[idx+1] = temp

count = 0
out_file.write('0\t0\t0\t16\t'+str(options.delay)+'\t0.000000\t0.000000\t0.000000\t' + str(wps[0][1]) + '\t' + str(wps[0][0]) + '\t'+str(options.depth)+'\t1\n')
for wp in wps:
    print count
    out_file.write(str(count+1) + '\t0\t0\t16\t'+str(options.delay)+'\t0.000000\t0.000000\t0.000000\t' + str(wp[1]) + '\t' + str(wp[0]) + '\t'+str(options.depth)+'\t1\n')
    count = count + 1  

print
print str(count) + ' waypoints exported to ' + options.out_file
print wps
in_file.close()
out_file.close()
print 'Done.'





