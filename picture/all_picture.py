from cmath import sqrt

from regular_figuer.all_figure import square, triangle, parallelogram


#Делаем функция под каждую картинку
def fish(x, y):
    square(-100, 300, "orange", 45, scale=0.7)  # вариант с увеличаением фигуры на 20%
    triangle(-50, 325, "light blue", 45, scale=1)  # вариант с увеличаением фигуры на 20%
    triangle(-150, 350, "red", 0, scale=1)  # вариант с увеличаением фигуры на 20%
    triangle(-50, 250, "yellow", 90, scale=1)  # вариант с увеличаением фигуры на 20%
    triangle(-198, 200, "purple", 270, scale=0.5)  # вариант с увеличаением фигуры на 20%
    triangle(-198, 250, "pink", 90, scale=0.5)  # вариант с увеличаением фигуры на 20%
    parallelogram(-198, 250, "green", 240, scale=1)  # вариант с увеличаением фигуры на 20%


def helicopter(x,y):
    parallelogram(0, 300, "green", 0, scale=1)
    triangle(-141, 256, "light blue", 315, scale = 0.8)
    triangle(-25, 256, "red", 45, 1)
    triangle(-25, 115, "yellow", 225, 1)
    triangle(-133, 151, "purple", 315, 0.5)
    triangle(-101, 186, "pink", 135, 0.5)
    square(-190,170, "orange",225, 0.5)

def rabbit(x, y):
    square(0, 200, "orange", 0, 0.5)
    parallelogram(-25, 203, "green", 240, scale=1)
    triangle(-3, 175, "red", 90, 1)
    triangle(-103, -25, "yellow", 270, 1)
    triangle(-25, 50, "light blue", 90, 0.75)
    triangle(28, -25, "purple", 180, 0.5)
    triangle(0, 100, "pink", 45, 0.5)
def humen(x, y):
    square(300, 300, "orange", 45, scale=0.7)
    triangle(300, 100, "red", 270, 1)
    triangle(200, 200, "yellow", 0, 1)
    triangle(400, 0, "light blue", 180, 1)
    parallelogram(170, -10, "green", 330, scale=1.5)
    triangle(380, 0, "purple", 0, 0.5)
    triangle(180, -80, "pink", 90, 0.5)

def left_person(x,y):
    square(0, 300, 'orange', 45, scale=0.5)
    triangle(-10, 120, "red", -90, 1)
    parallelogram(-100, 170, "green", -30, scale=1)
    triangle(20, 147, "yellow", 90, 1)
    triangle(-117, 15, "pink", -90, 0.5)
    triangle(23, 80, "light blue", 45, scale=0.8)
    triangle(20, -60, "purple", -135, 0.5)

def ship(x,y):
    triangle(0, 200, "purple", 180, 0.5)
    triangle(-50, 195, "red", 45, 1)
    triangle(-53, 170, "yellow", 90, 1)
    triangle(-45, 52, "pink", -45, 0.5)
    square(0, 100, 'orange', 45, scale=0.5)
def rooster(x,y):
    square(0, 300, "orange", 0, scale=0.5)
    triangle(0, 300, "pink", 315, 0.7)
    triangle(-50, 150, "yellow", 270, 1)
    triangle(20, 150, "purple", 225, 0.5)
    triangle(-150, 300, "red", 0, 1)
    triangle(-150, 300, "light blue", 315, 0.7)
    parallelogram(-170, 234, "green", 285, scale=0.7)

def ship(x,y):
    triangle(0, 200, "purple", 180, 0.5)
    triangle(-50, 195, "red", 45, 1)
    triangle(-53, 170, "yellow", 90, 1)
    triangle(-45, 52, "pink", -45, 0.5)
    square(25, 122, 'orange', 43, scale=0.45)
    triangle(30, 45, "light blue", 135, 0.7)
    parallelogram(-80, 45, "green", 45, scale=0.65)
