from picture.all_picture import fish
import turtle



def main():
    turtle.speed(10)  # Установка максимальной скорости рисования
    fish(0, 0) # Передаем координаты нашей рыбе
    turtle.done() # Завершаем рисовать



if __name__ == '__main__':
    main()
