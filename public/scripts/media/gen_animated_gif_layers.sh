#!/bin/bash

# create transparent animated gif of sequence layer
# output: ../sequences/out/gif/gen_animated_[layer #].gif
# TODO: refactor

ffmpeg -framerate 10 -i ../sequences/out/0/gen_%08d.png -i ../sequences/out/0/palette.png -lavfi paletteuse=alpha_threshold=128 ../sequences/out/gif/gen_animated_0.gif
ffmpeg -framerate 10 -i ../sequences/out/1/gen_%08d.png -i ../sequences/out/1/palette.png -lavfi paletteuse=alpha_threshold=128 ../sequences/out/gif/gen_animated_1.gif
ffmpeg -framerate 10 -i ../sequences/out/2/gen_%08d.png -i ../sequences/out/2/palette.png -lavfi paletteuse=alpha_threshold=128 ../sequences/out/gif/gen_animated_2.gif
ffmpeg -framerate 10 -i ../sequences/out/3/gen_%08d.png -i ../sequences/out/3/palette.png -lavfi paletteuse=alpha_threshold=128 ../sequences/out/gif/gen_animated_3.gif
ffmpeg -framerate 10 -i ../sequences/out/4/gen_%08d.png -i ../sequences/out/4/palette.png -lavfi paletteuse=alpha_threshold=128 ../sequences/out/gif/gen_animated_4.gif
ffmpeg -framerate 10 -i ../sequences/out/5/gen_%08d.png -i ../sequences/out/5/palette.png -lavfi paletteuse=alpha_threshold=128 ../sequences/out/gif/gen_animated_5.gif
ffmpeg -framerate 10 -i ../sequences/out/6/gen_%08d.png -i ../sequences/out/6/palette.png -lavfi paletteuse=alpha_threshold=128 ../sequences/out/gif/gen_animated_6.gif
ffmpeg -framerate 10 -i ../sequences/out/7/gen_%08d.png -i ../sequences/out/7/palette.png -lavfi paletteuse=alpha_threshold=128 ../sequences/out/gif/gen_animated_7.gif
ffmpeg -framerate 10 -i ../sequences/out/8/gen_%08d.png -i ../sequences/out/8/palette.png -lavfi paletteuse=alpha_threshold=128 ../sequences/out/gif/gen_animated_8.gif
ffmpeg -framerate 10 -i ../sequences/out/9/gen_%08d.png -i ../sequences/out/9/palette.png -lavfi paletteuse=alpha_threshold=128 ../sequences/out/gif/gen_animated_9.gif
ffmpeg -framerate 10 -i ../sequences/out/10/gen_%08d.png -i ../sequences/out/10/palette.png -lavfi paletteuse=alpha_threshold=128 ../sequences/out/gif/gen_animated_10.gif
ffmpeg -framerate 10 -i ../sequences/out/11/gen_%08d.png -i ../sequences/out/11/palette.png -lavfi paletteuse=alpha_threshold=128 ../sequences/out/gif/gen_animated_11.gif
ffmpeg -framerate 10 -i ../sequences/out/12/gen_%08d.png -i ../sequences/out/12/palette.png -lavfi paletteuse=alpha_threshold=128 ../sequences/out/gif/gen_animated_12.gif
ffmpeg -framerate 10 -i ../sequences/out/13/gen_%08d.png -i ../sequences/out/13/palette.png -lavfi paletteuse=alpha_threshold=128 ../sequences/out/gif/gen_animated_13.gif
ffmpeg -framerate 10 -i ../sequences/out/14/gen_%08d.png -i ../sequences/out/14/palette.png -lavfi paletteuse=alpha_threshold=128 ../sequences/out/gif/gen_animated_14.gif
ffmpeg -framerate 10 -i ../sequences/out/15/gen_%08d.png -i ../sequences/out/15/palette.png -lavfi paletteuse=alpha_threshold=128 ../sequences/out/gif/gen_animated_15.gif
ffmpeg -framerate 10 -i ../sequences/out/16/gen_%08d.png -i ../sequences/out/16/palette.png -lavfi paletteuse=alpha_threshold=128 ../sequences/out/gif/gen_animated_16.gif
ffmpeg -framerate 10 -i ../sequences/out/17/gen_%08d.png -i ../sequences/out/17/palette.png -lavfi paletteuse=alpha_threshold=128 ../sequences/out/gif/gen_animated_17.gif
ffmpeg -framerate 10 -i ../sequences/out/18/gen_%08d.png -i ../sequences/out/18/palette.png -lavfi paletteuse=alpha_threshold=128 ../sequences/out/gif/gen_animated_18.gif
ffmpeg -framerate 10 -i ../sequences/out/19/gen_%08d.png -i ../sequences/out/19/palette.png -lavfi paletteuse=alpha_threshold=128 ../sequences/out/gif/gen_animated_19.gif
ffmpeg -framerate 10 -i ../sequences/out/20/gen_%08d.png -i ../sequences/out/20/palette.png -lavfi paletteuse=alpha_threshold=128 ../sequences/out/gif/gen_animated_20.gif
ffmpeg -framerate 10 -i ../sequences/out/21/gen_%08d.png -i ../sequences/out/21/palette.png -lavfi paletteuse=alpha_threshold=128 ../sequences/out/gif/gen_animated_21.gif
ffmpeg -framerate 10 -i ../sequences/out/22/gen_%08d.png -i ../sequences/out/22/palette.png -lavfi paletteuse=alpha_threshold=128 ../sequences/out/gif/gen_animated_22.gif
ffmpeg -framerate 10 -i ../sequences/out/23/gen_%08d.png -i ../sequences/out/23/palette.png -lavfi paletteuse=alpha_threshold=128 ../sequences/out/gif/gen_animated_23.gif
ffmpeg -framerate 10 -i ../sequences/out/24/gen_%08d.png -i ../sequences/out/24/palette.png -lavfi paletteuse=alpha_threshold=128 ../sequences/out/gif/gen_animated_24.gif
ffmpeg -framerate 10 -i ../sequences/out/25/gen_%08d.png -i ../sequences/out/25/palette.png -lavfi paletteuse=alpha_threshold=128 ../sequences/out/gif/gen_animated_25.gif
ffmpeg -framerate 10 -i ../sequences/out/26/gen_%08d.png -i ../sequences/out/26/palette.png -lavfi paletteuse=alpha_threshold=128 ../sequences/out/gif/gen_animated_26.gif
ffmpeg -framerate 10 -i ../sequences/out/27/gen_%08d.png -i ../sequences/out/27/palette.png -lavfi paletteuse=alpha_threshold=128 ../sequences/out/gif/gen_animated_27.gif
ffmpeg -framerate 10 -i ../sequences/out/28/gen_%08d.png -i ../sequences/out/28/palette.png -lavfi paletteuse=alpha_threshold=128 ../sequences/out/gif/gen_animated_28.gif
ffmpeg -framerate 10 -i ../sequences/out/29/gen_%08d.png -i ../sequences/out/29/palette.png -lavfi paletteuse=alpha_threshold=128 ../sequences/out/gif/gen_animated_29.gif
ffmpeg -framerate 10 -i ../sequences/out/30/gen_%08d.png -i ../sequences/out/30/palette.png -lavfi paletteuse=alpha_threshold=128 ../sequences/out/gif/gen_animated_30.gif
ffmpeg -framerate 10 -i ../sequences/out/31/gen_%08d.png -i ../sequences/out/31/palette.png -lavfi paletteuse=alpha_threshold=128 ../sequences/out/gif/gen_animated_31.gif
ffmpeg -framerate 10 -i ../sequences/out/32/gen_%08d.png -i ../sequences/out/32/palette.png -lavfi paletteuse=alpha_threshold=128 ../sequences/out/gif/gen_animated_32.gif
: <<'END'
ffmpeg -framerate 10 -i ../sequences/out/33/gen_%08d.png -i ../sequences/out/33/palette.png -lavfi paletteuse=alpha_threshold=128 ../sequences/out/gif/gen_animated_33.gif
ffmpeg -framerate 10 -i ../sequences/out/34/gen_%08d.png -i ../sequences/out/34/palette.png -lavfi paletteuse=alpha_threshold=128 ../sequences/out/gif/gen_animated_34.gif
ffmpeg -framerate 10 -i ../sequences/out/35/gen_%08d.png -i ../sequences/out/35/palette.png -lavfi paletteuse=alpha_threshold=128 ../sequences/out/gif/gen_animated_35.gif
ffmpeg -framerate 10 -i ../sequences/out/36/gen_%08d.png -i ../sequences/out/36/palette.png -lavfi paletteuse=alpha_threshold=128 ../sequences/out/gif/gen_animated_36.gif
ffmpeg -framerate 10 -i ../sequences/out/37/gen_%08d.png -i ../sequences/out/37/palette.png -lavfi paletteuse=alpha_threshold=128 ../sequences/out/gif/gen_animated_37.gif
ffmpeg -framerate 10 -i ../sequences/out/38/gen_%08d.png -i ../sequences/out/38/palette.png -lavfi paletteuse=alpha_threshold=128 ../sequences/out/gif/gen_animated_38.gif
ffmpeg -framerate 10 -i ../sequences/out/39/gen_%08d.png -i ../sequences/out/39/palette.png -lavfi paletteuse=alpha_threshold=128 ../sequences/out/gif/gen_animated_39.gif
ffmpeg -framerate 10 -i ../sequences/out/40/gen_%08d.png -i ../sequences/out/40/palette.png -lavfi paletteuse=alpha_threshold=128 ../sequences/out/gif/gen_animated_40.gif
ffmpeg -framerate 10 -i ../sequences/out/41/gen_%08d.png -i ../sequences/out/41/palette.png -lavfi paletteuse=alpha_threshold=128 ../sequences/out/gif/gen_animated_41.gif
ffmpeg -framerate 10 -i ../sequences/out/42/gen_%08d.png -i ../sequences/out/42/palette.png -lavfi paletteuse=alpha_threshold=128 ../sequences/out/gif/gen_animated_42.gif
ffmpeg -framerate 10 -i ../sequences/out/43/gen_%08d.png -i ../sequences/out/43/palette.png -lavfi paletteuse=alpha_threshold=128 ../sequences/out/gif/gen_animated_43.gif
ffmpeg -framerate 10 -i ../sequences/out/44/gen_%08d.png -i ../sequences/out/44/palette.png -lavfi paletteuse=alpha_threshold=128 ../sequences/out/gif/gen_animated_44.gif
ffmpeg -framerate 10 -i ../sequences/out/45/gen_%08d.png -i ../sequences/out/45/palette.png -lavfi paletteuse=alpha_threshold=128 ../sequences/out/gif/gen_animated_45.gif
ffmpeg -framerate 10 -i ../sequences/out/46/gen_%08d.png -i ../sequences/out/46/palette.png -lavfi paletteuse=alpha_threshold=128 ../sequences/out/gif/gen_animated_46.gif
ffmpeg -framerate 10 -i ../sequences/out/47/gen_%08d.png -i ../sequences/out/47/palette.png -lavfi paletteuse=alpha_threshold=128 ../sequences/out/gif/gen_animated_47.gif
ffmpeg -framerate 10 -i ../sequences/out/48/gen_%08d.png -i ../sequences/out/48/palette.png -lavfi paletteuse=alpha_threshold=128 ../sequences/out/gif/gen_animated_48.gif
ffmpeg -framerate 10 -i ../sequences/out/49/gen_%08d.png -i ../sequences/out/49/palette.png -lavfi paletteuse=alpha_threshold=128 ../sequences/out/gif/gen_animated_49.gif
ffmpeg -framerate 10 -i ../sequences/out/50/gen_%08d.png -i ../sequences/out/50/palette.png -lavfi paletteuse=alpha_threshold=128 ../sequences/out/gif/gen_animated_50.gif
ffmpeg -framerate 10 -i ../sequences/out/51/gen_%08d.png -i ../sequences/out/51/palette.png -lavfi paletteuse=alpha_threshold=128 ../sequences/out/gif/gen_animated_51.gif
ffmpeg -framerate 10 -i ../sequences/out/52/gen_%08d.png -i ../sequences/out/52/palette.png -lavfi paletteuse=alpha_threshold=128 ../sequences/out/gif/gen_animated_52.gif
ffmpeg -framerate 10 -i ../sequences/out/53/gen_%08d.png -i ../sequences/out/53/palette.png -lavfi paletteuse=alpha_threshold=128 ../sequences/out/gif/gen_animated_53.gif
ffmpeg -framerate 10 -i ../sequences/out/54/gen_%08d.png -i ../sequences/out/54/palette.png -lavfi paletteuse=alpha_threshold=128 ../sequences/out/gif/gen_animated_54.gif
ffmpeg -framerate 10 -i ../sequences/out/55/gen_%08d.png -i ../sequences/out/55/palette.png -lavfi paletteuse=alpha_threshold=128 ../sequences/out/gif/gen_animated_55.gif
ffmpeg -framerate 10 -i ../sequences/out/56/gen_%08d.png -i ../sequences/out/56/palette.png -lavfi paletteuse=alpha_threshold=128 ../sequences/out/gif/gen_animated_56.gif
ffmpeg -framerate 10 -i ../sequences/out/57/gen_%08d.png -i ../sequences/out/57/palette.png -lavfi paletteuse=alpha_threshold=128 ../sequences/out/gif/gen_animated_57.gif
ffmpeg -framerate 10 -i ../sequences/out/58/gen_%08d.png -i ../sequences/out/58/palette.png -lavfi paletteuse=alpha_threshold=128 ../sequences/out/gif/gen_animated_58.gif
ffmpeg -framerate 10 -i ../sequences/out/59/gen_%08d.png -i ../sequences/out/59/palette.png -lavfi paletteuse=alpha_threshold=128 ../sequences/out/gif/gen_animated_59.gif
ffmpeg -framerate 10 -i ../sequences/out/60/gen_%08d.png -i ../sequences/out/60/palette.png -lavfi paletteuse=alpha_threshold=128 ../sequences/out/gif/gen_animated_60.gif
ffmpeg -framerate 10 -i ../sequences/out/61/gen_%08d.png -i ../sequences/out/61/palette.png -lavfi paletteuse=alpha_threshold=128 ../sequences/out/gif/gen_animated_61.gif
ffmpeg -framerate 10 -i ../sequences/out/62/gen_%08d.png -i ../sequences/out/62/palette.png -lavfi paletteuse=alpha_threshold=128 ../sequences/out/gif/gen_animated_62.gif
ffmpeg -framerate 10 -i ../sequences/out/63/gen_%08d.png -i ../sequences/out/63/palette.png -lavfi paletteuse=alpha_threshold=128 ../sequences/out/gif/gen_animated_63.gif
ffmpeg -framerate 10 -i ../sequences/out/64/gen_%08d.png -i ../sequences/out/64/palette.png -lavfi paletteuse=alpha_threshold=128 ../sequences/out/gif/gen_animated_64.gif
END 
