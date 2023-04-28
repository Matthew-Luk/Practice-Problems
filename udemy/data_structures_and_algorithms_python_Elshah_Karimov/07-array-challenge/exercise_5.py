# Write a function to find the duplicate number on given integer array/list.

def removeDuplicates(myList):
    newList = []
    for i in myList:
        if i not in newList:
            newList.append(i)
    return newList