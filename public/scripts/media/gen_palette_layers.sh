# creates transparency palette file for sequence layer
# output: ../sequences/[layer #]/palette.png
# TODO: refactor

ffmpeg -i ../sequences/0/gen_%08d.png -vf palettegen=reserve_transparent=1 ../sequences/0/palette.png
ffmpeg -i ../sequences/1/gen_%08d.png -vf palettegen=reserve_transparent=1 ../sequences/1/palette.png
ffmpeg -i ../sequences/2/gen_%08d.png -vf palettegen=reserve_transparent=1 ../sequences/2/palette.png
ffmpeg -i ../sequences/3/gen_%08d.png -vf palettegen=reserve_transparent=1 ../sequences/3/palette.png
ffmpeg -i ../sequences/4/gen_%08d.png -vf palettegen=reserve_transparent=1 ../sequences/4/palette.png
ffmpeg -i ../sequences/5/gen_%08d.png -vf palettegen=reserve_transparent=1 ../sequences/5/palette.png
ffmpeg -i ../sequences/6/gen_%08d.png -vf palettegen=reserve_transparent=1 ../sequences/6/palette.png
ffmpeg -i ../sequences/7/gen_%08d.png -vf palettegen=reserve_transparent=1 ../sequences/7/palette.png
ffmpeg -i ../sequences/8/gen_%08d.png -vf palettegen=reserve_transparent=1 ../sequences/8/palette.png
ffmpeg -i ../sequences/9/gen_%08d.png -vf palettegen=reserve_transparent=1 ../sequences/9/palette.png
ffmpeg -i ../sequences/10/gen_%08d.png -vf palettegen=reserve_transparent=1 ../sequences/10/palette.png
ffmpeg -i ../sequences/11/gen_%08d.png -vf palettegen=reserve_transparent=1 ../sequences/11/palette.png
ffmpeg -i ../sequences/12/gen_%08d.png -vf palettegen=reserve_transparent=1 ../sequences/12/palette.png
ffmpeg -i ../sequences/13/gen_%08d.png -vf palettegen=reserve_transparent=1 ../sequences/13/palette.png
ffmpeg -i ../sequences/14/gen_%08d.png -vf palettegen=reserve_transparent=1 ../sequences/14/palette.png
ffmpeg -i ../sequences/15/gen_%08d.png -vf palettegen=reserve_transparent=1 ../sequences/15/palette.png
ffmpeg -i ../sequences/16/gen_%08d.png -vf palettegen=reserve_transparent=1 ../sequences/16/palette.png
