integers = [1,2,3,4]
print(integers)

stringList = ["Milk", "Cheese", "Butter"]
print(stringList)

mixedList = [1, 1.5, "spam"]
print(mixedList)

nestedList = [1,2,3,4,5,[1.5,1.6], ["test"]]
print(nestedList)

shoppingList = ["Milk", "Cheese", "Butter"]
print("milk" in shoppingList)

for i in shoppingList:
    print(i)

for i in range(len(shoppingList)):
    shoppingList[i] = shoppingList[i] + "+"
    print(shoppingList[i])

myList = [1,2,3,4,5,6,7]
print(myList)
myList[2] = 33
myList[4] = 55
print(myList)

myList.insert(4, 15)
myList.append(55)
newList = [11,12,13,14]
myList.extend(newList)
print(myList)


myList = ["a","b","c","d","e","f"]
print(myList)
myList.pop(1)
del myList[2:4]
myList.remove("e")
print(myList)


myList = [10,20,30,40,50,60,70,80,90]
if 200 in myList:
    print(myList.index(20))
else:
    print("The value does not exist in the list")

def searchinList(list, value):
    for i in list:
        if i == value:
            return list.index(value)
    return "The value does not exist in the list"

print(searchinList(myList,500))