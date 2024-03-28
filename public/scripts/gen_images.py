#
# outputs grid image of all nested .txt files in path
#

from PIL import Image, ImageDraw
from pathlib import Path
import os, time, math, json

# grid size in pixels
size_grid = 400
# todo: script argument
# board size in cells
num_cells = 99
size_cell = round(size_grid / num_cells)
# path
path = "gen"

# grid styling
grid_lines = True

color_on = 255
# alpha not working
color_seq = (0, 255, 0, 64)
color_off = 0
color_line = (64, 64, 64)

# on cell image
img_on = Image.new('1', (size_cell, size_cell), color=color_on)
img_seq = Image.new('RGBA', (size_cell, size_cell), color=color_seq)

# create grid
def create_grid(gen, matrix, size_grid, fname, seq):
    grid = Image.new('RGB', size=(size_grid, size_grid))

    # apply on/off cell images
    for i, row in enumerate(matrix):
        for x, c in enumerate(row):
            if c == "1":
                grid.paste(img_on, box=(x * size_cell, i * size_cell)) 
    
    # grid lines
    if grid_lines == True:
        draw = ImageDraw.Draw(grid)
        for i in range(size_cell, size_grid, size_cell):
            draw.line([(i, 0), (i, size_grid)], fill=color_line)
            draw.line([(0, i), (size_grid, i)], fill=color_line)

    # apply sequence from gen_custom_seq.py
    board_center = round(num_cells / 2) - 1
    if gen < len(seq):
        for c in seq[gen]:
            if len(c) > 0:
                x = c[0]
                y = c[1]

                grid.paste(img_seq, box=((board_center + x) * size_cell, (board_center - y) * size_cell))

    # output image
    grid.save(fname,"PNG")

# load sequence 
seq = []
f_seq = open(path + "/sequence.json")
if f_seq:
    seq = json.load(f_seq)

# get total nested .txt files
num_files = 0
for p in Path(path).rglob('*.txt'):
    num_files += 1

# iterate .txt files in folder and generate image
i = 0
for p in sorted(Path(path).rglob('*.txt')):
    # .txt string to array of rows
    matrix = p.read_text().split("\n")
    # out file image name
    out_file = os.path.splitext(p)[0] + ".png"

    # generate image
    timer_start = time.time()
    create_grid(i, matrix, size_grid, out_file, seq)
    timer_end = time.time()

    # print status
    i += 1
    timer_str = str("{:.3f}".format(round(timer_end - timer_start, 3))) + "s"
    print(str(i) + "/" + str(num_files) + " " + timer_str + " " + out_file)

print("Finished")