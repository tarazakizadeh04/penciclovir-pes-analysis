import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap as lsc

fig = plt.figure()
ax = plt.axes(projection="3d")

indigo_maroon = lsc.from_list("OrangeBlue", ["Indigo", "Blue", "Cyan", "green", "Yellow", "Orange", "red", "Maroon"])

x = np.loadtxt(r"C:\Users\Ahoura\Downloads\my_code\new_D24.txt")
y = np.loadtxt(r"C:\Users\Ahoura\Downloads\my_code\new_D23.txt")
z = np.loadtxt(r"C:\Users\Ahoura\Downloads\my_code\new_out_energy.txt")
surf = ax.plot_trisurf(x, y, z, cmap=indigo_maroon, edgecolor='none', antialiased=False)

z_min = z.min()
z_offset = z_min - 0.15 * (z.max() - z_min)
contour = ax.tricontourf(x, y, z, levels=100, cmap=indigo_maroon, 
                         zdir='z', offset=z_offset, alpha=0.7)
ax.set_zlim(z_offset, z.max())

cbar = plt.colorbar(surf, shrink=0.6, aspect=20, format='%.2f', pad=0.1)

plt.title("Energy_D23_D24")
ax.set_xlabel('D24(degree)')
ax.set_ylabel('D23(degree)')
ax.set_zlabel('Energy(Kcal/mol)')
plt.show()