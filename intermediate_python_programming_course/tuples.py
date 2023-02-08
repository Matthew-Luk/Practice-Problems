# Tuple: ordered, immutable, allows duplicate elements

mytuple = ("Max", 28, "Boston")
# mytuple = tuple(["Max", 28, "Boston"])
print(mytuple)

item = mytuple[-1]
print(item)

if "Max" in mytuple:
    print("yes")
else:
    print("no")

mytuple2 = ("a","p","p","l","e")
print(len(mytuple2))
print(mytuple2.count("p"))
print(mytuple2.index("p"))

mylist = list(mytuple2)
print(mylist)
mytuple3 = tuple(mylist)
print(mytuple3)

a = (1,2,3,4,5,6,7,8,9,10)
b = a[::-1]
print(b)

mytuple3 = "Max", 28, "Boston"
name, age, city = mytuple3
print(name)
print(age)
print(city)

mytuple4 = (0,1,2,3,4)

i1, *i2, i3 = mytuple4

print(i1)
print(i2)
print(i3)

# tuples can be more efficient, space and time complexity is better on the tuple
import sys
my_list = [0,1,2,"hello",True]
my_tuple = (0,1,2,"hello",True)
print(sys.getsizeof(my_list), "bytes")
print(sys.getsizeof(my_tuple), "bytes")

import timeit
print(timeit.timeit(stmt="[0,1,2,3,4,5]", number=1000000))
print(timeit.timeit(stmt="(0,1,2,3,4,5)", number=1000000))