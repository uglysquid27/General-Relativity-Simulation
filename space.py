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
        
        # Add points to the map
        for point in self.points:
            ax.text(point.x, point.y, point.z, f"{point.label if point.label else f'({point.x}, {point.y}, {point.z})'}", fontsize=12)
        
        # Add a dot at the center to represent the black hole
        ax.scatter([0], [0], [0], color='black', s=100)
        
        # Add a flat wireframe
        self._add_wireframe(ax)

        ax.set_title('3D Space Map with Flat Wireframe and Black Hole')
        ax.set_xlabel('X Coordinate')
        ax.set_ylabel('Y Coordinate')
        ax.set_zlabel('Z Coordinate')
        ax.grid(True)
        plt.show()

    def _add_wireframe(self, ax):
        # Create a grid of points for the wireframe
        x = np.linspace(-10, 10, 100)
        y = np.linspace(-10, 10, 100)
        X, Y = np.meshgrid(x, y)
        Z = np.zeros_like(X)
        
        # Plot the wireframe
        ax.plot_wireframe(X, Y, Z, color='blue', alpha=0.5)

# Example Usage
if __name__ == "__main__":
    space_map = SpaceMap3D()
    
    # Adding some points to the space map
    space_map.add_point(1, 2, 3, "A")
    space_map.add_point(3, 4, 5, "B")
    space_map.add_point(5, 7, 2, "C")
    space_map.add_point(2, 9, 4)
    
    # Display the map with a flat wireframe and a black hole at the center
    space_map.display_map()
