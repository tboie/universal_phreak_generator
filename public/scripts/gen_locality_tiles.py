# creates a 2x2 inverse square tile for each 3x3 combination
# creates layered inverse square diagram

import itertools
import drawsvg as draw
import numpy as np

def split(arr, size):
    arrs = []
    while len(arr) > size:
        pice = arr[:size]
        arrs.append(pice)
        arr   = arr[size:]
    arrs.append(arr)
    return arrs

# all 3x3 combinations
bits = [0, 1]
combinations = list(itertools.product(bits, repeat=9))

# create tile
for idx, tuple in enumerate(combinations):
    d = draw.Drawing(120, 120, origin=(0,0))

    # ex) 010111001 = [[0, 1, 0], [1 ,1 ,1], [0, 0, 1]]
    token = split(tuple, 3)
    
    m = np.array(token)
    m = np.flip(m)

    # 1
    for i in range(3):
        for j in range(3):
            if m[j][i] == 1:
                d.append(draw.Rectangle(20 * i, 20 * j, 20, 20, fill='black'))
            else:
                d.append(draw.Rectangle(20 * i, 20 * j, 20, 20, fill='white'))

    # 2
    for i in range(3):
        for j in range(3):
            if m[j][i] == 1:
                d.append(draw.Rectangle(60 + (20 * i), 20 * j, 20, 20, fill='black'))
            else:
                d.append(draw.Rectangle(60 + (20 * i), 20 * j, 20, 20, fill='white'))

    # 3
    for i in range(3):
        for j in range(3):
            if m[j][i] == 1:
                d.append(draw.Rectangle(20 * i, 60 + (20 * j), 20, 20, fill='black'))
            else:
                d.append(draw.Rectangle(20 * i, 60 + (20 * j), 20, 20, fill='white'))

    # 4
    for i in range(3):
        for j in range(3):
            if m[j][i] == 1:
                d.append(draw.Rectangle(60 + (20 * i), 60 + (20 * j), 20, 20, fill='black'))
            else:
                d.append(draw.Rectangle(60 + (20 * i), 60 + (20 * j), 20, 20, fill='white'))

    file = ""
    for p in tuple:
        file = file + str(p)
    
    path = "tiles/" + file + ".svg"
    d.save_svg(path)
    
    # create layered inverse diagram using tile
    d = draw.Drawing(120, 120, origin=(0,0))
    
    d.append(draw.Image(0, 0, 120, 120, path, embed=True, opacity=0.5))

    d.append(draw.Image(0, 0, 60, 60, path, embed=True, opacity=0.5))
    d.append(draw.Image(60, 0, 60, 60, path, embed=True, opacity=0.5))
    d.append(draw.Image(0, 60, 60, 60, path, embed=True, opacity=0.5))
    d.append(draw.Image(60, 60, 60, 60, path, embed=True, opacity=0.5))

    for i in range(0,6):
        d.append(draw.Image(0 + (i * 20), 0, 20, 20, path, embed=True, opacity=0.5))
        d.append(draw.Image(0 + (i * 20), 20, 20, 20, path, embed=True, opacity=0.5))
        d.append(draw.Image(0 + (i * 20), 40, 20, 20, path, embed=True, opacity=0.5))
        d.append(draw.Image(0 + (i * 20), 60, 20, 20, path, embed=True, opacity=0.5))
        d.append(draw.Image(0 + (i * 20), 80, 20, 20, path, embed=True, opacity=0.5))
        d.append(draw.Image(0 + (i * 20), 100, 20, 20, path, embed=True, opacity=0.5))

    d.save_svg('tiles/' + file + "_layers.svg")
