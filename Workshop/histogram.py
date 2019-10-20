import matplotlib.mlab as mlab
import numpy as np
import matplotlib.pyplot as plt

# To have the same random numbers repeated again and again.
np.random.seed(2785)

mean = 170
sd = 15
N = 1000
binsize = 50

# Data
height = np.random.normal(mean, sd, N)

counts, bins, extras = plt.hist(height, binsize, facecolor='chocolate', edgecolor='k', label='IQs', density=True)
# An idealised PDF
# pdf = mlab.normpdf(bins, mean, sd) # Creates the pdf of normal distribution
# plt.plot(bins, pdf, label='series', color='xkcd:navy blue')

plt.show()