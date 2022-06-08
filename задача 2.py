from random import randint

summ = 0

n = int(input('Введите количество значений в массиве: '))

values = [randint(-500, 500)/100 for _ in range(n)]

for value in values[::-1]:

   if value < 0: break

   summ += value

print(values)

print('Сумма значений правее последнего отрицательного значения равна:', summ)

