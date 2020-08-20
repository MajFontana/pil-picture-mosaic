import os
import pickle
from PIL import Image

SOURCES = ("flock/LOWRES/", "flock/FULLHD/", "flock/HIRES/")
RES = 128
TILE_RESAMP = Image.LANCZOS
AVERAGE_RESAMP = Image.LANCZOS
TARGET = "PALETTE/"

newsize = (RES, RES)
palette = {}

idx = 0
for dr in SOURCES:
    for file in os.listdir(dr):
        
        path = os.path.abspath(os.path.join(dr, file))
        try:
            img = Image.open(path)
        except OSError:
            continue
        print("Processing %s ..." % file)
        
        side = min(img.size)
        topleft = [(img.size[i] - side) // 2 for i in range(2)]
        square = (topleft[0], topleft[1], topleft[0] + side, topleft[1] + side)
        img = img.resize(newsize, TILE_RESAMP, square).convert("RGB")
        newname = "%i.png" % idx
        newpath = os.path.abspath(os.path.join(TARGET, newname))
        img.save(newpath)

        img = img.resize((1, 1), AVERAGE_RESAMP)
        col = img.getpixel((0, 0))
        entry = (newpath, path)
        palette[col] = entry
        
        idx += 1

print("Storing the palette ...")
path = os.path.join(TARGET, "palette.pickle")
with open(path, "wb") as f:
    pickle.dump(palette, f)

print("Finished")
