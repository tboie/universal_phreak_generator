###
# generate a custom sequence of coordinates to apply 1
# generation at a time to board
#
# output each generation data to .txt file in path
###

import matplotlib.pyplot as plt
plt.rcParams["animation.html"] = "jshtml"

import seagull as sg
from seagull.lifeforms import Custom

import numpy as np
import os, time, json

# output path
path = "gen"

# board size in cells (odd has center)
board_size = 599
board_center = round(board_size / 2) - 1

# helper funcs for square perimeter
def get_square_coordinates(centerX, centerY, radius):
    # Calculate the four vertices
    top_left = (centerX - radius, centerY + radius)
    top_right = (centerX + radius, centerY + radius)
    bottom_left = (centerX - radius, centerY - radius)
    bottom_right = (centerX + radius, centerY - radius)

    # Return the coordinates
    return {
        "tl": top_left,
        "tr": top_right,
        "bl": bottom_left,
        "br": bottom_right
    }

def connect_points(ends):
    d0, d1 = np.abs(np.diff(ends, axis=0))[0]
    if d0 > d1:
        return np.c_[np.linspace(ends[0, 0], ends[1, 0], d0 + 1, dtype=np.int32),
                     np.round(np.linspace(ends[0, 1], ends[1, 1], d0 + 1)).astype(np.int32)]
    else:
        return np.c_[np.round(np.linspace(ends[0, 0], ends[1, 0], d1 + 1)).astype(np.int32),
                     np.linspace(ends[0, 1], ends[1, 1], d1 + 1, dtype=np.int32)]


# x,y coordinates per generation
# length of array determines total generations processed
# ex) seq = [[[1, 1], [-1, -1]], [[2, 2], [-2, -2]], [[3, 3]]]
#seq = [[[0, 0]]]
seq = []

''' 
sample sequence:

0 1 0
1 0 1
0 1 0

1 1 1
1 0 1
1 1 1

0 0 1 0 0
0 1 0 1 0
1 0 0 0 1
0 1 0 1 0
0 0 1 0 0

1 1 1 1 1
1 0 0 0 1
1 0 0 0 1
1 0 0 0 1
1 1 1 1 1

...

'''
# fill array with 45 degree rotating square perimeter
for i in range(round(board_size / 2)):
    if i > 0:
        # rotated
        if i % 2 != 0:
            c = {
                "t": [0, i],
                "l": [i * -1, 0],
                "r": [i, 0],
                "b": [0, i * -1]
            }
            
            l1 = connect_points(np.array([c["t"], c["l"]]))
            l2 = connect_points(np.array([c["t"], c["r"]]))
            l3 = connect_points(np.array([c["l"], c["b"]]))
            l4 = connect_points(np.array([c["r"], c["b"]]))

            f = []
            for coord in [l1, l2, l3, l4]:
                for cc in coord:
                    f.append(cc)

            f = np.unique(f, axis=0)
            seq.append(f.tolist())
        # not rotated
        else:
            c = get_square_coordinates(0, 0, i - 1)

            l1 = connect_points(np.array([c["tl"], c["tr"]]))
            l2 = connect_points(np.array([c["tl"], c["bl"]]))
            l3 = connect_points(np.array([c["br"], c["bl"]]))
            l4 = connect_points(np.array([c["tr"], c["br"]]))

            f = []
            for coord in [l1, l2, l3, l4]:
                for cc in coord:
                    f.append(cc)

            f = np.unique(f, axis=0)
            seq.append(f.tolist())

# repeat sequence
for idx, s in enumerate(seq):
    if idx < len(seq) - 2:
        for c in seq[idx]:
            seq[idx+2].append(c)
        
# .txt file output
if not os.path.exists(path):
    os.makedirs(path)

hist = []
# apply sequence locations to board history and run board for 1 generation
for i, gen in enumerate(seq):
    timer_start = time.time()

    # load previous board
    board = sg.Board(size=(board_size, board_size))
    if i > 0:
        board.add(Custom(hist[1]), loc=(0, 0))

    # add sequence coordinates
    for loc in gen:
        # loc = y, x
        board.add(Custom([[True]]), loc=(board_center - loc[1], board_center + loc[0]))
    
    # run 1 generation
    sim = sg.Simulator(board)
    sim.run(sg.rules.conway_classic, iters=1)
    hist = sim.get_history()

    # output data as .txt file
    np.savetxt(path + "/gen_" + '{:08}'.format(i) + ".txt", hist[1], delimiter="", fmt="%d")

    # console logging
    timer_end = time.time()
    timer_str = str("{:.3f}".format(round(timer_end - timer_start, 3))) + "s"
    print(str(i) + "/" + str(len(seq)) + " " + timer_str)

# write sequence to file for image drawing.
with open(path + "/sequence.json", "w") as f:
    json.dump(seq, f) # works with any number of elements in a line
