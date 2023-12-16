# creates 3x3 tiles of all possible combinations
# creates layered inverse square tile using 3x3 tile
# creates matrix "locality_diagram.svg" using layered tiles

import itertools
import drawsvg as draw
import numpy as np
import os
import math

# config...

# board matrix
matrix = [
        [1,1,1],
        [1,0,1],
        [1,1,1],
        ]

# tile size
size = 120

# total layers
layers = 8

# path to tiles
path = "out/"

# funcs...

# 3x3 base tile
# todo: should first layer have opacity?

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

# returns 3x3 of matrix element
def get_surrounding_elements(m, row, col):
    rows, cols = len(m), len(m[0])
    surrounding_elements = []
    for i in range(row-1, row+2):
        for j in range(col-1, col+2):
            if i >= 0 and i < rows and j >= 0 and j < cols:
                surrounding_elements.append(m[i][j])
    return surrounding_elements

# loop matrix and return 3x3 combinations
def get_matrix_combinations(m, x1, y1, x2, y2):
    combos = []
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            combos.append(get_surrounding_elements(m, j, i))

    return combos

# loop matrix and create locality_diagram
def gen_diagram(m, x1, y1, x2, y2):
    s = size * (len(m) - 2)
    d = draw.Drawing(s, s, origin=(0,0))

    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            strTile = ''.join(str(ele) for ele in get_surrounding_elements(m, j, i))
            strPath = path + strTile + "_layers.svg"
            d.append(draw.Image((i-1) * size, (j-1) * size, size, size, strPath, embed=True, opacity=1))

    d.save_svg(path + "locality_diagram.svg")

# main...
    
# create base 3x3 tile and layers tile...

# padding matrix by 2 more simple than checking NaN for surrounding elements
matrix = np.pad(matrix, 2, mode='constant')

# get matrix cell 3x3 combinations
combinations = get_matrix_combinations(matrix, 1, 1, len(matrix) - 2, len(matrix) - 2)

for bits in combinations:
    # 010111001 to [[0, 1, 0], [1 ,1 ,1], [0, 0, 1]]
    m = np.array_split(bits, 3)

    # flip array
    m = np.flip(m)

    # tile file name and path
    file = ''.join(map(str, bits))
    pathTile = path + file + ".svg"

    # create base 1x1 tile
    genTile(m, pathTile, "#FFFFFF", "#000000")

    # initialize svg
    d = draw.Drawing(size, size, origin=(0,0))

    # apply 1x1 tile
    d.append(draw.Image(0, 0, size, size, pathTile, embed=True, opacity=1))

    # base 1x1 tile with transparent bg for layering
    genTile(m, pathTile, "#FFFFFF", "transparent")

    # layers loop
    for layer in range(2, layers + 1):
        cSize = size / layer

        for x in range(0, layer):
            for y in range(0, layer):
                d.append(draw.Image(x * cSize, y * cSize, cSize, cSize, pathTile, embed=True, opacity=1/math.sqrt(layer)))

    # save layers tile
    d.save_svg(path + file + "_layers.svg")


# locality_diagram.svg...
gen_diagram(matrix, 1, 1, len(matrix) - 2, len(matrix) - 2)

# cleanup files...
for idx, bits in enumerate(combinations):
    f = path + ''.join(map(str, bits)) + ".svg"
    if os.path.exists(f):
        os.remove(f)

    f = path + ''.join(map(str, bits)) + "_layers.svg"
    if os.path.exists(f):
        os.remove(f)
