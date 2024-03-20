# add alive cells per generation using an array
# outputs each generation

import matplotlib.pyplot as plt
plt.rcParams["animation.html"] = "jshtml"

import seagull as sg
from seagull.lifeforms import Custom

import numpy as np
import os

# output path
path = "gen/"

# x,y coordinates per generation
# TODO: generate sequence using func?
seq = [[[1, 1], [-1, -1]], [[2, 2], [-2, -2]], [[3, 3], [-3, -3]]]

# initial config pattern
initial_config = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]

# board (odd has center)
board_size = 11
board_center = round(board_size / 2) - 1

# start with initial config
board = sg.Board(size=(board_size, board_size))
board.add(Custom(initial_config), loc=(board_center - 1, board_center - 1))

sim = sg.Simulator(board)
sim.run(sg.rules.conway_classic, iters=1)
hist = sim.get_history()

if not os.path.exists(path):
    os.makedirs(path)

np.savetxt(path + "0.txt", hist[0], delimiter="", fmt="%d")
np.savetxt(path + "1.txt", hist[1], delimiter="", fmt="%d")

# add locations from seq per generation
for i, gen in enumerate(seq):
    board = sg.Board(size=(board_size, board_size))
    board.add(Custom(hist[1]), loc=(0, 0))

    for loc in gen:
        board.add(Custom([[True]]), loc=(board_center + loc[1], board_center + loc[0]))

    sim = sg.Simulator(board)
    sim.run(sg.rules.conway_classic, iters=1)
    hist = sim.get_history()

    np.savetxt(path + str(i + 2) + ".txt", hist[1], delimiter="", fmt="%d")

    # display last generation sequence
    #if i == len(seq) - 1:
    #    anim = sim.animate(interval=500)
    #    plt.show()
