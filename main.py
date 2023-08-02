import random
import application
import tkinter as tk

# functions
def bandToValue(order) -> None:
    multi = 10**int(str(order)[-1])
    ans = int(str(order)[0:-1])*multi
    return int(ans)

def importer(file):
    with open(f"{file}") as f:
        bands = f.readlines()
    for line in range(len(bands)):
        bands[line] = bands[line][0:-1]
    total_questions = len(bands)
    data = [bands, total_questions]
    return data


if __name__ == "__main__":
    # init
    exclude = []
    bands = importer("bands.txt")
    total_questions = bands[1]
    bands = bands[0]
    score = 0

    app = application.App()
    

    # prog loop
    # while 1:
    #     if bands != []:
    #         band = random.randint(0,(len(bands)-1))
    #         value = bandToValue(bands[band])
    #         print(bands[band])
    #         # print(f"debug {value}")
    #         bands.pop(band)
    #         ans = input("yo gimme a value for this ting: ")
    #         if int(ans) == value:
    #             print("correct!")
    #             score += 1
    #         else:
    #             print(f"nice try the correct values was {value}")
    #     else:
    #         break
    # # final score display
    # print(f'you got {score} out of {total_questions}')
    app.draw(app.canvas, app.x1, app.y1, app.x2, app.y2, 
                 "red", "green", "purple", "yellow")
    app.ready(app.canvas)
    app.mainloop()