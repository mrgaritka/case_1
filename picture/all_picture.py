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
    triangle(-25, 256, "red", 90, 1)
    triangle(-25, 115, "yellow", 180, 1)
    triangle(-133, 151, "purple", 90, 0.5)
    triangle(-101, 186, "pink", 180, 0.5)
    square(-190,170, "orange",90, 0.5)