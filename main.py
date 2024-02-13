from picture.all_picture import fish, helicopter, rabbit, rocket, ship, left_person, human, rooster, big_sqare, human
import turtle



def main():
    turtle.screensize(900, 900)
    turtle.speed(100)  # Установка максимальной скорости рисования
    fish(115, 20) # Передаем координаты нашей рыбе
    helicopter(115, -500)  # Передаем координаты нашему вертолёту
    rabbit(-500,135)  # Передаем координаты нашему кролику
    left_person(-370,-150) # Передаем координаты левому человечку
    rocket(500,-300)  # Передаем координаты нашей ракете
    human(200,-100)  # Передаем координаты правому человечку
    rooster(560,30)  # Передаем координаты нашему петуху
    ship(-500,-400)  # Передаем координаты нашему кораблю
    big_sqare(0,0)  # Передаем координаты центральному квадрату
    turtle.done() # Завершаем рисовать



if __name__ == '__main__':
    main()
