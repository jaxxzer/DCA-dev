import math
import matplotlib.pyplot as plt

fig = plt.figure()

#sample_indices = [185, 239, 301, 416, 531, 636, 788, 969, 1151, 1297, 1479, 1715, 1952, 2161, 2440, 2780, 3121, 2262, 3646, 4020, 4394]

infile = open("samples.txt", "r")

lines = infile.readlines()
infile.close()

sample_indices = []
sample_radii = []

for line in lines:
    index, radius = line.split('\t')
    sample_indices.append(int(index))
    sample_radii.append(float(radius))

pi = 3.141592

starting_quadrant = 0;

current_quadrant = starting_quadrant;
current_index = sample_indices[0]

outfile = open("output.csv", "w")

for i in range(1,len(sample_indices)):
   radius_0 = sample_radii[i-1]
   radius_1 = sample_radii[i]
   
   angle_base = current_quadrant * pi/2
   current_quadrant = (current_quadrant + 1)%4

   num_between = sample_indices[i] - sample_indices[i-1]

   for idx in range(0, num_between):
        print current_index
        current_index = current_index + 1
        current_angle = angle_base + idx*math.pi/2/num_between
        current_radius = radius_0 + idx*(radius_1 - radius_0)/num_between

        x,y = current_radius*math.cos(current_angle), current_radius*math.sin(current_angle)
        outfile.write(str(current_index) + ',' + str(x) + ',' + str(y) + '\n')
        plt.scatter(x, y)

outfile.close()

while True:
    plt.pause(0.05)
	

	
