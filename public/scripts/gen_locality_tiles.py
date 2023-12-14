# creates 3x3 tiles of all possible combinations
# creates layered inverse square tile using 3x3 tile

import itertools
import drawsvg as draw
import numpy as np

# tile size
# note: check rectangle border when not a multiple of 2 and 3
size = 120

# total layers
layers = 4

# path to tiles
path = "../tiles/"

# generate gray scale colors
num_shades = layers + 1
gray_values = np.linspace(0, 255, num_shades, dtype=int)
colors = [f"#{val:02x}{val:02x}{val:02x}" for val in gray_values]

# 3x3 base tile
def genTile(m, p, color, colorBG):
    d = draw.Drawing(size, size, origin=(0,0))
    tSize = size / 3

    for i in range(3):
        for j in range(3):
            if m[j][i] == 1:
                d.append(draw.Rectangle(tSize * i, tSize * j, tSize, tSize, fill=color))
            else:
                d.append(draw.Rectangle(tSize * i, tSize * j, tSize, tSize, fill=colorBG))

    d.save_svg(p)

# main...

# all 3x3 combinations
bits = [0, 1]
combinations = list(itertools.product(bits, repeat=9))

for idx, tuple in enumerate(combinations):
    # 010111001 tuple to [[0, 1, 0], [1 ,1 ,1], [0, 0, 1]]
    m = np.array_split(tuple, 3)

    # flip array
    m = np.flip(m)

    # tile file name and path
    file = ""
    for p in tuple:
        file = file + str(p)

    pathTile = path + file + ".svg"

    # create base 1x1 tile
    genTile(m, pathTile, colors[1], colors[0])

    # initialize svg
    d = draw.Drawing(size, size, origin=(0,0))

    # apply 1x1 tile
    d.append(draw.Image(0, 0, size, size, pathTile, embed=True, opacity=1))

    # layers loop
    for layer in range(2, layers + 1):
        genTile(m, pathTile, colors[layer], "transparent")
        
        cSize = size / layer
        for x in range(0, layer):
            for y in range(0, layer):
                d.append(draw.Image(x * cSize, y * cSize, cSize, cSize, pathTile, embed=True, opacity=1))

    # save layers tile
    d.save_svg(path + file + "_layers.svg")
