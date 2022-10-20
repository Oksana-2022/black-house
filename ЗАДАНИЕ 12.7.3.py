money = input("Введите сумму, которую планируете положить под проценты:")
money_1 = money.split()
deposit = list(map(int, money_1))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
a = int(float(money) * 5.6 / 100.00)
b = int(float(money) * 5.9 / 100.00)
c = int(float(money) * 4.28 / 100.00)
d = int(float(money) * 4.0 / 100.00)
deposit = [a, b, c, d]
print(deposit)
print("Максимальная сумма, которую вы можете заработать -", max(deposit))
