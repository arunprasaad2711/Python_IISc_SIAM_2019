'''
Source to read:
https://mathematica.stackexchange.com/questions/100051/dynamic-epicycles
https://www.jstor.org/stable/2691465
'''

import numpy as np
from matplotlib import pyplot as plt    
from matplotlib import animation as anim

n = 1001
a = 0
b = 4.0*np.pi

theta = np.linspace(a, b, n)
x = np.cos(theta) + 0.5*np.cos(7.0*theta) + (1.0/3.0)*np.sin(17.0*theta)
y = np.sin(theta) + 0.5*np.sin(7.0*theta) + (1.0/3.0)*np.cos(17.0*theta)

fig = plt.figure()       		# Create a dummy figure

pts_x = 11
pts_y = 11
xmin = -2
xmax = 2
ymin = -2
ymax = 2

xticks = np.linspace(xmin, xmax, pts_x)
yticks = np.linspace(ymin, ymax, pts_y)

def animate(i):
	plt.clf()
	# fix to keep the axis steady
	plt.scatter([xmin, xmax, xmin, xmax], [ymin, ymin, ymax, ymax], color='azure')
	# actual plot to be animated
	plot = plt.plot(x[:i+1], y[:i+1], label="epicycle curve", color='chocolate')
	# trace dot
	plt.scatter(x[i], y[i], s=20, marker='o', edgecolor='k', color='red')
	plt.title('Epicycle curve at t = '+str(i))
	plt.xlabel('$x$')
	plt.ylabel('$y$') 
	plt.suptitle("Epicycle Exercise")
	plt.xticks(xticks)
	plt.yticks(yticks)
	plt.xlim([xmin, xmax])
	plt.ylim([ymin, ymax])
	plt.axis('equal')
	plt.grid(True)
	plt.legend(loc='upper right')
	plt.pause(0.001)
	print(i)
	return plot,
 
ani = anim.FuncAnimation(fig, animate, interval = 1000, frames=n)
ani.save('epicycle_animation.mp4',fps=5)
