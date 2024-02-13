from cmath import sqrt

from regular_figuer.all_figure import square, triangle, parallelogram


#Делаем функция под каждую картинку
def fish(x, y):
    square(-100, 300, "orange", 45, scale=0.7)  # вариант с увеличаением фигуры на 20%
    triangle(-50, 325, "blue", 45, scale=1)  # вариант с увеличаением фигуры на 20%
    triangle(-150, 350, "red", 0, scale=1)  # вариант с увеличаением фигуры на 20%
    triangle(-50, 250, "yellow", 90, scale=1)  # вариант с увеличаением фигуры на 20%
    triangle(-198, 200, "purple", 270, scale=0.5)  # вариант с увеличаением фигуры на 20%
    triangle(-198, 250, "pink", 90, scale=0.5)  # вариант с увеличаением фигуры на 20%
    parallelogram(-198, 250, "green", 240, scale=1)  # вариант с увеличаением фигуры на 20%


def helicopter(x,y):
    parallelogram(0, 300, "green", 0, scale=1)
    triangle(-141, 256, "blue", 315, scale = 0.8)
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
    triangle(-25, 50, "blue", 90, 0.75)
    triangle(28, -25, "purple", 180, 0.5)
    triangle(0, 100, "pink", 45, 0.5)

def rocket(x,y):
    triangle(0, 150, "pink", 315, 0.5)
    triangle(0, 150, "blue", 0, 0.7)
    triangle(0, 150, "yellow", 45, 1)
    triangle(70, -60, "red", 225, 1)
    parallelogram(70, -80, "green", 270, scale=0.8)
    square(0, 10, "orange", 45, 0.5)
    triangle(-35, -25, "purple", 45, 0.5)
