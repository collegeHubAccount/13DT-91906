# import/s
import tkinter as tk


# settup class for tk
class App(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        # configuration
        self.title("test application")
        self.canvas_w = self.winfo_screenwidth()
        self.canvas_h = self.winfo_screenheight()
        self.geometry(f"{self.canvas_w}x{self.canvas_h}")
        self.canvas_h *= 0.3

        self.displace = -140/2
        self.x1 = (self.canvas_w*0.5)+self.displace
        self.y1 = (self.canvas_h*0.5)
        self.x2 = (self.canvas_w*0.5)+self.displace+20
        self.y2 = (self.canvas_h*0.5)-40

        # objects
        self.canvas = tk.Canvas(self, width=self.canvas_w,
                                height=self.canvas_h)
        # self.draw(self.canvas, self.x1, self.y1, self.x2, self.y2, 
        #           "red", "blue", "yellow", "black")

    def draw(self, canvas, x1, y1, x2, y2, 
             colour1, colour2, colour3, colour4, colour5 = "brown"):
        canvas.create_rectangle(x1,y1,x2,y2,fill=colour1)
        canvas.create_rectangle(x1+30,y1,x2+30,y2,fill=colour2)
        canvas.create_rectangle(x1+60,y1,x2+60,y2,fill=colour3)
        canvas.create_rectangle(x1+90,y1,x2+90,y2,fill=colour4)
        canvas.create_rectangle(x1+120,y1,x2+120,y2,fill=colour5)
    
    def ready(self, canvas):
        canvas.pack(side=tk.TOP)