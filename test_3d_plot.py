import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import numpy as np

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

#data
X = [0.4,0.6,0.7,0.85,0.95]
Y = [260,320,360,400,440]
X, Y = np.meshgrid(X, Y)
Z = [2,3,4,2,1]

# Plot the surface.
surf = ax.plot_surface(X, Y, Z)


# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()
