import math
import matplotlib.pyplot as plt

# Function to generate lines between polygon vetices and a center point
def lines(center, radius, num_sides):
    lines_vertices = []
    angle = 2 * math.pi / num_sides
    cx, cy = center

    for i in range(num_sides):
        x = cx + radius * math.sin(i * angle)
        y = cy + radius * math.cos(i * angle)
        lines_vertices.append((x, y))
        lines_vertices.append(center)
        

    return lines_vertices

# Function to generate polygon vertices
def polygon(center, radius, num_sides):
    polygon_vertices = []
    angle = 2 * math.pi / num_sides
    cx, cy = center

    for i in range(num_sides):
        x = cx + radius * math.sin(i * angle)
        y = cy + radius * math.cos(i * angle)
        polygon_vertices.append((x, y))
        

    return polygon_vertices


# Test Example
center = (0, 0)
radius = 50
num_sides = 5

# Generate polygon vertices
polygon_vertices = polygon(center, radius, num_sides)
print("Polygon vertices:", polygon_vertices)
# Close Polygon
polygon_vertices.append(polygon_vertices[0])

# Make a line from center point to each vertex
line_vertices = lines(center, radius, num_sides)
print("Line vertices:", line_vertices)

# Plot polygon and lines
x_vals, y_vals = zip(*polygon_vertices)
line_x_vals, line_y_vals = zip(*line_vertices)

plt.plot(x_vals, y_vals, 'bo-', label="Original Polygon")
plt.plot(line_x_vals, line_y_vals, 'ro-', label="Line Polygon")
plt.plot(center[0], center[1], 'kx', label="Center of Rotation")
plt.gca().set_aspect('equal', adjustable='box')
plt.legend()
plt.grid(True)
plt.show()