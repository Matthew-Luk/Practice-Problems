# Dictionary: key-value pairs, unordered, mutable

mydict = {"name": "Matt", "age": 27, "city": "San Francisco"}
print(mydict)

mydict = dict(name="Mary",age=27,city="Boston")
print(mydict)

value = mydict["name"]
print(value)

mydict["email"] = "matt@gmail.com"
print(mydict)

mydict["email"] = "mattluk123@gmail.com"
print(mydict)

del mydict["name"]
print(mydict)

mydict.pop("age")
print(mydict)

if "lastname" in mydict:
    print(mydict["lastname"])
else:
    print("not in dict")

try:
    print(mydict["lastname"])
except:
    print("not in dict")

for key in mydict.keys():
    print(key)

for value in mydict.values():
    print(value)

for key, value in mydict.items():
    print(f"{key}: {value}")

mydict_cpy = mydict.copy()
print(mydict_cpy)

mydict_cpy["email"] = "matthew123@gmail.com"
print(mydict_cpy)
print(mydict)


my_dict = {"name": "Matthew", "age": 27, "email":"matthew123@gmail.com"}
my_dict2 = dict(name="Mary", age=27, city="Boston")

my_dict.update(my_dict2)
print(my_dict)

mydict3 = {3: 9, 6: 36, 9: 81}
print(mydict3)

value = mydict3[3]
print(value)

mytuple = (8, 7)
mydict4 = {mytuple: 15}
print(mydict4)