import collections
from collections import Counter

a = Counter("gallad")
print(a)
b = Counter(["a","a","b","c","c"])
print(b)
e = Counter({"a":1,"b":2})
print(3)
f = Counter(cats=4, dogs=7)
print(f["cats"])

print(list(b.elements()))
print(b.most_common(2))

c = Counter(a=4, b=2, c=0, d=-2)
d = ["a", "b", "b", "c"]
c.subtract(d)
print(c)
c.update(d)
print(c)
c.clear()
print(c)