###
# outputs grid image of all .txt files in path (recursive)
# optional: apply sequence visual from "sequence.json"
#           from gen_custom_seq.py
###

from PIL import Image, ImageDraw
from pathlib import Path
import os, time, json

# data path
path = "gen"

# grid size in pixels
grid_size = 400

# todo: script argument
# board size in cells
grid_cells = 99

# grid styling
grid_lines = True

# cell size in pixels
cell_size = round(grid_size / grid_cells)

color_on = 255
color_seq = (0, 255, 0, 64) # alpha not working
color_off = 0
color_line = (64, 64, 64)

# on cell image
img_on = Image.new('1', (cell_size, cell_size), color=color_on)
img_seq = Image.new('RGBA', (cell_size, cell_size), color=color_seq)

# create grid
def create_grid(gen, matrix, grid_size, fname, seq):
    grid = Image.new('RGB', size=(grid_size, grid_size))

    # apply on/off cell images
    for i, row in enumerate(matrix):
        for x, c in enumerate(row):
            if c == "1":
                grid.paste(img_on, box=(x * cell_size, i * cell_size)) 
    
    # grid lines
    if grid_lines == True:
        draw = ImageDraw.Draw(grid)
        for i in range(cell_size, grid_size, cell_size):
            draw.line([(i, 0), (i, grid_size)], fill=color_line)
            draw.line([(0, i), (grid_size, i)], fill=color_line)

    # apply sequence from gen_custom_seq.py (optional)
    board_center = round(grid_cells / 2) - 1
    if gen < len(seq):
        for c in seq[gen]:
            if len(c) > 0:
                x = c[0]
                y = c[1]

                grid.paste(img_seq, box=((board_center + x) * cell_size, (board_center - y) * cell_size))

    # output image
    grid.save(fname,"PNG")

# load sequence if exists
seq = []
f_seq = open(path + "/sequence.json")
if f_seq:
    seq = json.load(f_seq)

# get total nested .txt files for logging
num_files = 0
for p in Path(path).rglob('*.txt'):
    num_files += 1

# iterate .txt files in folder and generate image
i = 0
for p in sorted(Path(path).rglob('*.txt')):
    # .txt string to array of rows
    matrix = p.read_text().split("\n")

    # out file image name
    file_out = os.path.splitext(p)[0] + ".png"

    # generate image
    timer_start = time.time()
    create_grid(i, matrix, grid_size, file_out, seq)
    timer_end = time.time()

    # print status
    i += 1
    timer_str = str("{:.3f}".format(round(timer_end - timer_start, 3))) + "s"
    print(str(i) + "/" + str(num_files) + " " + timer_str + " " + file_out)

print("Finished")