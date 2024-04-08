#!/bin/bash
 
# recursively iterate directory
# command: ./gen_animated_gif [dir] [framerate]
# output: [dir]/gen_animated.gif
# ex: ./gen_animated_gif.sh "../sequences/gen" 4

find $1 -type d -exec ffmpeg -y -framerate $2 -f image2 -i "{}/gen_%08d.png" "{}/gen_animated.gif" \;