import os
import pickle
import random
from PIL import Image

IMAGE = "flock/HIRES/KittyHawk_E3_withLogo_001-1.jpg"
PALETTE = "PALETTE/"
MINRES = 35
RESAMP = Image.LANCZOS
PREVIEW_SCALE = 20
BLUEPRINT = "blueprint.png"
PREVIEW = "preview.png"
COOLDOWN = 1
RANDOMIZE_NOISE = True

path = os.path.join(PALETTE, "palette.pickle")
with open(path, "rb") as f:
    palette = pickle.load(f)
colors = list(palette.keys())

print("Processing image ...")
img = Image.open(IMAGE)
side = min(img.size)
newres = [int(img.size[i] / side * MINRES) for i in range(2)]
img = img.resize(newres, RESAMP)

if COOLDOWN:
    hist = [None] * COOLDOWN
bp = Image.new("RGB", newres)
for y in range(newres[1]):
    for x in range(newres[0]):
        pixel = img.getpixel((x, y))
        deltas = [sum([abs(pixel[i] - color[i]) for i in range(3)]) / 3 for color in colors]
        
        while True:
            idx = deltas.index(min(deltas))
            mapped = colors[idx]
            if COOLDOWN and mapped in hist:
                deltas[idx] = float("inf")
            else:
                break
        bp.putpixel((x, y), mapped)
        if COOLDOWN:
            if not RANDOMIZE_NOISE or random.randint(0, 1):
                hist.pop(0)
                hist.append(mapped)
        
bp.save(BLUEPRINT)

prevsize = [newres[i] * PREVIEW_SCALE for i in range(2)]
bp = bp.resize(prevsize, Image.NEAREST)
bp.save(PREVIEW)

print("Finished")
