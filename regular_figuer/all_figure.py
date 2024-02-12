import turtle

def square(x, y, fill_color, rotation=0, scale = 1):
    a = 100 * scale
    turtle.up()  # Поднять перо (не оставлять след при перемещении)
    turtle.setposition(x, y)  # Установка позиции
    turtle.down()  # Опустить перо (оставлять след при перемещении)
    turtle.fillcolor(fill_color)  # Установка цвета заливки
    turtle.begin_fill()  # Начать заливку фигуры

    turtle.right(rotation)  # Повернуть
    turtle.forward(a)  # Переместиться вперед на длину стороны

    turtle.right(90)  # Повернуть направо на 90 градусов
    turtle.forward(a)  # Переместиться вперед на длину стороны

    turtle.right(90)  # Повернуть направо на 90 градусов
    turtle.forward(a)  # Переместиться вперед на длину стороны


    turtle.end_fill()  # Завершить заливку фигуры


def triangle(x, y, fill_color, rotation=0, scale=1):
    a = 100 * scale

    turtle.up()  # Поднять перо (не оставлять след при перемещении)
    turtle.setposition(x, y)  # Установка позиции
    turtle.down()  # Опустить перо (оставлять след при перемещении)
    turtle.fillcolor(fill_color)  # Установка цвета заливки
    turtle.begin_fill()  # Начать заливку фигуры

    turtle.right(rotation)
    turtle.forward(a)  # Переместиться вперед на длину стороны

    turtle.right(90)  # Повернуть направо на 90 градусов
    turtle.forward(a)  # Переместиться вперед на длину стороны
    turtle.end_fill()  # Завершить заливку фигуры


