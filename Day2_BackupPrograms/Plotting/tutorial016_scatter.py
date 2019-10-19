# Plotting tutorials in Python
# Scatter Plot Illustration
# sine scatter plot

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.style.use('default')

# To have the same random numbers repeated again and again.
np.random.seed(2785)

N = 1001
X = np.linspace(-2.0*np.pi, 2.0*np.pi, N)
# Y = np.sin(X)
Y = 0.1*np.random.normal(0, 1, N) + np.sin(X)

# Default
# plt.scatter(X, Y)

# Some additions : label, marker, marker colour
# For different Marker styles : https://matplotlib.org/api/markers_api.html
plt.scatter(X, Y, label='sine scatter', marker='o', c='chocolate', s=30, edgecolors='blue', alpha=0.95, linewidths=0.75)

# marker size = in area of pixels! not mere size of pixel
# More fancier additions: marker size, edge colour, transparency, edgewidth
# marker size is in area of pixels! so, specify a large value
# plt.scatter(X, Y, label='sine scatter', marker='p', c='chocolate',
#            s=1000, edgecolors='blue', alpha=0.5,
#            linewidths=1.5)

plt.xlabel('Angles')
plt.ylabel('Points')
plt.title('Sample Scatter Plot')
plt.grid(True)
plt.savefig("ScatterPlot.png", format='png', dpi=400)
plt.legend()
plt.show()
