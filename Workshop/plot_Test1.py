import numpy as np
import matplotlib.pyplot as plt

angles = np.linspace(0, 2.0*np.pi, 101)
sine = np.sin(angles)
cosine = np.cos(angles)
xticks = np.linspace(0, 7, 15)
yticks = np.linspace(-1, 1, 11)

plt.figure()
plt.plot(angles, sine, color='r', label="sine curve", linewidth=2.0)
plt.xlabel("Angle")
plt.xticks(xticks)
plt.yticks(yticks)
plt.ylabel("Value", fontsize=16)
plt.xticks(fontsize=14, color='r')
plt.title("A fancy sine curve")
plt.legend()
plt.grid()

# plt.figure()
# plt.plot(angles, cosine, color='b', label="cosine curve")
# plt.xlabel("Angle")
# # plt.xticks(xticks)
# # plt.yticks(yticks)
# plt.ylabel("Value", fontsize=16)
# plt.xticks(fontsize=14, color='r')
# plt.title("A fancy cosine curve")
# plt.legend()
# plt.grid()

plt.show()