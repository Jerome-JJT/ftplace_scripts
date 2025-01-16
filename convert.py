
import sys
import time
import math
from PIL import Image
from show import create_image

def calculate_distance(color1, color2):
    """Calculate the Euclidean distance between two RGB colors."""
    return math.sqrt(
        (color1[0] - color2[0]) ** 2 +
        (color1[1] - color2[1]) ** 2 +
        (color1[2] - color2[2]) ** 2
    )

def find_nearest_color(pixel, color_mapping):
    """Find the nearest color from the color_mapping for a given pixel."""
    nearest_color = None
    min_distance = float('inf')

    for color in color_mapping.values():
        mapping_color = (color['red'], color['green'], color['blue'])
        distance = calculate_distance(pixel, mapping_color)

        if distance < min_distance:
            min_distance = distance
            nearest_color = color

    return nearest_color

def map_image(image_name):
    color_mapping = [
        {'id': 1, 'name': 'white', 'red': 236, 'green': 240, 'blue': 241}, 
        {'id': 2, 'name': 'lightgray', 'red': 165, 'green': 180, 'blue': 190}, 
        {'id': 3, 'name': 'darkgray', 'red': 105, 'green': 121, 'blue': 135}, 
        {'id': 4, 'name': 'black', 'red': 44, 'green': 62, 'blue': 80}, 
        {'id': 5, 'name': 'pink', 'red': 255, 'green': 167, 'blue': 209}, 
        {'id': 6, 'name': 'red', 'red': 231, 'green': 76, 'blue': 60}, 
        {'id': 7, 'name': 'orange', 'red': 230, 'green': 126, 'blue': 34}, 
        {'id': 8, 'name': 'brown', 'red': 160, 'green': 106, 'blue': 66}, 
        {'id': 9, 'name': 'yellow', 'red': 241, 'green': 196, 'blue': 15}, 
        {'id': 10, 'name': 'lime', 'red': 54, 'green': 222, 'blue': 127}, 
        {'id': 11, 'name': 'green', 'red': 2, 'green': 162, 'blue': 1}, 
        {'id': 12, 'name': 'cyan', 'red': 0, 'green': 211, 'blue': 212}, 
        {'id': 13, 'name': 'blue', 'red': 0, 'green': 152, 'blue': 255}, 
        {'id': 14, 'name': 'indigo', 'red': 0, 'green': 65, 'blue': 176}, 
        {'id': 15, 'name': 'magenta', 'red': 207, 'green': 110, 'blue': 228}, 
        {'id': 16, 'name': 'purple', 'red': 155, 'green': 28, 'blue': 182}
    ]
    color_mapping = dict(map(lambda x: (x["id"], x), color_mapping))
    
    
    
    image = Image.open(image_name).convert('RGBA')
    width, height = image.size

    grid = []

    for y in range(height):
        grid.append("")
        for x in range(width):
            pixel = image.getpixel((x, y))
            if (pixel[3] != 0):
                nearest_color = find_nearest_color(pixel, color_mapping)
            else:
                nearest_color = {'id': 0}
            # print(nearest_color)
            
            grid[-1] += chr(nearest_color["id"] + ord('A'))
    
    
    with open('converted.txt', "w") as f:
        for i in grid:
            f.write(f"{i}\n")

    create_image(grid, 10, 'converted.png')
    
    
    

    # # Calculate the size of the image
    # rows = len(grid)
    # cols = len(grid[0].strip())
    # image_width = cols * chunk_size
    # image_height = rows * chunk_size

    # # Create a new image with an RGBA mode
    # image = Image.new("RGB", (image_width, image_height))

    # # Draw the grid on the image
    # for row_idx, row in enumerate(grid):
    #     for col_idx, cell in enumerate(row.strip()):
            
    #         color = color_mapping.get(ord(cell) - ord('A'), None)
            
    #         for y in range(row_idx * chunk_size, (row_idx + 1) * chunk_size):
    #             for x in range(col_idx * chunk_size, (col_idx + 1) * chunk_size):
    #                 if (color != None):
    #                     image.putpixel((x, y), (color['red'], color['green'], color['blue']))
                    
                    
    # return image

if (__name__ == "__main__"):
    if (len(sys.argv) > 1):

        if (sys.argv[1] == "2"):
            
            map_image(sys.argv[2])
            
            # with open(sys.argv[2], "r") as f:
            #     grid = f.readlines()
            
            #     chunk_size = 10
            #     image = create_image(grid, chunk_size)
            #     image.save("output.png")
            #     print("Image saved as output.png")
