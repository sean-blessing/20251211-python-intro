# for loops
# perform 21 times, 0 to 20
for x in range(21):
    print(x)

# 20 times, 1 to 20
for x in range(1,21):
    print("x:", x)

# interst rates 0.5 to 5.0, step .5
import numpy as np
for x in np.arange(.5,5.1,.5):
    print(f"x = {x}")

colors = ["red", "blue", "yellow", "green"]
for c in colors:
    print(f"color {c}")

for i, color in enumerate(colors):
    print(f"i{i}: {color}")