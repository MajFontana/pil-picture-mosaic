# pil-picture-mosaic
A project that lets you render an image as a mosaic of many smaller images

# How to use #
1. `create_palette.py`
    1. Create the `TARGET` (`./PALETTE/`) directory
    2. Edit the `SOURCES` variable to include the directories you wish the program takes photos from
    3. Run the script (run it whenever there are new images in the directories)
2. `convert_image.py`
    1. Edit the `IMAGE` variable to choose which image file to convert to a mosaic
    2. Edit the `MINRES` variable to choose how many mosaic tiles the shortest side of the image should consist of
    3. Run the script
    4. `Preview.png` shows a flat-shaded version of the mosaic, useful for adjusting the `MINRES` resolution
3. `render_image.py`
    1. Edit the `SCALE` variable to choose the resolution of each mosaic tile
    2. Run the script
    3. Result is stored in `result.png`
