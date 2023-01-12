import turtle as tl

tl.reset()
tl.speed(100)
tl.color("red")

def rosace(taille):
    for i in range(18):
        for j in range(3):
            tl.forward(taille)
            tl.right(120)
        tl.right(20)

rosace(100)
tl.up()
tl.goto(200, 0)
tl.down()
rosace(50)

tl.mainloop()
