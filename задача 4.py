a = [int(i) for i in input().split()]
s = 0
for item in a:
    if item % 2 == 0:
        s += item
print(s)
