# Question 5 - Is Unique:
list = [1,20,30,44,5,56,57,8,9,10,31,12,13,14,35,16,27,58,19,21]

def isUnique(array):
    for i in array:
        if array.count(i) > 1:
            return False
    return True

print(isUnique(list))


def isUnique2(array):
    newList = []
    for i in array:
        if i not in newList:
            newList.append(i)
    return(len(newList) == len(array))

print(isUnique2(list))


def isUnique3(array):
    newList = []
    for i in array:
        if i not in newList:
            newList.append(i)
        else:
            return False
    return True

print(isUnique3(list))