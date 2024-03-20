import itertools, os, time
import numpy as np

import matplotlib.pyplot as plt
plt.rcParams["animation.html"] = "jshtml"

import seagull as sg
from seagull.lifeforms import Custom

# Tile Quadrant Size
size_matrix = 3

# Tile Tesselation Size
num_tiles = 3

# Board Margin
margin = (size_matrix * num_tiles) * 2

# Total Generations
generations = 100

# Output Animated GIF
animated_gif = False

# Output Folder Path (ex: Tile Size/Tesselation Size/Number Generations)
path = "tile_" + str(size_matrix) + "x" + str(size_matrix) + "/"
path = path + "tess_" + str(num_tiles) + "x" + str(num_tiles) + "/"
path = path + "gen_" + str(generations) + "/"
#if not os.path.exists(path):
os.makedirs(path)

# Script Performance
script_start = time.time()

# Generate all combinations of a 3x3 matrix
combinations = list(itertools.product([0, 1], repeat=pow(size_matrix, 2)))

# Loop combinations
for idx, combo in enumerate(combinations):
    # Start Performance Timer
    item_start = time.time()

    str_matrix = ''.join(str(i) for i in combo)
    os.makedirs(path + str_matrix)

    # Reshape the flat list into a 3x3 matrix
    matrix = np.array([combo[i:i + size_matrix] for i in range(0, pow(size_matrix, 2), size_matrix)])

    # Tile Quadrants
    #if idx == 30:
    q1 = matrix
    # counter-clockwise
    q2 = np.rot90(q1)
    q3 = np.rot90(q2)
    q4 = np.rot90(q3)

    # Tile
    size_quad = len(q1)
    size_tile = size_quad * 2

    # Board
    size_board = size_tile * num_tiles
    size_board = size_board + (margin * 2)
    board = sg.Board(size=(size_board , size_board))

    for y in range(num_tiles):
        loc_y = (y * size_tile) + margin

        for x in range(num_tiles):
            loc_x = (x * size_tile) + margin + size_quad
            
            # note: loc = y, x
            board.add(Custom(q1), loc=(loc_y, loc_x))
            board.add(Custom(q2), loc=(loc_y, loc_x - size_quad))
            board.add(Custom(q3), loc=(loc_y + size_quad, loc_x - size_quad))
            board.add(Custom(q4), loc=(loc_y + size_quad, loc_x))

    # Simulate board
    sim = sg.Simulator(board)      
    sim.run(sg.rules.conway_classic, iters=generations)

    # Logging
    hist = sim.get_history()
    #print(hist)

    for i, gen in enumerate(hist):
        np.savetxt(path + str_matrix + "/" + str(i) + '.txt', gen, delimiter="", fmt="%d")
    
    # Animated GIF
    if animated_gif == True:
        anim = sim.animate(interval=1)
        anim.save(path + str_matrix + "/animation.gif", fps=4)
        # Display
        #plt.show()

    # Console Status
    str_status = str(idx + 1) + "/" + str(pow(2, size_matrix * size_matrix))
    item_end = time.time()
    str_time = str(round(item_end - item_start, 3)) + "s"
    
    print(str_status + " " + str_time)

# Total Elapsed Time
script_end = time.time()
print("Total Elapsed: " + str(round(script_end - script_start, 3)) + "s")
