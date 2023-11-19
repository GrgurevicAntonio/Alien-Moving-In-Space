from tkinter import *
import time

WIDTH = 1700
HEIGHT = 1000

xSpeed = 3
ySpeed = 2

window = Tk()

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

bgImg = PhotoImage(file="space.png")

my_bgImg = canvas.create_image(0,0, image=bgImg, anchor=NW)

alienImg = PhotoImage(file="alien.png")

my_img = canvas.create_image(0,0, image=alienImg, anchor=NW)




image_width = alienImg.width()
image_height =alienImg.height()

while True:
    coordinates = canvas.coords(my_img)
    print(coordinates)
    if(coordinates[0]>= (WIDTH - image_width) or coordinates[0] < 0):
        xSpeed = -xSpeed

    if (coordinates[1] >= (HEIGHT - image_height) or coordinates[1] < 0):
        ySpeed = -ySpeed

    canvas.move(my_img, xSpeed, ySpeed)
    window.update()
    time.sleep(0.01)


window.mainloop()
