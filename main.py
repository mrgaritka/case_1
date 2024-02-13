from picture.all_picture import fish, helicopter, rabbit, rocket, ship, left_person, humen, rooster, big_sqare
import turtle



def main():
    turtle.screensize(900, 900)
    turtle.speed(1000)  # Установка максимальной скорости рисования
    fish(115, 20) # Передаем координаты нашей рыбе
    helicopter(115, -500)
    rabbit(-500,135)
    left_person(-370,-150)
    rocket(500,-300)
    humen(200,-100)
    rooster(560,30)
    ship(-500,-400)
    big_sqare(0,0)
    turtle.done() # Завершаем рисовать



if __name__ == '__main__':
    main()
