# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.
from fractions import Fraction

def fraction(num1, num2):
    numerator1, denominator1 = map(int, num1.split('/'))
    numerator2, denominator2 = map(int, num2.split('/'))
    total_denominator = denominator1 * denominator2
    sum_numerator = numerator1 * denominator2 + numerator2 * denominator1
    res_sum = f'{sum_numerator}/{total_denominator}'
    res_mult = f'{numerator1 * numerator2}/{total_denominator}'
    return res_sum, res_mult


num1 = input('Введите первую дробь: ')
num2 = input('Введите вторую дробь: ')
res = fraction(num1, num2)
print(res)
fr1 = Fraction(num1)
fr2 = Fraction(num2)
fr_sum = Fraction(res[0])
fr_mult = Fraction(res[1])
assert fr_sum == fr1 + fr2, 'Сумма дробей функции не равна сумме дробей модуля fractions.'
assert fr_mult == fr1 * fr2, 'Произведение дробей функции не равно произведению дробей модуля fractions.'
print('Проверка пройдена, функция возвращает правильный результат.')
