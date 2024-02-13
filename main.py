from picture.all_picture import fish, helicopter, left_person
import turtle
#turtle.setup(1200,1200)


def main():
    turtle.speed(10)  # Установка максимальной скорости рисования
    fish(0, 0) # Передаем координаты нашей рыбе
    helicopter(0,0)
    left_person(0,0)
    turtle.done() # Завершаем рисовать



if __name__ == '__main__':
    main()
