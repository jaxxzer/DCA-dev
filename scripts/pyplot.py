import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
fig = plt.figure()
ax = plt.gca()
plt.axis([0,10,0,10])
points = [[2, 1], [8, 1], [8, 4]]
polygon = plt.Polygon(points)
t1 = ax.transData

ax.add_patch(polygon)

for i in range(10):

    t2 = mpl.transforms.Affine2D().rotate_deg_around(2, 1, i*10) + t1
    polygon.set_transform(t2)
    y = np.random.random()
    plt.scatter(i, y)
    plt.pause(0.55)

while True:
    plt.pause(0.05)
