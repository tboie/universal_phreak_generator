#!/bin/bash
 
# recursively iterate directory
# command: ./gen_animated_gif [dir] [framerate]
# output: [dir]/gen_animated.gif

find $1 -type d -exec ffmpeg -y -framerate $2 -f image2 -i "{}gen_%08d.png" "{}gen_animated.gif" \;