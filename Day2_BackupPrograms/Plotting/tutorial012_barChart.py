# Plotting tutorials in Python
# bar chart Plots
# illustration

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.mlab as mlab 

# mpl.style.use('classic')
mpl.style.use('seaborn')

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

counts, bins = np.histogram(IQ, binsize, density=True)
# print(np.shape(counts), np.shape(bins))
errors = np.ones(50)*0.5
bar_Width = 1.5

# An idealised PDF
pdf = mlab.normpdf(bins, mean, sd) # Creates the pdf of normal distribution
plt.plot(bins, pdf, label='series', color='xkcd:navy blue')

plt.bar(bins[:-1], counts, facecolor='chocolate', edgecolor='k', width=bar_Width, label='sample bar1')#, yerr=errors)
plt.xlabel('values')
plt.ylabel('Count/Fraction')
plt.title('Simple Bar chart')
plt.grid(True)
plt.legend()
plt.savefig("barChart.png", format="png", dpi=400)
plt.show()
