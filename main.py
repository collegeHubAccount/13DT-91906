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


def display():
    global bands, value, run
    colours = ['black', 'brown', 'red', 'orange', 'yellow', 
               'green', 'blue', 'violet', 'grey', 'white']
    if bands != []:
        band = random.randint(0,(len(bands)-1))
        value = bandToValue(bands[band])
        app.draw(app.canvas, app.x1, app.y1, app.x2, app.y2, 
                    colours[int(str(bands[band])[0])], 
                    colours[int(str(bands[band])[1])], 
                    colours[int(str(bands[band])[2])], 
                    colours[int(str(bands[band])[3])])
        bands.pop(band)
    else:
        run = False


def confirm(event=None):
    global score
    if run:
        app.ans = app.entry.get()
        if int(app.ans) == value:
            print("correct!")
            score += 1
        else:
            print(f"nice try the correct values was {value}")
        # final score display
        display()
    else:
        print(f"total score: {score}")


if __name__ == "__main__":
    # init
    exclude = []
    bands = importer("bands.txt")
    total_questions = bands[1]
    bands = bands[0]
    score = 0
    run = True
    app = application.App()
    app.ready()
    app.bind('<Return>', confirm)
    display()
    app.mainloop()