import random
import secrets
import numpy as np

# float
a = random.uniform(1,10)
print(a)

# upper range included
b = random.randint(1,10)
print(b)

# upper range not included
c = random.randrange(1,10)
print(c)

d = random.normalvariate(0,1)
print(d)


mylist = list("ABCDEFGH")
e = random.choice(mylist)
f = random.sample(mylist,3)
print(f)

random.shuffle(mylist)
print(mylist)

random.seed(1)
print(random.random())
print(random.randint(1,10))
random.seed(2)
print(random.random())
print(random.randint(1,10))
random.seed(1)
print(random.random())
print(random.randint(1,10))
random.seed(2)
print(random.random())
print(random.randint(1,10))


g = secrets.randbelow(10)
print(g)

h = secrets.randbits(4)
print(h)

mylist2 = list("ABCDEFGH")
i = secrets.choice(mylist2)
print(i)

j = np.random.rand(3,3)
print(j)

k = np.random.randint(0,10,(3,4))
print(k)

arr = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(arr)
np.random.shuffle(arr)
print(arr)