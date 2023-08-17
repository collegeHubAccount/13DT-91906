import random
import application
import tkinter as tk

# functions


def bandToValue(order) -> None:
    if str(order)[-1] == 'a':
        multi = 10 ** -1
    elif str(order)[-1] == 'b':
        multi = 10 ** -2
    else:
        multi = 10 ** int(str(order)[-1])
    ans = int(str(order)[0:-1]) * multi
    return int(ans)


def importer(file):
    with open(f"{file}") as f:
        bands = f.readlines()
    for line in range(len(bands)):
        bands[line] = bands[line][:4]
    total_questions = len(bands)
    data = [bands, total_questions]
    return data
# Make quesiton not go over limit (10/9)
# add some silver color code multiplyers


def display():
    global bands, value, run
    colours = ['black', '#5e3d05', 'red', '#ff8400', 'yellow', 
               'green', 'blue', 'violet', 'grey', 'white', 
               '#dbac34', '#a5a9b4']
    colours_writen = ['Black', 'Brown', 'Red', 'Orange', 
                      'Yellow', 'Green', 'Blue', 'Purple', 
                      'Grey', 'White', 'Gold', 'Silver']
    if bands != []:
        band = random.randint(0, (len(bands) - 1))
        value = bandToValue(bands[band])
        alt = False
        for i in range(4):
            if bands[band][i] == 'a':
                alt = 'a'
            elif bands[band][i] == 'b':
                alt = 'b'
        first = int(str(bands[band])[0])
        second = int(str(bands[band])[1])
        third = int(str(bands[band])[2])
        if not alt:
            fourth = int(str(bands[band])[3])
        elif alt == 'a':
            fourth = 10
        elif alt == 'b':
            fourth = 11
        app.draw(app.canvas, app.x1, app.y1, app.x2, app.y2, colours[first], 
                 colours[second], colours[third], colours[fourth])
        app.display_txt.config(text=f'\
{colours_writen[first]} {colours_writen[second]}\
 {colours_writen[third]} {colours_writen[fourth]}')
        bands.pop(band)
    else:
        run = False


def confirm(event=None):
    global score, question
    app.ans = app.entry.get()
    if run and app.ans != '' and not question > total_questions:
        if question != total_questions:
            question += 1
            app.ques.config(text=f'Question {question}/{total_questions}')
        else:
            app.ques.config(text='Press enter to view your final score')
        if int(app.ans) == value:
            app.lbl.config(text=f'Correct it was {value}')
            score += 1
        else:
            app.lbl.config(text=f'nice try the correct values was {value}')
        # final score display
        display()
    elif not run and question == total_questions:
        app.lbl.config(text=f'Total score: {score}/{total_questions}')
        if score >= total_questions//2:
            app.ques.config(text='Well done thats a passing grade!')
        else:
            app.ques.config(text="It looks like you still need \
some practise, don\'t worry keep trying")


if __name__ == "__main__":
    # init
    question = 1
    exclude = []
    bands = importer("bands.txt")
    total_questions = bands[1]
    bands = bands[0]
    score = 0
    run = True
    app = application.App()
    app.ready()
    app.ques.config(text=f'Question {question}/{total_questions}')
    app.bind('<Return>', confirm)
    display()
    app.mainloop()