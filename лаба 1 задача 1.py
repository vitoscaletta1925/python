kd=float(input("Введите курс доллара "))
k=float(input("Введите курс евро "))
print("1) Перевести из рублей в доллары и евро/n2)Перевести из долларов в евро и рубли/n")
vibor=int(input("Выберите ваше действие/n"))
if vibor==1:
    ryb=float(input("Введите сумму в рублях"))
    s1=ryb/kd
    s2=ryb/k
    print("Сумма в долларах = ",'{:.2f}'.format(s1))
    print("Сумма в евро = ",'{:.2f}'.format(s2))
elif vibor==2:
    kold=float(input("Введите сумму в долларах"))
    kol=float(input("Введите сумму в евро"))
    s1=kold*kd
    s2=kol*k
    print("Сумма перевода из долларов в рубли = ",'{:.2f}'.format(s1))
    print("Сумма перевода из евро в рубли = ",'{:.2f}'.format(s2)) 
else:
    print("Ошибка! введите только 1 или 2")
    exit(0)

    
