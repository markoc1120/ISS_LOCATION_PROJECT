from tkinter import *
from earth import Earth
from data import Data
from PIL import Image

class Iss:

    def __init__(self, earth: Earth, data: Data):
        self.earth = earth
        self.data = data
        self.iss_image = PhotoImage(file="./iss.png")
        self.iss = self.earth.canvas.create_image(self.data.x, self.data.y, image=self.iss_image)
        self.move()

    def move(self):
        self.data.get_position()
        self.earth.canvas.moveto(self.iss, x=self.data.x-16, y=self.data.y-16)
        asd = self.data.older_rotation - self.data.rotation
        asd1 = self.data.rotation - self.data.older_rotation
        print(self.data.rotation, self.data.older_rotation, asd, asd1)
        self.earth.canvas.after(5000, self.move)
        self.data.older_rotation = self.data.rotation
        self.path()

    def path(self):
        if self.data.older[0] > 1270 and self.data.x < 15:
            self.data.older[0] = self.data.x
        else:
            self.earth.canvas.create_line(self.data.older[0], self.data.older[1], self.data.x, self.data.y,
                                          fill="#f4ff21")
            self.data.older[0] = self.data.x
            self.data.older[1] = self.data.y

    def rotate(self):
        self.image = Image.open("./iss.png")
        self.rotated = self.image.rotate(self.data.rotation - self.data.older_rotation).save("iss.png")
