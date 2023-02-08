# Lists: ordered, mutable, allows duplicate elements

mylist = ["banana","cherry","apple"]
print(mylist)

for x in mylist:
    print(x)

if "yes" in mylist:
    print("yes")
else:
    print("no")
mylist.append("lemon")
print(mylist)

mylist.insert(1, "blueberry")
print(mylist)

print(len(mylist))

item = mylist.pop()
print(item)
item2 = mylist.remove("cherry")
item3 = mylist.clear()
print(mylist)

mylist2 = [4,3,1,-1,-5,10]
print(mylist2)

new_list = sorted(mylist2)
print(mylist2)
print(new_list)

list_org = ["banana","cherry","apple"]

# three ways to copy a list without
list_cpy = list_org.copy()
# list_cpy = list(list_org)
# list_cpy = list_org[:]

list_cpy.append("lemon")
print(list_cpy)
print(list_org)

a = [1,2,3,4,5,6]
b = [i*i for i in a]
print(b)