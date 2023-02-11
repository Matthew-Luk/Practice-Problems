# Lambda arguments: expression

add10 = lambda x: x+ 10
print(add10(5))

def add10_function(x):
    return x + 10

mult = lambda x,y: x*y
print(mult(2,7))

points2d = [(1,2), (15,1), (5,-1), (10,4)]
# sort by the y value instead of the x value
points2d_sorted = sorted(points2d, key=lambda x: x[0] + x[1])
print(points2d)
print(points2d_sorted)

# map function(func, seq)
a = [1,2,3,4,5,6]
b = map(lambda x: x * 2, a)
print(list(b))

c = [x*2 for x in a]
print(c)

#filter function(func, seq)
d = filter(lambda x: x%2==0,a)
print(list(d))

e = [x for x in a if x%2==0]
print(e)

# reduce(func, seq)
from functools import reduce
product_a = reduce(lambda x,y: x*y,a)
print(product_a)