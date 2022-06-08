from random import randint

values = [randint(-50, 50) for _ in range(10)]

print(values)

n = int(input('Введите значение, элементы меньше которого будут удалены: '))

for i in range(len(values)-1, 0, -1):

   if values[i] < n: values.pop(i)

print(values)
