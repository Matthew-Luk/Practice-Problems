# map function
li = [1,2,3,4,5,6,7,8,9,10]

def func(x):
    return x**x

print(list(map(func,li)))
print([func(x) for x in li if x%2 == 0])

# filter function
def add7(x):
    return x+7

def isOdd(x):
    return x%2 != 0

a = [1,2,3,4,5,6,7,8,9,10]
b = list(filter(isOdd,a))
c = list(map(add7,b))
print(c)

# lambda function
def func(x):
    func2 = lambda x: x+5
    return func2(x) + 85

func3 = lambda x,y=4:x+y
print(func3(5))
print(func(2))

a = [1,2,3,4,5,6,7,8,9,10]
newList = list(filter(lambda x: x%2==0,a))
print(newList)