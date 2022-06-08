a = [[1,2,3], [3,0,6], [4,5,2]]
sum(all(col) for col in map(lambda *x: x, *a))
