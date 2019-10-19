# Animation Example

import numpy as np
from matplotlib import pyplot as plt    
from matplotlib import animation as anim

def rose_curves(n, d):
	
	k = n/d

	lim = d*2.0*np.pi
	
	theta = np.linspace(0, lim, nlim)
	
	r = scale*np.cos(k*theta)
	
	x = r*np.cos(theta)
	y = r*np.sin(theta)
	
	return x, y

# Data
scale = 5
nlim = 1001
num = 8.0
den = 9.0
xcord, ycord = rose_curves(num, den)
xmin = -5.5
xmax = 5.5
ymin = -5.5
ymax = 5.5

fig = plt.figure() # Create a dummy figure

for i in range(nlim):

	plt.clf()
	# fix to keep the axis steady
	plt.scatter([xmin, xmax, xmin, xmax], [ymin, ymin, ymax, ymax], color='azure')
	# actual animation
	plt.plot(xcord[:i+1], ycord[:i+1], label="rose curve", color="chocolate")
	# tracer point
	plt.scatter(xcord[i], ycord[i], s=20, marker='o', edgecolor='k', color='green')
	# centre point
	plt.scatter([0], [0], s=20, marker='o', edgecolor='k', color='red')
	plt.title(f"Rose curve with k={num/den} Iteration={i} out of {nlim}")
	plt.suptitle("Rose curve animation")
	plt.xlim([xmin, xmax])
	plt.ylim([ymin, ymax])
	plt.axis('equal')
	plt.grid(True)
	plt.pause(0.001)
