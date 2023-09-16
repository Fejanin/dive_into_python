# 4. Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
# должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
# числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint


min_number = 0
max_number = 1000
number_of_attempts = 10
num = randint(min_number, max_number)
win = False

print(f'Программа загадала число от {min_number} до {max_number}. Попробуйте угадать его.\nУвас есть только {number_of_attempts} попыток.')

for i in range(number_of_attempts):
    print(f'Попытка №{i + 1}.')
    while True:
        try:
            user_number = int(input('Введите ваше число: '))
            break
        except ValueError:
            print('Введены некорректные данные. Попробуйте еще раз.')
    if num == user_number:
        print('Вы угадали. С вашей удачей нужно учавствовать в лотереях.')
        win = True
        break
    else:
        if num < user_number:
            print('Загаданное чило меньше.\n')
        else:
            print('Загаданное чило больше.\n')

if not win:
    print('Мне очень жаль, но вы проиграли.')

print('Игра окончена.')
