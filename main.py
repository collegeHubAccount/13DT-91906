import resistor
import random
# init
exclude = []
with open(f"bands.txt") as f:
    bands = f.readlines()
total_questions = len(bands)
for line in range(len(bands)):
    bands[line] = bands[line][0:-1]

# main
# print(bands)
score = 0
while 1:
    if bands != []:
        band = random.randint(0,(len(bands)-1))
        value = resistor.bandToValue(bands[band])
        print(bands[band])
        # print(f"debug {value}")
        bands.pop(band)
        ans = input("yo gimme a value for this ting: ")
        if int(ans) == value:
            score += 1
    else:
        break
print(f'you got {score} out of {total_questions}')