"""
Assignment 2: Fractal Generator

Author: Boas Olesen

Description:
This script generates fractal patterns using recursive functions and geometric transformations.
The geometric transformations focuses around polygons, with the variations being adding or subtractions of the number of sides.
The fractal pattern starts from a startpoint and ends with polygon vertices, which are the start point for the next recursive function.
Randomness has also been added, as varying between adding and subtracting between each recursive function, both for number of polygon sides, radius and end probability.
"""

# Import necessary libraries
import matplotlib.pyplot as plt
from shapely.geometry import LineString
import random

# Global list to store all line segments
line_list = []

# Defining the fractal generation function
def generate_fractal(start_point, num_polygon_sides, radius, depth, max_depth, length_scaling_factor, end_probability):
    """
    Recursive function to generate fractal patterns.
    Parameters:
     - start_point: Tuple (x, y), starting coordinate.
     - num_polygon_sides: Number of sides for the polygon.
     - radius: Radius for the polygon.
     - depth: Current recursion depth.
     - max_depth: max recursion depth.
     - length_scaling_factor: Scaling factor to vary each recursion.
     - end_probabilityh: Probability for a vertice to end its recursion.
    """
    if depth > max_depth or num_polygon_sides < 3:
        return
    
    # Generate polygon
    from Polygons import polygon, lines
    polygon_vertices = polygon(start_point, radius, num_polygon_sides)  # Makes a polygon based on center, radius and number of sides.
    polygon_vertices.append(polygon_vertices[0])    # Closes the polygon
    new_point_polygon = list(polygon_vertices)  # Makes a list for polygon vertices

    polygon_lines = LineString(new_point_polygon)   # Makes a line between the polygon vertices
    line_list.append(polygon_lines)     # Adds polygon lines to line_list

    # Generate center lines
    line_vertices = lines(start_point, radius, num_polygon_sides)   # Makes a polygon based on center, radius and number of sides.
    new_point_line = list(line_vertices)    # Makes a list for polygon vertices
    center_point = [start_point] + new_point_line   # Makes a list which connect the center point to the vertices
    center_lines = LineString(center_point) # Makes a line between the center point and the polygon vertices
    line_list.append(center_lines)  # Adds center lines to line_list

    # Increment depth
    next_depth = depth + 1

#     # Recursive calls for branches
    for vertex in polygon_vertices[:-1]:
        if random.random() < end_probability:   # chance for a vertice to stop its recursion
            continue
        
        side_adjustment = random.choice([-1, 1])    # Randomly adjust the number of sides: either -1, +1
        new_polygon_sides = max(3, num_polygon_sides + side_adjustment)

        # Randomly adjust the radius by scaling factor, with a slight random fluctuation
        random_scaling_factor = length_scaling_factor * (0.5 + random.random())  # Random factor between 0.5 and 1.5
        new_radius = radius * random_scaling_factor

        generate_fractal(vertex, new_polygon_sides,  new_radius, next_depth, max_depth, length_scaling_factor, end_probability)

# # Main execution
if __name__ == "__main__":
    # Parameters
    start_point = (0, 0)
    num_polygon_sides = 4
    initial_radius = 100
    recursion_depth = 0
    max_recursion_depth = 3
    length_scaling_factor = 1
    end_probability = 0.4

    # Generate the fractal
    generate_fractal(start_point, num_polygon_sides, initial_radius, recursion_depth, max_recursion_depth, length_scaling_factor, end_probability)

    # Visualization
    fig, ax = plt.subplots()
    for line in line_list:
        x, y = line.xy
        ax.plot(x, y, color='green', linewidth=1)

    # Optional: Customize the plot
    ax.set_aspect('equal')
    plt.axis('off')
    plt.show()
    # Save the figure
    fig.savefig('images/pol_cen2.png', dpi=300, bbox_inches='tight')