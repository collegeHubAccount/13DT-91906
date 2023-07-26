import resistor
import random
# init
exclude = []
with open(f"bands.txt") as f:
    bands = f.readlines()
for line in range(len(bands)):
    bands[line] = bands[line][0:-1]

# main
print(bands)
while 1:
    if bands != []:
        band = random.randint(0,(len(bands)-1))
        value = resistor.bandToValue(bands[band])
        bands.pop(band)
        print(value)
    else:
        break
print("program complete")