# Given a list, write a function to get first, second best scores from the list.

def firstSecond(givenList):
    givenList.sort()
    return givenList[-1], givenList[-2]

myList = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]
print(firstSecond(myList))