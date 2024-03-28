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

# test func
def spiral(X, Y):
    x, y = 0, 0
    dx, dy = 0, -1

    coords = []

    for i in range(max(X, Y) ** 2):
        if (-X / 2 < x <= X / 2) and (-Y / 2 < y <= Y / 2):
            coords.append([[x, y]])

        if x == y or (x < 0 and x == -y) or (x > 0 and x == 1 - y):
            dx, dy = -dy, dx
        x, y = x + dx, y + dy
    
    return coords

# output path
path = "gen"

# x,y coordinates per generation
# length of array determines total generations processed
# seq = [[[1, 1], [-1, -1]], [[2, 2], [-2, -2]], [[3, 3]]]
seq = spiral(20, 20)
# remove first 0,0 coordinate
seq.pop()

# initial config pattern
initial_config = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]

# board size in cells (odd has center)
board_size = 99
board_center = round(board_size / 2) - 1

# start by applying initial config to board and run 1 generation
board = sg.Board(size=(board_size, board_size))
board.add(Custom(initial_config), loc=(board_center - 1, board_center - 1))

sim = sg.Simulator(board)
sim.run(sg.rules.conway_classic, iters=1)
hist = sim.get_history()

# .txt file output
if not os.path.exists(path):
    os.makedirs(path)

np.savetxt(path + "/gen_00000000.txt", hist[0], delimiter="", fmt="%d")
np.savetxt(path + "/gen_00000001.txt", hist[1], delimiter="", fmt="%d")

# apply sequence locations to board history and run board for 1 generation
for i, gen in enumerate(seq):
    timer_start = time.time()

    board = sg.Board(size=(board_size, board_size))
    board.add(Custom(hist[1]), loc=(0, 0))

    # add sequence coordinates
    for loc in gen:
        # loc = y, x
        board.add(Custom([[True]]), loc=(board_center - loc[1], board_center + loc[0]))
    
    # run 1 generation
    sim = sg.Simulator(board)
    sim.run(sg.rules.conway_classic, iters=1)
    hist = sim.get_history()

    # debug gen coordinates
    # np.savetxt(path + "/orig_" + '{:08}'.format(i + 2) + ".txt", hist[0], delimiter="", fmt="%d")
    
    # data .txt output
    np.savetxt(path + "/gen_" + '{:08}'.format(i + 2) + ".txt", hist[1], delimiter="", fmt="%d")

    # console logging
    timer_end = time.time()
    timer_str = str("{:.3f}".format(round(timer_end - timer_start, 3))) + "s"
    print(str(i + 2) + "/" + str(len(seq) + 2) + " " + timer_str)

# write sequence to file for image drawing.
# add first 2 gens to beginning of seq
seq.insert(0, [[]])
seq.insert(0, [[]])
with open(path + "/sequence.json", "w") as f:
    json.dump(seq, f) # works with any number of elements in a line
