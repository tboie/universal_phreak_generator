#
# generate animated gif for each nested directory with images
#

from PIL import Image, ImageDraw
from pathlib import Path
import os, time

path = "tile_3x3/"
ext = "png"
size = 400

# get all directories
dirs = []
for p in sorted(Path(path).rglob('*.' + ext)):
    path = os.path.dirname(p)

    if path not in dirs:
        dirs.append(path)

# created animated gif for each directory
i = 0
for dir in dirs:
    timer_start = time.time()

    imgs = []
    for p in sorted(Path(dir).rglob('*.' + ext)):
        imgs.append(Image.open(p))

    imgs[0].save(dir + "/gen_animated.gif", save_all=True, append_images=imgs[1:], duration=100, loop=0)
    
    timer_end = time.time()
    timer_str = str("{:.3f}".format(round(timer_end - timer_start, 3))) + "s"
    
    i += 1
    print(str(i) + "/" + str(len(dirs)) + " " + timer_str + " " + str(dir))

print("Finished")