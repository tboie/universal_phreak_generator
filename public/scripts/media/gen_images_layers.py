###
# outputs grid image of all .txt files for each layer radius
# to sequences/[layer #]/
#
# not implemented: seq_step visual
###

from PIL import Image, ImageDraw
from pathlib import Path
import os, time, json, math

# data path
path_base = "../sequences/out/"
radius_sizes = list(range(0, 9))

# todo: script argument
# board size in cells
# generations + 1
grid_cells = 51

# grid size in pixels
# multiple of grid_cells for alignment (no floats)
grid_size = 408

# step sequence visual (not implemented)
seq_step = False

# grid styling
grid_lines = False

#color_on = (0, 0, 255, 100)
color_on = 255
color_seq = (0, 255, 0, 64) # alpha not working
# color_off = 255
color_line = (64, 64, 64)

# cell size in pixels
cell_size = round(grid_size / grid_cells)

# on cell image
img_on = Image.new('1', (cell_size, cell_size), color=color_on)
# grid has to be RGB for alpha to work?
img_seq = Image.new('RGBA', (cell_size, cell_size), color=color_seq)

# create grid
def create_grid(gen, matrix, grid_size, fname, seq):
    grid = Image.new('RGBA', size=(grid_size, grid_size), color=(255, 255, 255, 0))

    # apply on/off cell images
    for i, row in enumerate(matrix):
        for x, c in enumerate(row):
            if c == "1":
                grid.paste(img_on, box=(x * cell_size, i * cell_size)) 

    # apply sequence from gen_custom_seq.py (optional)
    board_center = math.floor(grid_cells / 2)
    if gen < len(seq):
        for c in seq[gen]:
            if len(c) > 0:
                x = c[0]
                y = c[1]

                grid.paste(img_seq, box=((board_center + x) * cell_size, (board_center - y) * cell_size))

    # grid lines
    if grid_lines == True:
        draw = ImageDraw.Draw(grid)
        for i in range(cell_size, grid_size, cell_size):
            draw.line([(i, 0), (i, grid_size)], fill=color_line)
            draw.line([(0, i), (grid_size, i)], fill=color_line)
    
    # output image
    grid.save(fname,"PNG")

for radius_size in radius_sizes:
    path = path_base + str(radius_size)
        
    # load sequence if exists
    seq = []
    if seq_step == True:
        f_seq = open(path + "/sequence.json")
        if f_seq:
            seq = json.load(f_seq)

    # get total nested .txt files for logging
    num_files = 0
    for p in Path(path).rglob('*.txt'):
        num_files += 1
        if seq_step == True:
            num_files += 1

    # iterate .txt files in folder and generate image
    i = 0
    prev_matrix = []

    for p in sorted(Path(path).rglob('*.txt')):
        timer_start = time.time()
            
        # .txt string to array of rows
        matrix = p.read_text().split("\n")

        # out file image name
        file_out = []
        
        if seq_step == True:
            file_path = os.path.splitext(p)[0].rsplit("_", 1)
            file_out.append(file_path[0] + '_{0:08}'.format(i) + ".png")
            file_out.append(file_path[0] + '_{0:08}'.format(i + 1) + ".png")
        else:
            file_out.append(os.path.splitext(p)[0] + ".png")
            
        # generate image
        if seq_step == True:
            gen = round(i / 2)
            create_grid(gen, prev_matrix, grid_size, file_out[0], seq)
            create_grid(gen, matrix, grid_size, file_out[1], [])
        else:
            create_grid(i, matrix, grid_size, file_out[0], seq)

        prev_matrix = matrix

        timer_end = time.time()

        i += 1
        # print status
        timer_str = str("{:.3f}".format(round(timer_end - timer_start, 3))) + "s"
        print(str(i) + "/" + str(num_files) + " " + timer_str + " " + file_out[0])

        if seq_step == True:
            i += 1
            print(str(i) + "/" + str(num_files) + " " + timer_str + " " + file_out[1])


print("Finished")