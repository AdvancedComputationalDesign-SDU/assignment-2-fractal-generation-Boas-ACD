# Function to generate lines between polygon vetices and a center point
def lines(center, radius, num_sides):
    import math
    import matplotlib.pyplot as plt

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
    import math
    import matplotlib.pyplot as plt
    polygon_vertices = []
    angle = 2 * math.pi / num_sides
    cx, cy = center

    for i in range(num_sides):
        x = cx + radius * math.sin(i * angle)
        y = cy + radius * math.cos(i * angle)
        polygon_vertices.append((x, y))
        

    return polygon_vertices