# import/s application is on a seprerate line because I created it
import random
import application


# takes in a band in base 12 form each character representing a color and 
# converts it to the value of the resistor. For example 210a is 21 ohms
def band_to_value(order) -> None:
    if str(order)[-1] == 'a':
        multi = 10 ** -1
    elif str(order)[-1] == 'b':
        multi = 10 ** -2
    else:
        multi = 10 ** int(str(order)[-1])
    ans = int(str(order)[0:-1]) * multi
    return int(ans)


# this is used to import the resistors from a file and returns 2 data blocks 
# first contains a list of all resistors in 210a format and second contains
# the number of total questions as int
def importer(file):
    with open(f"{file}") as f:
        bands = f.readlines()
    for line in range(len(bands)):
        bands[line] = bands[line][:4]
    total_questions = len(bands)
    data = [bands, total_questions]
    return data


# this is the display updater worth noting it handles drawing color bands and 
# decoding 210a format into red brown black gold format as well as displaying 
# using custom colors (colours variable is in same order as colours_writen)
def display(bands, run):
    colours = ['black', '#5e3d05', 'red', '#ff8400', 'yellow',
               'green', 'blue', 'violet', 'grey', 'white',
               '#dbac34', '#a5a9b4']
    colours_writen = ['Black', 'Brown', 'Red', 'Orange',
                      'Yellow', 'Green', 'Blue', 'Purple',
                      'Grey', 'White', 'Gold', 'Silver']
    if bands != []:
        band = random.randint(0, (len(bands) - 1))
        value = band_to_value(bands[band])
        alt = False
        for i in range(4):
            if bands[band][i] == 'a':
                alt = 'a'
            elif bands[band][i] == 'b':
                alt = 'b'
        first = int(str(bands[band])[0])
        second = int(str(bands[band])[1])
        third = int(str(bands[band])[2])
        # converting from base 12
        if not alt:
            fourth = int(str(bands[band])[3])
        elif alt == 'a':
            fourth = 10
        elif alt == 'b':
            fourth = 11
        # this updates the coloured squares
        app.draw(app.canvas, app.x1, app.y1, app.x2, app.y2, colours[first],
                 colours[second], colours[third], colours[fourth])
        # code here is split across multipul lines meaning indentation is reset
        app.display_txt.config(text=f'\
{colours_writen[first]} {colours_writen[second]}\
 {colours_writen[third]} {colours_writen[fourth]} Brown')
        bands.pop(band)
        app.entry.focus()
        return value, bands, run
    else:
        return 0, [], False



def confirm(event=None):
    global score, question, bands, run, value
    app.ans = app.entry.get()
    if run and app.ans != '' and not question > total_questions:
        if question != total_questions:
            question += 1
            app.ques.config(text=f'Question {question}/{total_questions}')
        else:
            app.canvas.delete("all")
            app.canvas.create_image(app.canvas_w//2, 50, image=app.img)
            app.ques.config(text='Press enter to view your final score')
        if int(app.ans) == value:
            app.lbl.config(text=f'Correct it was {value}')
            score += 1
        else:
            app.lbl.config(text=f'nice try the correct values was {value}')
        # final score display
        value, bands, run = display(bands, run)
    elif not run and question == total_questions:
        app.lbl.config(text=f'Total score: {score}/{total_questions}')
        if score >= total_questions//2:
            app.ques.config(text='Well done thats a passing grade!')
        else:
            app.ques.config(text="It looks like you still need \
some practise, don\'t worry keep trying")
    app.entry.delete(0, 'end')


if __name__ == "__main__":
    # init
    question = 1
    score = 0
    bands = importer("bands.txt")
    total_questions = bands[1]
    bands = bands[0]
    run = True
    app = application.App()
    app.ready()
    app.ques.config(text=f'Question {question}/{total_questions}')
    app.bind('<Return>', confirm)
    value, bands, run = display(bands, run)
    app.mainloop()
