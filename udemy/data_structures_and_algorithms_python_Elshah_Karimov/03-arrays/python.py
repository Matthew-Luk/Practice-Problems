from array import *

arr1 = array("i", [1,2,3,4,5,6])
arr2 = array("d", [1.3,1.5,1.6])

print(arr2)

arr1.insert(2,9)
print(arr1)

def traverseArray(array):
    for i in array:
        print(i)


traverseArray(arr1)

def accessElement(array, index):
    if index > len(array):
        print("There is not any element in this index")
    else:
        print(array[index])

accessElement(arr1, 1)

def searchInArray(array, value):
    for i in array:
        if i == value:
            return True
    return "The element does not exist in this array"

print(searchInArray(arr1, 9))

arr1.remove(4)
print(arr1)