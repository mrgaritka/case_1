from regular_figuer.all_figure import square, triangle, parallelogram


#Делаем функция под каждую картинку
def fish(x, y):
    # square(-200, 200, "red")  #Состовляем из готовых функций картинки
    square(-100, 300, "orange", 45, scale=1)  #вариант с увеличаением фигуры на 20%
    triangle(-27, 300, "blue", 0, scale=1)  #вариант с увеличаением фигуры на 20%
    triangle(-177, 375, "red", 315, scale=1.5)  # вариант с увеличаением фигуры на 20%
    triangle(-28, 230, "yellow", 90, scale=1.5)  # вариант с увеличаением фигуры на 20%
    triangle(-172, 230, "purple", 90, scale=0.5)  # вариант с увеличаением фигуры на 20%
    triangle(-272, 280, "pink", 180, scale=0.5)  # вариант с увеличаением фигуры на 20%
    parallelogram(-172, 230, "green", 90, scale=1)  # вариант с увеличаением фигуры на 20%
