from picture.all_picture import fish, helicopter
import turtle



def main():
    turtle.speed(100)  # Установка максимальной скорости рисования
    fish(0, 0) # Передаем координаты нашей рыбе
    helicopter(0,0)
    turtle.done() # Завершаем рисовать



if __name__ == '__main__':
    main()
