###
# generate a custom sequence of coordinates to apply 1
# generation at a time to board.
#
# output each generation data to .txt file in path
###

import matplotlib.pyplot as plt
plt.rcParams["animation.html"] = "jshtml"

import seagull as sg
from seagull.lifeforms import Custom

import numpy as np
import os, time, json, math

# output path
path = "gen"

generations = 8
margin = 8
reverse = True

# todo: test
gen_start = 0

# board size in cells (odd has center)
board_size = generations + gen_start + margin
if board_size % 2 == 0:
    board_size += 1

board_center = math.floor(board_size / 2)

# helper funcs for square perimeter
def get_coordinates(radius, shape):
    coords = []
    
    if shape == "square":
        top_left = [0 - radius, 0 + radius]
        top_right = [0 + radius, 0 + radius]
        bottom_left = [0 - radius, 0 - radius]
        bottom_right = [0 + radius, 0 - radius]
        
        for c in connect_points(np.array([top_left, top_right])):
            coords.append(c)
        for c in connect_points(np.array([top_right, bottom_right])):
            coords.append(c)
        for c in connect_points(np.array([bottom_right, bottom_left])):
            coords.append(c)
        for c in connect_points(np.array([bottom_left, top_left])):
            coords.append(c)
    
    elif shape == "rhombus":
        top = [0, 0 + radius]
        right = [0 + radius, 0]
        bottom = [0, 0 - radius]
        left = [0 - radius, 0]
        
        for c in connect_points(np.array([top, right])):
            coords.append(c)
        for c in connect_points(np.array([right, bottom])):
            coords.append(c)
        for c in connect_points(np.array([bottom, left])):
            coords.append(c)
        for c in connect_points(np.array([left, top])):
            coords.append(c)
    
    return np.unique(coords, axis=0).tolist()      
        
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

# expanding square perimeter by rotating
gen_range = gen_start + round(generations / 2) + 1

for gen in range(gen_range):
    seq.append(get_coordinates(gen, "square"))
    seq.append(get_coordinates(gen + 1, "rhombus"))

# initial config if gen_start > 0
# todo: better perf method?
for i in range(gen_start):
    for c in seq[i]:
        seq[i + 1].append(c.copy())

# slice array to gen_start
seq = seq[gen_start:gen_start + generations]

# reverse
if reverse == True:
    seq = seq[::-1]

'''
testing changing directions

for i, gen in enumerate(seq):
    cc = []
    for c in gen:
        cc.append(c.copy())
    
    seq_rev.append(cc.copy())
    
seq = seq_rev[::-1]
'''

'''
for i, gen in enumerate(seq):
    for c in seq_rev[i]:
        seq[i].append(c.copy())
'''

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
    print(str(i + 1) + "/" + str(len(seq)) + " " + timer_str)

# write sequence to file for image drawing.
with open(path + "/sequence.json", "w") as f:
    json.dump(seq, f) # works with any number of elements in a line
