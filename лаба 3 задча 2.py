from math import cos
L, R, x = 0, 1, 0
while abs(R - L) >= 1e-4:
    x = (L + R) / 2
    if (cos(x) - x) * (cos(L) - L) < 0:
       R = x
    else:
        L = x
print(f'Корень равен {x:0.4}')
