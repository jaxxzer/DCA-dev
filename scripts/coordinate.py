import math
import matplotlib.pyplot as plt
from optparse import OptionParser

parser = OptionParser()
parser.add_option("--in", dest="infile", help="Input file, tab separated: <index radius>")
parser.add_option("--out", dest="outfile", default="Spiral.csv", help="Output csv file: <index, x, y>")
parser.add_option("--scalar", dest="scalar", type="float", default=1.0, help="Arbitrary scalar applied to output coordinates")
parser.add_option("--start-ordinate", dest="start_ordinate", type="int", default=0, help="ordinate of first point, 0,1,2,3 = +x,+y,-x,-y")
parser.add_option("--reverse", dest="reverse", default=False, action="store_true", help="spiral clockwise")
parser.add_option("--noplot", dest="noplot", default=False, action="store_true", help="skip plot output for faster processing")
(options,args) = parser.parse_args()


fig = plt.figure()

infile = open("samples.txt", "r")

lines = infile.readlines()
infile.close()

sample_indices = []
sample_radii = []

for line in lines:
    index, radius = line.split('\t')
    sample_indices.append(int(index))
    sample_radii.append(float(radius))

current_ordinate = options.start_ordinate

current_index = sample_indices[0]

outfile = open("output.csv", "w")

for i in range(1,len(sample_indices)):
   radius_0 = sample_radii[i-1]
   radius_1 = sample_radii[i]
   
   angle_base = current_ordinate * math.pi/2
   if options.reverse:
       current_ordinate = (current_ordinate - 1)%4
   else:
       current_ordinate = (current_ordinate + 1)%4

   num_between = sample_indices[i] - sample_indices[i-1]

   for idx in range(0, num_between):
        print current_index
        

        if options.reverse:
            current_angle = angle_base - idx*math.pi/2/num_between
        else:
            current_angle = angle_base + idx*math.pi/2/num_between

        current_radius = radius_0 + idx*(radius_1 - radius_0)/num_between
        x,y = options.scalar*current_radius*math.cos(current_angle), options.scalar*current_radius*math.sin(current_angle)
        outfile.write(str(current_index) + ',' + str(x) + ',' + str(y) + '\n')

        if not options.noplot:
            plt.scatter(x, y)

        current_index = current_index + 1

outfile.close()

while not options.noplot:
    plt.pause(0.05)
	

	
