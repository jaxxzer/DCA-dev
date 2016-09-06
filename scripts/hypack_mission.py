# python hypack .lnw file to Mavproxy mission file converter
# Jacob Walser September 2016

from optparse import OptionParser

parser = OptionParser()
parser.add_option("--in", dest="in_file", help="Input .lnw file")
parser.add_option("--out", dest="out_file", default="mission.wp", help="Output .wp file (mission.wp by default)")
(options,args) = parser.parse_args()

in_file = open(options.in_file, "r")
out_file = open(options.out_file, "w")

# header
out_file.write("QGC WPL 110\n")

# file out = open(output, w)
lines = in_file.readlines()

count = 0
for line in lines:

    first_space = line.find(' ')
    second_space = line[first_space + 1:].find(' ') + first_space + 1

    if line[:first_space] == 'PTS':
        print '#',
        lat = float(line[first_space+1:second_space]) / 100000
        lng = float(line[second_space:]) / 100000
 
        if count == 0:
            out_file.write(str(count) + '\t0\t0\t16\t0.000000\t0.000000\t0.000000\t0.000000\t' + str(lng) + '\t' + str(lat) + '\t25.000000\t1\n')
        else :
            out_file.write(str(count) + '\t0\t3\t16\t0.000000\t0.000000\t0.000000\t0.000000\t' + str(lng) + '\t' + str(lat) + '\t25.000000\t1\n')
        count = count + 1

print
print str(count) + ' waypoints exported to ' + options.out_file
in_file.close()
out_file.close()
print 'Done.'





