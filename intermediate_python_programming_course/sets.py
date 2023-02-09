# Sets: unordered, mutable, no duplicates

myset = {1,2,3,1,2}
myset = set([1,2,3,1,2])
myset = set("Hello")
myset = set()
myset.add(1)
myset.add(2)
myset.add(3)
print(myset)

myset.remove(3)
myset.remove(4)
myset.discard(4)
print(myset)

for i in myset:
    print(i)

if 4 in myset:
    print("yes")
else:
    print("no")

odds = {1,3,5,7,9}
evens = {0,2,4,6,8}
primes = {2,3,5,7}

u = odds.union(evens)
print(u)

i = odds.intersection(evens)
print(i)

i2 = odds.intersection(primes)
print(i2)

setA = {1,2,3,4,5,6,7,8,9}
setB = {1,2,3,10,11,12}

# in setA but not setB
diff = setA.difference(setB)
print(diff)
# in setB but not setA
diff2 = setB.difference(setA)
print(diff2)
# all differences
diff3 = setB.symmetric_difference(setA)
print(diff3)

setA.update(setB)
print(setA)

setA.intersection_update(setB)
print(setA)

setA.difference_update(setB)
print(setA)

setA.symmetric_difference_update(setB)
print(setA)

setA = {1,2,3,4,5,6}
setB = {1,2,3}
setC = {7,8}

# checks if all of setA is in setB
print(setA.issubset(setB))
# checks if all of setB is in setA
print(setB.issubset(setA))

print(setA.isdisjoint(setB))

setD = set(setA)
setD.add(7)
print(setD)
print(setA)

a = frozenset([1,2,3,4])
a.add(2)
a.remove(1)
print(a)