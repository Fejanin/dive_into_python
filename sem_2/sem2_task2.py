# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое
# представление. Функцию hex используйте для проверки своего результата.
sym = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}

def into_hex(number):
    res = ''
    while number:
        last_num = number % 16
        if last_num > 9:
            res = str(sym[last_num]) + res
        else:
            res = str(last_num) + res
        number //= 16
    return '0x' + res

num = into_hex(int(input('Введите целое положительное число: ')))
print(num)

# Дополнительные проверки
for i in range(1, 101):
    assert into_hex(i) == hex(i), f'Функция вернула {into_hex(i)}, вместо {hex(i)}'
print('Проверка прошла успешно.')
