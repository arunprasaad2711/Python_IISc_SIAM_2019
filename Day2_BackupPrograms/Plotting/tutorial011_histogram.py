# Plotting tutorials in Python
# Histogram Plots
# IQ distribution of a random normal population

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.mlab as mlab 

# mpl.style.use('classic')
mpl.style.use('default')

# To have the same random numbers repeated again and again.
np.random.seed(2785)

# For details
# https://stackoverflow.com/questions/21494489/what-does-numpy-random-seed0-do

mean = 100
sd = 15
N = 1000
binsize = 50

# Data
IQ = np.random.normal(mean, sd, N)

counts, bins, extras = plt.hist(IQ, binsize, facecolor='chocolate', edgecolor='k', label='IQs', density=True)

# An idealised PDF
pdf = mlab.normpdf(bins, mean, sd) # Creates the pdf of normal distribution
plt.plot(bins, pdf, label='series', color='xkcd:navy blue')

plt.xlabel('IQ')
plt.ylabel('Count/Fraction')
plt.xticks(bins)
plt.title('IQ Distribution Histogram')
plt.grid(True)
plt.legend()
plt.show()
