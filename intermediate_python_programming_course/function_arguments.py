def print_name(name):
    print(name)

print_name("Matthew")

def foo(a,b,c,d=4):
    print(a,b,c,d)

foo(c=3,b=2,a=1,d=7)

def foo2(a,b,*args,**kwargs):
    print(a, b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])

foo2(1,2,3,4,5,six=6,seven=7)

def foo3(a, b, *, c, d):
    print(a, b, c, d)

foo3(1,2,c=3,d=4)

def foo4(a,b,c):
    print(a,b,c)

my_list = [0,1,2]
my_dict = {"a": 1, "b": 2, "c": 3}
foo4(*my_list)
foo4(**my_dict)

def foo5():
    global number
    number = 3
    print("number inside function:", number)

number = 0
foo5()
print(number)

def foo6(x):
    x = 5

var = 10
foo6(var)
print(var)