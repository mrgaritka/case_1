from cmath import sqrt

from regular_figuer.all_figure import square, triangle, parallelogram


#Делаем функция под каждую картинку
def fish(x, y):
    # square(-200, 200, "red")  #Состовляем из готовых функций картинки
    square(-100, 300, "blue", 0, scale=1.2)  #вариант с увеличаением фигуры на 20%
    triangle(200, 200, "blue", 0, scale=1.2)  #вариант с увеличаением фигуры на 20%
    parallelogram(-300, 300, "blue", 0, scale=1.2)

def helicopter(x,y):
    parallelogram(0, 300, "green", 0, scale=1)
    triangle(-141, 256, "blue", 315, scale = 0.8)
    triangle(-25, 256, "red", 90, 1)
    triangle(-25, 115, "yellow", 180, 1)
    triangle(-133, 151, "purple", 90, 0.5)
    triangle(-101, 186, "pink", 180, 0.5)
    square(-190,170, "orange",90, 0.5)