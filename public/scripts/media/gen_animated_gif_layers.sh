# create transparent animated gif of sequence layer
# output: ../sequences/gif/gen_animated_[layer #].gif
# TODO: refactor

ffmpeg -framerate 10 -i ../sequences/0/gen_%08d.png -i ../sequences/0/palette.png -lavfi paletteuse=alpha_threshold=128 ../sequences/gif/gen_animated_0.gif
ffmpeg -framerate 10 -i ../sequences/1/gen_%08d.png -i ../sequences/1/palette.png -lavfi paletteuse=alpha_threshold=128 ../sequences/gif/gen_animated_1.gif
ffmpeg -framerate 10 -i ../sequences/2/gen_%08d.png -i ../sequences/2/palette.png -lavfi paletteuse=alpha_threshold=128 ../sequences/gif/gen_animated_2.gif
ffmpeg -framerate 10 -i ../sequences/3/gen_%08d.png -i ../sequences/3/palette.png -lavfi paletteuse=alpha_threshold=128 ../sequences/gif/gen_animated_3.gif
ffmpeg -framerate 10 -i ../sequences/4/gen_%08d.png -i ../sequences/4/palette.png -lavfi paletteuse=alpha_threshold=128 ../sequences/gif/gen_animated_4.gif
ffmpeg -framerate 10 -i ../sequences/5/gen_%08d.png -i ../sequences/5/palette.png -lavfi paletteuse=alpha_threshold=128 ../sequences/gif/gen_animated_5.gif
ffmpeg -framerate 10 -i ../sequences/6/gen_%08d.png -i ../sequences/6/palette.png -lavfi paletteuse=alpha_threshold=128 ../sequences/gif/gen_animated_6.gif
ffmpeg -framerate 10 -i ../sequences/7/gen_%08d.png -i ../sequences/7/palette.png -lavfi paletteuse=alpha_threshold=128 ../sequences/gif/gen_animated_7.gif
ffmpeg -framerate 10 -i ../sequences/8/gen_%08d.png -i ../sequences/8/palette.png -lavfi paletteuse=alpha_threshold=128 ../sequences/gif/gen_animated_8.gif
ffmpeg -framerate 10 -i ../sequences/9/gen_%08d.png -i ../sequences/9/palette.png -lavfi paletteuse=alpha_threshold=128 ../sequences/gif/gen_animated_9.gif
ffmpeg -framerate 10 -i ../sequences/10/gen_%08d.png -i ../sequences/10/palette.png -lavfi paletteuse=alpha_threshold=128 ../sequences/gif/gen_animated_10.gif
ffmpeg -framerate 10 -i ../sequences/11/gen_%08d.png -i ../sequences/11/palette.png -lavfi paletteuse=alpha_threshold=128 ../sequences/gif/gen_animated_11.gif
ffmpeg -framerate 10 -i ../sequences/12/gen_%08d.png -i ../sequences/12/palette.png -lavfi paletteuse=alpha_threshold=128 ../sequences/gif/gen_animated_12.gif
ffmpeg -framerate 10 -i ../sequences/13/gen_%08d.png -i ../sequences/13/palette.png -lavfi paletteuse=alpha_threshold=128 ../sequences/gif/gen_animated_13.gif
ffmpeg -framerate 10 -i ../sequences/14/gen_%08d.png -i ../sequences/14/palette.png -lavfi paletteuse=alpha_threshold=128 ../sequences/gif/gen_animated_14.gif
ffmpeg -framerate 10 -i ../sequences/15/gen_%08d.png -i ../sequences/15/palette.png -lavfi paletteuse=alpha_threshold=128 ../sequences/gif/gen_animated_15.gif
ffmpeg -framerate 10 -i ../sequences/16/gen_%08d.png -i ../sequences/16/palette.png -lavfi paletteuse=alpha_threshold=128 ../sequences/gif/gen_animated_16.gif
