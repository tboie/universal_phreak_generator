#
# outputs grid image of all nested .txt files in path
#

from PIL import Image, ImageDraw
from pathlib import Path
import os, time

path = "tile_3x3/"
size_cell = 8

color_on = 255
color_off = 0
color_line = (64, 64, 64)

# on cell image
img_on = Image.new('1', (size_cell, size_cell), color=color_on)

# create grid
def create_grid(matrix, size_grid, fname):
    grid = Image.new('RGB', size=(size_grid, size_grid))

    # apply on/off cell images
    for i, row in enumerate(matrix):
        for x, c in enumerate(row):
            if c == "1":
                grid.paste(img_on, box=(x * size_cell, i * size_cell)) 
    
    # grid lines
    draw = ImageDraw.Draw(grid)
    for i in range(size_cell, size_grid, size_cell):
        draw.line([(i, 0), (i, size_grid)], fill=color_line)
        draw.line([(0, i), (size_grid, i)], fill=color_line)

    # output image
    grid.save(fname,"PNG")

# get total nested .txt files
num_files = 0
for p in Path(path).rglob('*.txt'):
    num_files += 1

# iterate .txt files in folder and generate image
i = 0
for p in sorted(Path(path).rglob('*.txt')):
    # .txt string to array of rows
    matrix = p.read_text().split("\n")
    # grid size using data array size
    size_grid = size_cell * (len(matrix) - 1)
    # out file image name
    out_file = os.path.splitext(p)[0] + ".png"

    # generate image
    timer_start = time.time()
    create_grid(matrix, size_grid, out_file)
    timer_end = time.time()

    # print status
    i += 1
    timer_str = str("{:.3f}".format(round(timer_end - timer_start, 3))) + "s"
    print(str(i) + "/" + str(num_files) + " " + timer_str + " " + str(p))

print("Finished")