n = int(input('n: '))
m = int(input('m: '))
k = 1
while n != m:
    if n > m:
        n -= m
    else:
        m -= n
    k += 1
print(f'Можно разделить прямоугольник на {k} квадратов')
