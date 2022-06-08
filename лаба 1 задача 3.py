from math import sqrt, pi, exp, tan, log10, cos

a, x = map(int(input('Введите a и x: ').split()))

y = (sqrt(pi * x) - exp(0.2 * sqrt(a))
     +2 * tan(2*a) + 1.6e3
     *log10(pow(x, 2))) / (2
     *tan(2*a) *(1 / cos(x)))

print('Результат функции:' , str(round(y, 3)))


input()
