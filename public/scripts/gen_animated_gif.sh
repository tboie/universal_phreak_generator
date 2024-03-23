#!/bin/bash
 
# recursively iterate directory
# command: ./gen_animated_gif [dir]
# output: [dir]/gen_animated.gif
# todo: set gif speed

find $1 -type d -exec ffmpeg -y -f image2 -i "{}/gen_%08d.png" "{}/gen_animated.gif" \;