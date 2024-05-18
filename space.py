import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

class Point3D:
    def __init__(self, x, y, z, label=None):
        self.x = x
        self.y = y
        self.z = z
        self.label = label

class SpaceMap3D:
    def __init__(self):
        self.points = []

    def add_point(self, x, y, z, label=None):
        point = Point3D(x, y, z, label)
        self.points.append(point)

    def display_map(self):
        fig = plt.figure(figsize=(10, 10))
        ax = fig.add_subplot(111, projection='3d')
        
        for point in self.points:
            ax.text(point.x, point.y, point.z, f"{point.label if point.label else f'({point.x}, {point.y}, {point.z})'}", fontsize=12)
        
        black_hole_coord, distortion_coord, schwarzschild_calc = self._add_wireframe(ax)  # Get coordinates and calculation

        ax.scatter(*distortion_coord, color='blue', s=100, label='Distortion Coordinate')  # Plot distortion coordinate
        ax.scatter(*black_hole_coord, color='black', s=100, label='Black Hole Coordinate')  # Plot black hole

        ax.set_title('3D Space Map with Warped Space-Time (Schwarzschild Metric)')
        ax.set_xlabel('X Coordinate')
        ax.set_ylabel('Y Coordinate')
        ax.set_zlabel('Z Coordinate')
        ax.grid(True)
        ax.legend()

        plt.show()

        # Print the calculation process outside the Cartesian coordinate system
        print("Calculation Process:")
        print(f"Gravitational Constant (G): {G} m^3 kg^-1 s^-2")
        print(f"Mass of Black Hole (M): {M} kg")
        print(f"Speed of Light (c): {c} m/s")
        print(f"Potential at Black Hole Location: {potential}")
        print(f"Schwarzschild Metric at Black Hole: {schwarzschild_calc}")

    def _add_wireframe(self, ax):
        x = np.linspace(-10, 10, 100)
        y = np.linspace(-10, 10, 100)
        X, Y = np.meshgrid(x, y)
        r = np.sqrt(X**2 + Y**2 + 0**2)  # Radial distance from the black hole at origin

        # Schwarzschild Metric Equation
        G = 6.67430e-11  # Gravitational constant in m^3 kg^-1 s^-2
        M = 100 * 1.989e30  # Mass of the black hole in kg (100 times solar mass)
        c = 299792458  # Speed of light in m/s
        potential = 1 - (2 * G * M) / (c**2 * r)

        Z = np.zeros_like(X) + potential
        ax.plot_wireframe(X, Y, Z, color='blue', alpha=0.5)

        # Calculate and return the coordinates of the distortion caused by the black hole
        # In this case, we take a point slightly below the black hole to represent the distortion
        distortion_coord = (0, 0, Z[50, 50])  # Adjust indices as needed

        # Adjust black hole coordinates to match z-coordinate of the distortion
        black_hole_coord = (0, 0, distortion_coord[2])

        # Calculate the Schwarzschild metric value at the black hole's location
        schwarzschild_calc = 1 - (2 * G * M) / (c**2 * r[50, 50])  # Using radial distance at black hole's location

        return black_hole_coord, distortion_coord, schwarzschild_calc

if __name__ == "__main__":
    space_map = SpaceMap3D()
    
    space_map.add_point(1, 2, 3, "A")
    space_map.add_point(3, 4, 5, "B")
    space_map.add_point(5, 7, 2, "C")
    space_map.add_point(2, 9, 4)
    
    space_map.display_map()
