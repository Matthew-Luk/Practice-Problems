# Write a function to remove the duplicate numbers on given integer array/list.

def removeDuplicates(myList):
    newList = []
    for i in myList:
        if i not in newList:
            newList.append(i)
    return newList

print(removeDuplicates([1, 1, 2, 2, 3, 4, 5]))