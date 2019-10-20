import numpy as np
import matplotlib.pyplot as plt
import matplotlib._color_data as mcd
import matplotlib as mpl
print(mpl.style.available)

mpl.style.use('classic')

theta = np.linspace(0, 2.0*np.pi, 101)
sine = np.sin(theta)
cosine = np.cos(theta)

# print(mcd.CSS4_COLORS.items())

xnumbers = np.linspace(0, 7, 15)
ynumbers = np.linspace(-1, 1, 11)

plt.plot(theta, sine, color='blueviolet', label='sin') # r - red colour
plt.xlabel("Angle in Radians")
plt.ylabel("Magnitude")
plt.title("Plot of some trigonometric functions")
plt.xticks(xnumbers)
plt.yticks(ynumbers)
plt.legend()
plt.grid()
plt.axis([0, 6.5, -1.1, 1.1]) # [xstart, xend, ystart, yend]
plt.savefig("Full_SinePlot.jpg", format="jpg", dpi=400)
plt.show()