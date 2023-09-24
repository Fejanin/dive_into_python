# Задание №6
# Напишите программу банкомат. 

# Начальная сумма равна нулю
# Допустимые действия: пополнить, снять, выйти
# Сумма пополнения и снятия кратны 50 у.е.
# Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# После каждой третей операции пополнения или снятия начисляются проценты - 3%
# Нельзя снять больше, чем на счёте
# При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# Любое действие выводит сумму денег

class CashDispenser:
    def __init__(self):
        self.cash = 0.00
        self.count_event = 0
        self.num_event = 3
        self.percentage_for_withdrawal_of_money = 1.5 # процент за снятие
        self.multiplicity = 50 # кратность при пополнении и снятии
        self.min_sum_for_withdrawal_of_money = 30 # минимальное стоимость обналичивания
        self.max_sum_for_withdrawal_of_money = 600 # максимальная стоимость обналичивания
        self.account_maintenance = 3 # обслуживание счета, взымается после 3-й операции (пополнения или снятия)
        self.wealth_tax = 10 # налог на богатство

    def added_money(self):
        self.pay_wealth_tax()
        print('Введите сумму для пополнения счета:')
        value = input()
        if not self.check_value(value):
            return
        value = float(value)
        if self.check_multiplicity(value):
            self.cash += value
            self.cash = round(self.cash, 2)
            print(f'На счет добавлено: {value}$.')
            self.check_event()
        else:
            print(f'Банкомат может проводить операции только кратно - {self.multiplicity}$.')

    def withdraw_money(self):
        self.pay_wealth_tax()
        print('Введите сумму для списания со счета:')
        value = input()
        if not self.check_value(value):
            return
        value = float(value)
        if self.check_multiplicity(value):
            percentage_for_withdrawal = self.calculated_percentage(value)
            if self.cash >= value + percentage_for_withdrawal:
                self.cash -= (value + percentage_for_withdrawal)
                self.cash = round(self.cash, 2)
                print(f'Со счета было обналичено: {value}$.\nЗа оказание услуги, банк взымает: {percentage_for_withdrawal}$.')
                self.check_event()
            else:
                print('На счету недостаточно средств.')
        else:
            print(f'Банкомат может проводить операции только кратно - {self.multiplicity}$.')

    def check_event(self):
        self.count_event += 1
        if not self.count_event % self.num_event:
            amount_to_be_debited = round(self.cash * self.account_maintenance / 100, 2)
            self.cash -= amount_to_be_debited
            print(f'За обслуживание счета списано: {amount_to_be_debited}$.')

    def calculated_percentage(self, value):
        percentage = round(value * self.percentage_for_withdrawal_of_money / 100, 2)
        if percentage < self.min_sum_for_withdrawal_of_money:
            return self.min_sum_for_withdrawal_of_money
        elif percentage > self.max_sum_for_withdrawal_of_money:
            return self.max_sum_for_withdrawal_of_money
        return percentage

    def pay_wealth_tax(self):
        if self.cash > 5_000_000:
            wealth_tax = round(self.cash * self.wealth_tax / 100, 2)
            self.cash = round(self.cash - wealth_tax, 2)
            print(f'Взымается налог на богатство, в размере: {wealth_tax}$.')

    def check_multiplicity(self, value):
        return not value % self.multiplicity

    def check_value(self, value):
        try:
            value = float(value)
        except:
            return
        return value > 0
            

    def __str__(self):
        return f'На счету {self.cash}$.'

        
class MenuCashDispenser:
    def init(self):
        self.is_work = True
        self.cash_dispenser = CashDispenser()
        self.user_choise = {'1': self.cash_dispenser.added_money, '2': self.cash_dispenser.withdraw_money, '3': self.quit}
        while self.is_work:
            print('\nMenu:')
            print(self.cash_dispenser)
            user_command = input('''Для пополнения счета введите - 1
Для снятия наличных введите - 2
Для завершения работы с банкоматом нажмите - 3.\n''')
            if user_command in self.user_choise:
                self.user_choise[user_command]()
            else:
                print('Введены некорректные данные.')

    def quit(self):
        self.is_work = False


menu = MenuCashDispenser()
menu.init()

