x = input("Введите значения x ").split()
y = input("Введите значения y ").split()
x = float(x)
y = float(y)
if ((x*x)+(y*y)<=1 or x<=0 and y<=0 and y>=-x-2):
    print("Точка попадает в область")
else:
    print("Точка не попадает в область")
