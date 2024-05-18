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
        
        black_hole_coord, distortion_coord = self._add_wireframe(ax)  # Get coordinates

        ax.scatter(*distortion_coord, color='blue', s=100, label='Distortion Coordinate')  # Plot distortion coordinate
        ax.scatter(*black_hole_coord, color='black', s=100, label='Black Hole Coordinate')  # Plot black hole

        ax.set_title('3D Space Map with Warped Space-Time (Schwarzschild Metric)')
        ax.set_xlabel('X Coordinate')
        ax.set_ylabel('Y Coordinate')
        ax.set_zlabel('Z Coordinate')
        ax.grid(True)
        ax.legend()

        plt.show()

    def _add_wireframe(self, ax):
        x = np.linspace(-10, 10, 100)
        y = np.linspace(-10, 10, 100)
        X, Y = np.meshgrid(x, y)
        r = np.sqrt(X**2 + Y**2 + 0**2) 

        G = 6.67430e-11  
        M = 100 * 1.989e30  
        c = 299792458  
        potential = 1 - (2 * G * M) / (c**2 * r)

        Z = np.zeros_like(X) + potential
        ax.plot_wireframe(X, Y, Z, color='blue', alpha=0.5)
        distortion_coord = (0, 0, Z[50, 50])  

        black_hole_coord = (0, 0, distortion_coord[2])

        return black_hole_coord, distortion_coord

if __name__ == "__main__":
    space_map = SpaceMap3D()
    
    space_map.add_point(1, 2, 3, "A")
    space_map.add_point(3, 4, 5, "B")
    space_map.add_point(5, 7, 2, "C")
    space_map.add_point(2, 9, 4)
    
    space_map.display_map()
