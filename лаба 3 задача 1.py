Maxiter = 500
x, eps = map(float,input("Введите аргумент и точность:").split())
c:float
y:float
n:int = 1
done:bool=True
c = x
y = c
while abs(c)> eps:
    c = -c* pow(x, 2)/2/n/(2*n + 1)
    y = y+c
    n = n+1 
    if n <= Maxiter:
        print("Ряд расходится")
        done = False
        if done:
            print("Аргумент:" + str(x) + "/n" +
                  "Значение Функции: "+ str(y) + "/n" +
                  "Вычислено с точностью" + str(eps) + " за " + str(n) + " итераций" + "/n")





