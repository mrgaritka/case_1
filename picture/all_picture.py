from regular_figuer.all_figure import square, triangle



#Делаем функция под каждую картинку
def fish(x, y):
    # square(-200, 200, "red")  #Состовляем из готовых функций картинки
    square(-100, 300, "blue", 30, scale=1.2)  #вариант с увеличаением фигуры на 20%
    triangle(200, 200, "blue", 30, scale=1.2)  #вариант с увеличаением фигуры на 20%

