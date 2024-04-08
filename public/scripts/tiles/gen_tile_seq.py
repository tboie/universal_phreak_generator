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
generations = 8

# Output Initial Tesselation RLE
out_tess = False

# Output Data of Each Generation to Text File
out_txt = True

# Output RLE File for Each Generation
out_rle = False

# Output Tile Image
out_img_tile = False

# Output Animated GIF of all Generations
out_img_animated = False

# Output Folder Path (ex: Tile Size/Tesselation Size/Number Generations)
path = "tile_" + str(size_matrix) + "x" + str(size_matrix) + "/"
path = path + "tess_" + str(num_tiles) + "x" + str(num_tiles) + "/"
path = path + "gen_" + str(generations) + "/"

# Convert boolean array to uncompressed RLE string
# https://conwaylife.com/wiki/Run_Length_Encoded
def arrayToRLE(arr):
    data = ""

    for row in arr:
        s = ""

        for ele in row:
            if ele == True or ele == 1:
                s += "o"
            else:
                s += "b"

        data += encodeRLE(s) + "$"
    
    return data

# Encode string to RLE
def encodeRLE(message):
    encoded_message = ""
    i = 0
 
    while (i <= len(message)-1):
        count = 1
        ch = message[i]
        j = i
        while (j < len(message)-1):
            if (message[j] == message[j+1]):
                count = count+1
                j = j+1
            else:
                break
        encoded_message=encoded_message+str(count)+ch
        i = j+1
    return encoded_message


# Begin...

# Script Performance
script_start = time.time()

# Generate all combinations of a 3x3 matrix
combinations = list(itertools.product([0, 1], repeat=pow(size_matrix, 2)))

# Loop combinations
for idx, combo in enumerate(combinations):
    # Tile quadrant matrix to binary string
    str_matrix = ''.join(str(i) for i in combo)

    # Print Item Information to Console
    str_status = str(idx + 1) + "/" + str(pow(2, size_matrix * size_matrix))
    print(str_status)
    print(str_matrix)

    # Start Performance Timer
    item_start = time.time()

    # Create directory
    if not os.path.exists(path + str_matrix):
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

    # Generate Tesselation RLE
    if out_tess == True:
        tile_arr = []

        # Create Tile Array from Quadrants
        for row in range(len(q1)):
            tile_arr.append(np.concatenate((q2[row], q1[row])))
        for row in range(len(q1)):
            tile_arr.append(np.concatenate((q3[row], q4[row])))

        # Tile RLE String
        tile_rle = arrayToRLE(tile_arr)
        rle_lines = tile_rle.split("$")

        # Row of Tiles as RLE string
        str_rle_row = ""
        for row in range(len(rle_lines) - 1):
            for y in range(num_tiles):
                str_rle_row = str_rle_row + rle_lines[row]
            
            str_rle_row += "$"

        # Add Rows of RLE string
        str_rle = ""
        for row in range(num_tiles):
            str_rle += str_rle_row
        
        # Output tesselation.rle
        with open(path + str_matrix + "/tesselation.rle", "w") as file:
            file.write("x = 0, y = 0, rule = B3/S23\n")
            file.write(str_rle)

    if out_txt == True or out_rle == True or out_img_animated == True or out_img_tile == True:
        # Tile
        size_quad = len(q1)
        size_tile = size_quad * 2

        # Single Tile Image
        if out_img_tile:
            board = sg.Board(size=(size_tile, size_tile))

            for y in range(1):
                loc_y = (y * size_tile)

                for x in range(1):
                    loc_x = (x * size_tile) + size_quad
                    
                    # note: loc = y, x
                    board.add(Custom(q1), loc=(loc_y, loc_x))
                    board.add(Custom(q2), loc=(loc_y, loc_x - size_quad))
                    board.add(Custom(q3), loc=(loc_y + size_quad, loc_x - size_quad))
                    board.add(Custom(q4), loc=(loc_y + size_quad, loc_x))
            
            # Grid Lines
            fig = board.view()[0]
            for pt in np.arange(0.5, size_tile, 1):
                plt.axvline(pt, lw=1, color='gray', alpha=1)
                plt.axhline(pt, lw=1, color='gray', alpha=1)

            plt.savefig(path + str_matrix + "/tile.png")

        # Data Output and Animated GIF
        if out_txt == True or out_rle == True or out_img_animated:
            # Setup Board
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

            # Output Generation Data to Files
            for i, gen in enumerate(hist):
                # check performance?
                if out_txt:
                    np.savetxt(path + str_matrix + "/gen_" + '{:08}'.format(i) + ".txt", gen, delimiter="", fmt="%d")
                
                if out_rle:
                    with open(path + str_matrix + "/gen_" + '{:08}'.format(i) + ".rle", "w") as file:
                        file.write("x = 0, y = 0, rule = B3/S23\n")
                        file.write(arrayToRLE(gen))
            
            # Animated GIF
            if out_img_animated == True:
                # 250ms
                anim = sim.animate(interval=1)
                anim.save(path + str_matrix + "/animation.gif", fps=4)
        
        # Display
        #plt.show()

    # Print Item Performance to Console
    item_end = time.time()
    str_time = str(round(item_end - item_start, 3)) + "s"
    print(str_time + "\n")

# Print Total Script Elapsed Time to Console
script_end = time.time()
print("Total Elapsed: " + str(round(script_end - script_start, 3)) + "s" + "\n")
