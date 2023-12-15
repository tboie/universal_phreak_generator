# creates 3x3 tiles of all possible combinations
# creates layered inverse square tile using 3x3 tile
# creates locality diagram using layered tiles

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
num_shades = layers
gray_values = np.linspace(255, 100, num_shades, dtype=int)
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

# base 3x3 tile and layers tile...

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
    genTile(m, pathTile, colors[0], "#303030")

    # initialize svg
    d = draw.Drawing(size, size, origin=(0,0))

    # apply 1x1 tile
    d.append(draw.Image(0, 0, size, size, pathTile, embed=True, opacity=1))

    # layers loop
    for layer in range(2, layers + 1):
        genTile(m, pathTile, colors[layer-1], "transparent")
        
        cSize = size / layer
        for x in range(0, layer):
            for y in range(0, layer):
                d.append(draw.Image(x * cSize, y * cSize, cSize, cSize, pathTile, embed=True, opacity=0.5))

    # save layers tile
    d.save_svg(path + file + "_layers.svg")


# locality diagram...
    
matrix = [
        [1,1,1],
        [1,0,1],
        [1,1,1],
        ]

def get_surrounding_elements(matrix, row, col):
    """
    Returns the surrounding elements of a specified element in an array matrix.
    """
    rows, cols = len(matrix), len(matrix[0])
    surrounding_elements = []
    for i in range(row-1, row+2):
        for j in range(col-1, col+2):
            if i >= 0 and i < rows and j >= 0 and j < cols:
                surrounding_elements.append(matrix[i][j])
    return surrounding_elements

def loop_through_matrix(matrix, x1, y1, x2, y2):
    s = size * (len(matrix) - 2)
    d = draw.Drawing(s, s, origin=(0,0))
    """
    Loops through all matrix elements within an array matrix bounding box.
    """
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            strTile = ''.join(str(ele) for ele in get_surrounding_elements(matrix, j, i))
            strPath = path + strTile + "_layers.svg"
            d.append(draw.Image((i-1) * size, (j-1) * size, size, size, strPath, embed=True, opacity=1))

    d.save_svg(path + "locality_diagram.svg")

# padding matrix by 2 more simple than checking NaN for surrounding elements
matrix = np.pad(matrix, 2, mode='constant')
loop_through_matrix(matrix, 1, 1, len(matrix) - 2, len(matrix) - 2)