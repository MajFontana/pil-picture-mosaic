import os
import pickle
import random
from PIL import Image

SCALE = 40
PALETTE = "PALETTE/"
BLUEPRINT = "blueprint.png"
TARGET = "result.png"
RESAMP = Image.LANCZOS
ROTATE = False

path = os.path.join(PALETTE, "palette.pickle")
with open(path, "rb") as f:
    palette = pickle.load(f)
blueprint = Image.open("blueprint.png")

print("Generating image ...")
newres = [blueprint.size[i] * SCALE for i in range(2)]
tilesize = (SCALE, SCALE)

img = Image.new("RGB", newres)
for y in range(blueprint.height):
    for x in range(blueprint.width):
        pixel = blueprint.getpixel((x, y))
        path = palette[pixel][0]
        tile = Image.open(path).resize(tilesize, RESAMP)
        if ROTATE:
            angle = random.randint(0, 3) * 90
            tile = tile.rotate(angle)
        pos = (x * SCALE, y * SCALE)
        img.paste(tile, pos)
img.save(TARGET)

print("Finished")
