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

    turtle.right(180-rotation)

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
    turtle.forward(a)# Переместиться вперед на длину стороны

    turtle.right(270 - rotation)
    turtle.end_fill()  # Завершить заливку фигуры

def parallelogram(x, y, fill_color, rotation=0, scale = 1):
    a = 100 * scale
    b = 50 * scale
    turtle.up()  # Поднять перо (не оставлять след при перемещении)
    turtle.setposition(x, y)  # Установка позиции
    turtle.down()  # Опустить перо (оставлять след при перемещении)
    turtle.fillcolor(fill_color)  # Установка цвета заливки
    turtle.begin_fill()  # Начать заливку фигуры

    turtle.right(rotation)  # Повернуть
    turtle.forward(a)  # Переместиться вперед на длину стороны

    turtle.right(120)  # Повернуть направо на 120 градусов
    turtle.forward(b)  # Переместиться вперед на длину стороны

    turtle.right(60)  # Повернуть направо на 60 градусов
    turtle.forward(a) # Переместиться вперед на длину стороны

    turtle.right(120)  # Повернуть направо на 120 градусов
    turtle.forward(b)

    turtle.right(60 - rotation)
    turtle.end_fill()  # Завершить заливку фигуры

def special(x, y, fill_color, rotation=0, scale = 1):
    a = 92 * scale
    b = 70 * scale
    turtle.up()  # Поднять перо (не оставлять след при перемещении)
    turtle.setposition(x, y)  # Установка позиции
    turtle.down()  # Опустить перо (оставлять след при перемещении)
    turtle.fillcolor(fill_color)  # Установка цвета заливки
    turtle.begin_fill()  # Начать заливку фигуры

    turtle.right(rotation)  # Повернуть
    turtle.forward(a)  # Переместиться вперед на длину стороны

    turtle.right(135)  # Повернуть направо на 90 градусов
    turtle.forward(b)  # Переместиться вперед на длину стороны

    turtle.right(45)  # Повернуть направо на 45 градусов
    turtle.forward(a)  # Переместиться вперед на длину стороны

    turtle.right(135)  # Повернуть направо на 135 градусов
    turtle.forward(b)

    turtle.right(45 - rotation)
    turtle.end_fill()  # Завершить заливку фигур


