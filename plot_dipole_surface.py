import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap as lsc
from matplotlib.tri import Triangulation

fig = plt.figure()
ax = plt.axes(projection="3d")

indigo_maroon = lsc.from_list("OrangeBlue", ["Indigo", "Blue", "Cyan", "green", "Yellow", "Orange", "red", "Maroon"])

X = np.loadtxt(r"C:\Users\Ahoura\Downloads\my_code\new_D24.txt")
Y = np.loadtxt(r"C:\Users\Ahoura\Downloads\my_code\new_D23.txt")
Z = np.loadtxt(r"C:\Users\Ahoura\Downloads\my_code\new_out_dipole_1.txt")


surf = ax.plot_trisurf(X, Y, Z, cmap=indigo_maroon, edgecolor='none', antialiased=False)

z_min = Z.min()
z_offset = z_min - 0.15 * (Z.max() - z_min)
contour = ax.tricontourf(X, Y, Z, levels=100, cmap=indigo_maroon, 
                         zdir='z', offset=z_offset, alpha=0.7)
ax.set_zlim(z_offset, Z.max())


cbar = plt.colorbar(surf, shrink=0.6, aspect=20, format='%.2f', pad=0.1)

plt.title("Dipole_D23_D24")
ax.set_xlabel('D24')
ax.set_ylabel('D23')
ax.set_zlabel('Dipole')
plt.show()