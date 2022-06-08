from random import randint

cnt = 0

values = [randint(-50, 50) for _ in range(10)]

min_index = values.index(min(values))

max_index = values.index(max(values))

if max_index < min_index: min_index, max_index = max_index, min_index

for i in range(min_index+1,max_index):

   if values[i] > 0: cnt += 1

print(values)

print('Количество положительных значений между минимальным и максимальным значениями равно:', cnt)
