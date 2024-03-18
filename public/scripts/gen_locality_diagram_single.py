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
layers = 32

# path to tiles & diagram
path = "out/"

# experimenting...

# inverse square opacity change
changeOpacity = False

# inverse square color scale
changeColor = False


# funcs...

# generate inverse square gray scale colors
grays = []
for layer in range(2, layers + 1):
    val = int(255 * (1 / math.sqrt(layer)))
    grays.append('#%02x%02x%02x' % (val, val, val))

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

# loop matrix and create locality_diagram
def gen_diagram(m, x1, y1, x2, y2, layer):
    s = size * (len(m) - 2)
    #d = draw.Drawing(s, s, origin=(0,0))

    d_single = draw.Drawing(s, s, origin=(0,0))
    d_single.append(draw.Rectangle(0, 0, s, s, fill="#000000"))

    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            strTile = ''.join(str(ele) for ele in get_surrounding_elements(m, j, i))

            strPath = path + strTile + "_layers_" + str(layer) + ".svg"
            strPath_single = path + strTile + "_single_" + str(layer) + ".svg"
      
            if layer > 0:
                #d.append(draw.Image((i-1) * size, (j-1) * size, size, size, strPath, embed=True, opacity=1))                
                d_single.append(draw.Image((i-1) * size, (j-1) * size, size, size, strPath_single, embed=True, opacity=1))
            else:
                if m[i][j] == 1:
                    d_single.append(draw.Rectangle((i-1) * size, (j-1) * size, size, size, fill="#FFFFFF", stroke="#000000"))

    #if layer > 0:
        #d.save_svg(path + "locality_diagram_layered_" + str(layer) + ".svg")
    
    d_single.save_svg(path + "locality_diagram_single_" + str(layer) + ".svg")


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
    pathTile = path + file + "_layers_1.svg"
    pathTile_single = path + file + "_single_1.svg"

    # create base 1x1 tile
    genTile(m, pathTile, "#FFFFFF", "#000000")
    genTile(m, pathTile_single, "#FFFFFF", "#000000")

    # initialize layers tile svg
    #d_layers = draw.Drawing(size, size, origin=(0,0))

    # apply 1x1 tile
    #d_layers.append(draw.Image(0, 0, size, size, pathTile, embed=True, opacity=1))

    # layers loop
    for layer in range(1, layers + 1):
        tSize = size / layer

        # initialize single generation propagation tile
        d_single = draw.Drawing(size, size, origin=(0,0))

        opacity = 1
        if changeOpacity == True:
            opacity = 1 / math.sqrt(layer + 1)
        
        color = "#FFFFFF"
        if changeColor == True:
            color = grays[layer-2]

        # base 1x1 tile with transparent bg for layering
        genTile(m, pathTile, color, "transparent")

        for x in range(0, layer):
            for y in range(0, layer):
                #d_layers.append(draw.Image(x * tSize, y * tSize, tSize, tSize, pathTile, embed=True, opacity=opacity))
                d_single.append(draw.Image(x * tSize, y * tSize, tSize, tSize, pathTile, embed=True, opacity=opacity))
                
        # save layers tile
        #d_layers.save_svg(path + file + "_layers_" + str(layer) + ".svg")
        d_single.save_svg(path + file + "_single_" + str(layer) + ".svg")

    # base 1x1 tile was modified, re-create it
    genTile(m, pathTile, "#FFFFFF", "#000000")


# locality_diagram.svg...

for layer in range(0, layers + 1):
    gen_diagram(matrix, 1, 1, len(matrix) - 2, len(matrix) - 2, layer)

# cleanup files...

for layer in range(1, layers + 1):
    for idx, bits in enumerate(combinations):
        f = path + ''.join(map(str, bits)) + "_layers_" + str(layer) + ".svg"
        if os.path.exists(f):
            os.remove(f)

        f = path + ''.join(map(str, bits)) + "_single_" + str(layer) + ".svg"
        if os.path.exists(f):
            os.remove(f)
