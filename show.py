
import sys
import time


from PIL import Image

def create_image(grid, chunk_size, outp):
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

    # Calculate the size of the image
    rows = len(grid)
    cols = len(grid[0].strip())
    image_width = cols * chunk_size
    image_height = rows * chunk_size

    # Create a new image with an RGBA mode
    image = Image.new("RGBA", (image_width, image_height))

    # Draw the grid on the image
    for row_idx, row in enumerate(grid):
        for col_idx, cell in enumerate(row.strip()):
            
            color = color_mapping.get(ord(cell) - ord('A'), None)
            
            for y in range(row_idx * chunk_size, (row_idx + 1) * chunk_size):
                for x in range(col_idx * chunk_size, (col_idx + 1) * chunk_size):
                    if (color != None):
                        image.putpixel((x, y), (color['red'], color['green'], color['blue']))
                    
                    
    image.save(outp)
    return image

if (__name__ == "__main__"):
    if (len(sys.argv) > 1):

        if (sys.argv[1] == "2" and len(sys.argv) > 2):
            
            with open(sys.argv[2], "r") as f:
                grid = f.readlines()
            
                image = create_image(grid, 10, 'output.png')

            # with open(sys.argv[2], "r") as f:
            #     for i in range(starty, starty + sizey):
            #         s = ""
            #         for j in range(startx, startx + sizex):
            #             s += chr(board[j][i]["color_id"] + ord('A'))
                        
            #         print(f"{s}")
            #         f.write(f"{s}\n")
                