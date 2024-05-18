import numpy as np
import matplotlib.pyplot as plt

G = 6.67430e-11  
c = 2.998e8  
solar_mass = 1.989e30  
def schwarzschild_radius(mass):
    return 2 * G * mass / c**2

def gravitational_potential(x, y, r_s):
    r = np.sqrt(x**2 + y**2)
    return -G * mass / (r + 1e-9)  

mass = 100e6 * solar_mass  
r_s = schwarzschild_radius(mass)

grid_size = 100
spacing = 1
x = np.arange(-grid_size, grid_size + spacing, spacing)
y = np.arange(-grid_size, grid_size + spacing, spacing)
X, Y = np.meshgrid(x, y)

Z = gravitational_potential(X, Y, r_s)

# Plotting the 2D map
plt.figure(figsize=(10, 10))
plt.contourf(X, Y, Z, levels=50, cmap='viridis')
plt.colorbar(label='Gravitational Potential')
plt.title('2D Space-Time Map Around a Black Hole')
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.show()
