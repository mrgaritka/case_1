from cmath import sqrt

from regular_figuer.all_figure import square, triangle, parallelogram, special


#Делаем функция под каждую картинку
def fish(x, y):
    square(x-100, y+300, "orange", 45, scale=0.7)  # вариант с увеличением фигуры на 30%
    triangle(x-50, y+325, "light blue", 45, scale=1)
    triangle(x-150, y+350, "red", 0, scale=1)
    triangle(x-50, y+250, "yellow", 90, scale=1)
    triangle(x-198, y+200, "purple", 270, scale=0.5)  # вариант с уменьшением фигуры на 50%
    triangle(x-198, y+250, "pink", 90, scale=0.5)  # вариант с уменьшением фигуры на 50%
    parallelogram(x-198, y+250, "green", 240, scale=1)


def helicopter(x,y):
    parallelogram(x+0, y+300, "green", 0, scale=1)
    triangle(x-141, y+256, "light blue", 315, scale = 0.8)
    triangle(x-25, y+256, "red", 45, 1)
    triangle(x-25, y+115, "yellow", 225, 1)
    triangle(x-133, y+151, "purple", 315, 0.5)
    triangle(x-101, y+186, "pink", 135, 0.5)
    square(x-190, y+170, "orange",225, 0.5)

def rabbit(x, y):
    square(x+0, y+200, "orange", 0, 0.5)
    special(x-30, y+203, "green", 225, scale=0.8)
    triangle(x-3, y+175, "red", 90, 1)
    triangle(x-103, y-25, "yellow", 270, 1)
    triangle(x-25, y+50, "light blue", 90, 0.75)
    triangle(x+28, y-25, "purple", 180, 0.5)
    triangle(x+0, y+100, "pink", 45, 0.5)

def rocket(x,y):
    triangle(x+0, y+150, "pink", 315, 0.5)
    triangle(x+0, y+150, "light blue", 0, 0.7)
    triangle(x+0, y+150, "yellow", 45, 1)
    triangle(x+70, y-60, "red", 225, 1)
    parallelogram(x+70, y-80, "green", 270, scale=0.8)
    square(x+0, y+10, "orange", 45, 0.5)
    triangle(x-35, y-25, "purple", 45, 0.5)

def big_square(x,y):
    triangle(150, 132, "red", 135, 2)
    triangle(150, -10, "purple", 225, 1)
    square(80, 60, "orange", 45, 1)
    triangle(-135, 132, "yellow", 45, 2)
    triangle(-63, -82, "pink", -45, 1)
    triangle(150, -10, "light blue", 90, 1.5)
    special(-63, -83, "green", 0, scale=1.5)





def ship(x,y):
    triangle(x+0, y+200, "purple", 180, 0.5)
    triangle(x-50, y+195, "red", 45, 1)
    triangle(x-53, y+170, "yellow", 90, 1)
    triangle(x-45, y+52, "pink", -45, 0.5)
    square(x+25, y+122, 'orange', 43, scale=0.45)
    triangle(x+30, y+45, "light blue", 135, 0.7)
    special(x-73, y+45, "green", 44, scale=0.75)

def left_person(x,y):
    square(x+0, y+300, 'orange', 45, scale=0.5)
    triangle(x-10, y+120, "red", -90, 1)
    parallelogram(x-100, y+170, "green", -30, scale=1)
    triangle(x+20, y+147, "yellow", 90, 1)
    triangle(x-117, y+15, "pink", -90, 0.5)
    triangle(x+23, y+80, "light blue", 45, scale=0.8)
    triangle(x+20, y-60, "purple", -135, 0.5)
def human(x, y):
    square(x+300, y+270, "orange", 45, scale=0.5)
    triangle(x+300, y+100, "yellow", 270, 1)
    triangle(x+200, y+200, "red", 0, 1)
    triangle(x+400, y+0, "light blue", 180, 1)
    special(x+232, y+38, "green", 317.5, scale=1)
    triangle(x+380, y+0, "purple", 0, 0.5)
    triangle(x+230, y-35, "pink", 90, 0.5)

def rooster(x, y):
    square(x+0, y+300, "orange", 0, scale=0.5)
    triangle(x+0, y+300, "pink", 315, 0.7)
    triangle(x-50, y+150, "yellow", 270, 1)
    triangle(x+20, y+150, "purple", 225, 0.5)
    triangle(x-150, y+300, "red", 0, 1)
    triangle(x-150, y+300, "light blue", 315, 0.7)
    parallelogram(x-170, y+234, "green", 285, scale=0.7)
