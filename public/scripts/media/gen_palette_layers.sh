#!/bin/bash

# creates transparency palette file for sequence layer
# output: ../sequences/out/[layer #]/palette.png
# TODO: refactor
# only 1 palette needed for same color?

ffmpeg -i ../sequences/out/0/gen_%08d.png -vf palettegen=reserve_transparent=1 ../sequences/out/0/palette.png
ffmpeg -i ../sequences/out/1/gen_%08d.png -vf palettegen=reserve_transparent=1 ../sequences/out/1/palette.png
ffmpeg -i ../sequences/out/2/gen_%08d.png -vf palettegen=reserve_transparent=1 ../sequences/out/2/palette.png
ffmpeg -i ../sequences/out/3/gen_%08d.png -vf palettegen=reserve_transparent=1 ../sequences/out/3/palette.png
ffmpeg -i ../sequences/out/4/gen_%08d.png -vf palettegen=reserve_transparent=1 ../sequences/out/4/palette.png
ffmpeg -i ../sequences/out/5/gen_%08d.png -vf palettegen=reserve_transparent=1 ../sequences/out/5/palette.png
ffmpeg -i ../sequences/out/6/gen_%08d.png -vf palettegen=reserve_transparent=1 ../sequences/out/6/palette.png
ffmpeg -i ../sequences/out/7/gen_%08d.png -vf palettegen=reserve_transparent=1 ../sequences/out/7/palette.png
ffmpeg -i ../sequences/out/8/gen_%08d.png -vf palettegen=reserve_transparent=1 ../sequences/out/8/palette.png
ffmpeg -i ../sequences/out/9/gen_%08d.png -vf palettegen=reserve_transparent=1 ../sequences/out/9/palette.png
ffmpeg -i ../sequences/out/10/gen_%08d.png -vf palettegen=reserve_transparent=1 ../sequences/out/10/palette.png
ffmpeg -i ../sequences/out/11/gen_%08d.png -vf palettegen=reserve_transparent=1 ../sequences/out/11/palette.png
ffmpeg -i ../sequences/out/12/gen_%08d.png -vf palettegen=reserve_transparent=1 ../sequences/out/12/palette.png
ffmpeg -i ../sequences/out/13/gen_%08d.png -vf palettegen=reserve_transparent=1 ../sequences/out/13/palette.png
ffmpeg -i ../sequences/out/14/gen_%08d.png -vf palettegen=reserve_transparent=1 ../sequences/out/14/palette.png
ffmpeg -i ../sequences/out/15/gen_%08d.png -vf palettegen=reserve_transparent=1 ../sequences/out/15/palette.png
ffmpeg -i ../sequences/out/16/gen_%08d.png -vf palettegen=reserve_transparent=1 ../sequences/out/16/palette.png
ffmpeg -i ../sequences/out/17/gen_%08d.png -vf palettegen=reserve_transparent=1 ../sequences/out/17/palette.png
ffmpeg -i ../sequences/out/18/gen_%08d.png -vf palettegen=reserve_transparent=1 ../sequences/out/18/palette.png
ffmpeg -i ../sequences/out/19/gen_%08d.png -vf palettegen=reserve_transparent=1 ../sequences/out/19/palette.png
ffmpeg -i ../sequences/out/20/gen_%08d.png -vf palettegen=reserve_transparent=1 ../sequences/out/20/palette.png
ffmpeg -i ../sequences/out/21/gen_%08d.png -vf palettegen=reserve_transparent=1 ../sequences/out/21/palette.png
ffmpeg -i ../sequences/out/22/gen_%08d.png -vf palettegen=reserve_transparent=1 ../sequences/out/22/palette.png
ffmpeg -i ../sequences/out/23/gen_%08d.png -vf palettegen=reserve_transparent=1 ../sequences/out/23/palette.png
ffmpeg -i ../sequences/out/24/gen_%08d.png -vf palettegen=reserve_transparent=1 ../sequences/out/24/palette.png
ffmpeg -i ../sequences/out/25/gen_%08d.png -vf palettegen=reserve_transparent=1 ../sequences/out/25/palette.png
ffmpeg -i ../sequences/out/26/gen_%08d.png -vf palettegen=reserve_transparent=1 ../sequences/out/26/palette.png
ffmpeg -i ../sequences/out/27/gen_%08d.png -vf palettegen=reserve_transparent=1 ../sequences/out/27/palette.png
ffmpeg -i ../sequences/out/28/gen_%08d.png -vf palettegen=reserve_transparent=1 ../sequences/out/28/palette.png
ffmpeg -i ../sequences/out/29/gen_%08d.png -vf palettegen=reserve_transparent=1 ../sequences/out/29/palette.png
ffmpeg -i ../sequences/out/30/gen_%08d.png -vf palettegen=reserve_transparent=1 ../sequences/out/30/palette.png
ffmpeg -i ../sequences/out/31/gen_%08d.png -vf palettegen=reserve_transparent=1 ../sequences/out/31/palette.png
ffmpeg -i ../sequences/out/32/gen_%08d.png -vf palettegen=reserve_transparent=1 ../sequences/out/32/palette.png
: <<'END'
ffmpeg -i ../sequences/out/33/gen_%08d.png -vf palettegen=reserve_transparent=1 ../sequences/out/33/palette.png
ffmpeg -i ../sequences/out/34/gen_%08d.png -vf palettegen=reserve_transparent=1 ../sequences/out/34/palette.png
ffmpeg -i ../sequences/out/35/gen_%08d.png -vf palettegen=reserve_transparent=1 ../sequences/out/35/palette.png
ffmpeg -i ../sequences/out/36/gen_%08d.png -vf palettegen=reserve_transparent=1 ../sequences/out/36/palette.png
ffmpeg -i ../sequences/out/37/gen_%08d.png -vf palettegen=reserve_transparent=1 ../sequences/out/37/palette.png
ffmpeg -i ../sequences/out/38/gen_%08d.png -vf palettegen=reserve_transparent=1 ../sequences/out/38/palette.png
ffmpeg -i ../sequences/out/39/gen_%08d.png -vf palettegen=reserve_transparent=1 ../sequences/out/39/palette.png
ffmpeg -i ../sequences/out/40/gen_%08d.png -vf palettegen=reserve_transparent=1 ../sequences/out/40/palette.png
ffmpeg -i ../sequences/out/41/gen_%08d.png -vf palettegen=reserve_transparent=1 ../sequences/out/41/palette.png
ffmpeg -i ../sequences/out/42/gen_%08d.png -vf palettegen=reserve_transparent=1 ../sequences/out/42/palette.png
ffmpeg -i ../sequences/out/43/gen_%08d.png -vf palettegen=reserve_transparent=1 ../sequences/out/43/palette.png
ffmpeg -i ../sequences/out/44/gen_%08d.png -vf palettegen=reserve_transparent=1 ../sequences/out/44/palette.png
ffmpeg -i ../sequences/out/45/gen_%08d.png -vf palettegen=reserve_transparent=1 ../sequences/out/45/palette.png
ffmpeg -i ../sequences/out/46/gen_%08d.png -vf palettegen=reserve_transparent=1 ../sequences/out/46/palette.png
ffmpeg -i ../sequences/out/47/gen_%08d.png -vf palettegen=reserve_transparent=1 ../sequences/out/47/palette.png
ffmpeg -i ../sequences/out/48/gen_%08d.png -vf palettegen=reserve_transparent=1 ../sequences/out/48/palette.png
ffmpeg -i ../sequences/out/49/gen_%08d.png -vf palettegen=reserve_transparent=1 ../sequences/out/49/palette.png
ffmpeg -i ../sequences/out/50/gen_%08d.png -vf palettegen=reserve_transparent=1 ../sequences/out/50/palette.png
ffmpeg -i ../sequences/out/51/gen_%08d.png -vf palettegen=reserve_transparent=1 ../sequences/out/51/palette.png
ffmpeg -i ../sequences/out/52/gen_%08d.png -vf palettegen=reserve_transparent=1 ../sequences/out/52/palette.png
ffmpeg -i ../sequences/out/53/gen_%08d.png -vf palettegen=reserve_transparent=1 ../sequences/out/53/palette.png
ffmpeg -i ../sequences/out/54/gen_%08d.png -vf palettegen=reserve_transparent=1 ../sequences/out/54/palette.png
ffmpeg -i ../sequences/out/55/gen_%08d.png -vf palettegen=reserve_transparent=1 ../sequences/out/55/palette.png
ffmpeg -i ../sequences/out/56/gen_%08d.png -vf palettegen=reserve_transparent=1 ../sequences/out/56/palette.png
ffmpeg -i ../sequences/out/57/gen_%08d.png -vf palettegen=reserve_transparent=1 ../sequences/out/57/palette.png
ffmpeg -i ../sequences/out/58/gen_%08d.png -vf palettegen=reserve_transparent=1 ../sequences/out/58/palette.png
ffmpeg -i ../sequences/out/59/gen_%08d.png -vf palettegen=reserve_transparent=1 ../sequences/out/59/palette.png
ffmpeg -i ../sequences/out/60/gen_%08d.png -vf palettegen=reserve_transparent=1 ../sequences/out/60/palette.png
ffmpeg -i ../sequences/out/61/gen_%08d.png -vf palettegen=reserve_transparent=1 ../sequences/out/61/palette.png
ffmpeg -i ../sequences/out/62/gen_%08d.png -vf palettegen=reserve_transparent=1 ../sequences/out/62/palette.png
ffmpeg -i ../sequences/out/63/gen_%08d.png -vf palettegen=reserve_transparent=1 ../sequences/out/63/palette.png
ffmpeg -i ../sequences/out/64/gen_%08d.png -vf palettegen=reserve_transparent=1 ../sequences/out/64/palette.png
END
