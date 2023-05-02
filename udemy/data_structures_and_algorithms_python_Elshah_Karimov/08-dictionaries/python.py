myDict = {"name": "Edy", "age": 26, "address": "London", "education": "master"}
print(myDict)

def traverseDict(dict):
    for key in dict:
        print(key, dict[key])

traverseDict(myDict)

def searchDict(dict, value):
    for key in dict:
        if value == dict[key]:
            return key, value
    return "Value does not exist"

print(searchDict(myDict, "Edy"))


myDict.pop("name")
print(myDict.popitem())
del myDict["age"]
myDict.clear()
print(myDict)

dict = myDict.copy()
print(dict)


newDict = {}.fromkeys([1,2,3], 0)
print(newDict)

print(myDict.get("city", 27))


print(myDict.items())
# print(myDict.popitem())
print(myDict)

print(myDict.values())
newDict = {"a":1, "b":2, "c":3}
myDict.update(newDict)
print(myDict)