import tkinter as tk
from math import cos, sin, pi

class JarvisFace:
    def __init__(self, root):
        self.canvas = tk.Canvas(root, width=400, height=400, bg='black', highlightthickness=0)
        self.canvas.pack()
        self.angle = 0
        self.rug_color = "#00d2ff" 
        self.draw_reactor()

    def draw_reactor(self):
        self.canvas.delete("all")
        self.canvas.create_oval(50, 50, 350, 350, outline=self.rug_color, width=4)
        for i in range(12):
            a = self.angle + (i * 30) * pi / 180
            x = 200 + 130 * cos(a)
            y = 200 + 130 * sin(a)
            self.canvas.create_line(200, 200, x, y, fill=self.rug_color, width=2)
        self.angle += 0.04
        self.canvas.after(50, self.draw_reactor)

    def update_theme(self, color):
        self.rug_color = color
