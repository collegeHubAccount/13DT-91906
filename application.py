# import/s
import tkinter as tk
from PIL import ImageTk, Image


# settup class for tk
class App(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        # configuration
        self.val = self.register(self.onlyNum)
        self.title("Resistor test")
        self.resizable(False,False)
        self.canvas_w = 640
        self.canvas_h = 480
        self.geometry(f"{self.canvas_w}x{self.canvas_h}+240+100")
        self.canvas_h *= 0.3
        self.displace = -140 / 2
        self.img = Image.open("resbody.png").resize((300,58))
        self.img = ImageTk.PhotoImage(self.img)
        self.x1 = (self.canvas_w * 0.5) + self.displace
        self.y1 = (self.canvas_h * 0.5)
        self.x2 = (self.canvas_w * 0.5) + self.displace + 20
        self.y2 = (self.canvas_h * 0.5) - 45

        # objects
        self.canvas = tk.Canvas(self, width=self.canvas_w,
                                height=self.canvas_h)
        self.entry = tk.Entry(self, width=40, validate='key', 
                              validatecommand=(self.val, '%S'))
        self.lbl = tk.Label(self, text='Enter the resistor value in ohms then \
press ENTER \n to check your answer and move onto the next question')
        self.display_txt = tk.Label(self, text='')
        self.ques = tk.Label(self, text='')

    
    # this function is for validity checking it simply returns true if input
    # is a number (0-9)
    def onlyNum(self, char):
        if char.isdigit():
            return True
        else:
            return False


    # this draws all the resistor bands with the correct ofesets
    def draw(self, canvas, x1, y1, x2, y2, 
             colour1, colour2, colour3, colour4, colour5="brown"):
        canvas.create_rectangle(x1, y1, x2, y2, fill=colour1)
        canvas.create_rectangle(x1 + 30, y1, x2 + 30, y2, fill=colour2)
        canvas.create_rectangle(x1 + 60, y1, x2 + 60, y2, fill=colour3)
        canvas.create_rectangle(x1 + 90, y1, x2 + 90, y2, fill=colour4)
        canvas.create_rectangle(x1 + 120, y1, x2 + 120, y2, fill=colour5)


    # runs after setup in complete in main file just packs everything to 
    # prepare for usage
    def ready(self):
        self.canvas.pack()
        self.canvas.create_image(self.canvas_w//2, 50, image=self.img)
        self.display_txt.pack()
        self.entry.pack()
        self.lbl.pack()
        self.ques.pack()