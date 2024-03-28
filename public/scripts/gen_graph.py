# problem: what size area should be used to capture display
# display of tesselation reaction?
#
# potential solution: get min x/y values of pattern for each
# generation to plot on line graph

import numpy as np
import pandas as pd
import plotly.graph_objects as go

from pathlib import Path
import os, time, math

pd.set_option('display.max_colwidth', None)

path = "tile_3x3/tess_2x2/gen_256"

def read_text_file(filename):
    array2D = []
    with open(filename, 'r') as file:
        for line in file:
            # Split the line by whitespace and convert to integers
            row = [int(c) for c in line.replace("\n", "")]
            array2D.append(row)
    return array2D

data = []
for root, dirs, files in os.walk(path):
        for folder in dirs:
            path_pattern = path + "/" + folder

            p_minY = []
            for i, p in enumerate(sorted(Path(path_pattern).rglob('*.txt'))):
                print(p)
                d = np.array(read_text_file(p))
                # print(pd.DataFrame(d))

                minY = len(d) / 2
                minX = 0
                coordinates = np.argwhere(d == 1)
                if len(coordinates) > 0:
                    x_values = coordinates[:, 0]  # Extract x-values
                    y_values = coordinates[:, 1]  # Extract y-values
                    
                    # assuming symmetrical form
                    # max_x_index = np.argmax(x_values)
                    min_x_index = np.argmin(x_values)
                    min_y_index = np.argmin(y_values)

                    minX = coordinates[min_x_index][0]
                    minY = coordinates[min_y_index][1]         
                
                # todo: precision?
                dist = (len(d) / 2) - minY
                p_minY.append(dist)

            data.append({
                "name": folder,
                "dist": p_minY,
            })

# line graph
fig = go.Figure()
for row in data:
    fig.add_trace(go.Scatter(
        y = row["dist"],
        name = row["name"]
    ))
fig.show()