sequence layers concept
(verify paths and configs in scripts)

TODO: refactor

set config in gen_rotating_square_layers.py and gen_images_layers.py
update gen_palette_layers.sh and gen_animated_gif_layers.sh to match config

cd sequences
python3.9 gen_rotating_square_layers.py

cd media
python3.9 gen_images_layers.py
./gen_palette_layers.sh
./gen_animated_gif_layers.sh

use html to display overlapping animated gifs
copy all gen_animated_[layer #].gif from /sequences/gif to /media/html_layers
update index.html in /media/html_layers

run html server to view:
serve -s /media/html_layers

use tool to capture screen
use tool to convert movie to gif

------------------
sequence concept:
(verify paths and configs in scripts)

/sequences/gen_rotating_square.py and /sequences/gen_custom_seq.py
/media/gen_images.py
/media/gen_animated_gif.sh [dir] [framerate]

----------------
tesselated tiles concept:

/tiles/gen_tile_seq.py
/media/gen_graph.py

----------------
locality diagram concept:

all in /locality_diagrams/
