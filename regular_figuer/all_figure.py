import turtle

def square(x, y, a, fill_color):
    turtle.up()  # Поднять перо (не оставлять след при перемещении)
    turtle.setposition(x, y)  # Установка позиции
    turtle.down()  # Опустить перо (оставлять след при перемещении)
    turtle.fillcolor(fill_color)  # Установка цвета заливки
    turtle.begin_fill()  # Начать заливку фигуры
    for i in range(4):  # Цикл для рисования квадрата
        turtle.forward(a)  # Переместиться вперед на длину стороны
        turtle.right(90)  # Повернуть направо на 90 градусов
    turtle.end_fill()  # Завершить заливку фигуры