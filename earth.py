from tkinter import *


class Earth:

    def __init__(self):
        self.window = Tk()
        self.width = 1280
        self.height = 640
        self.window.title("ISS position")

        self.earth_image = PhotoImage(file="./map.png")
        self.canvas = Canvas(width=self.width, height=self.height)
        self.canvas.create_image(self.width/2, self.height/2, image=self.earth_image)
        self.canvas.pack()

    def maintain_window(self):
        self.window.mainloop()
