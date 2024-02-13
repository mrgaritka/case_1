from cmath import sqrt

from regular_figuer.all_figure import square, triangle, parallelogram


#Делаем функция под каждую картинку
def fish(x, y):
    square(-100, 300, "orange", 45, scale=0.7)
    triangle(-50, 325, "blue", 45, scale=1)
    triangle(-150, 350, "red", 0, scale=1)
    triangle(-50, 250, "yellow", 90, scale=1)
    triangle(-198, 200, "purple", 270, scale=0.5)
    triangle(-198, 250, "pink", 90, scale=0.5)
    parallelogram(-198, 250, "green", 240, scale=1)


def helicopter(x,y):
    parallelogram(0, 300, "green", 0, scale=1)
    triangle(-141, 256, "blue", 315, scale = 0.8)
    triangle(-25, 256, "red", 90, 1)
    triangle(-25, 115, "yellow", 180, 1)
    triangle(-133, 151, "purple", 90, 0.5)
    triangle(-101, 186, "pink", 180, 0.5)
    square(-190,170, "orange",90, 0.5)

def humen(x,y):
    square(300, 300, "orange", 45, scale=0.7)
    triangle(300, 100, "blue", 270, 1)
    triangle(200, 200, "blue", 0, 1)
    triangle(400, 0, "purple", 180, 1)
    parallelogram(170, -10, "purple", 330, scale=1.5)
    triangle(380, 0, "red", 0, 0.5)
    triangle(180, -80, "red", 90, 0.5)