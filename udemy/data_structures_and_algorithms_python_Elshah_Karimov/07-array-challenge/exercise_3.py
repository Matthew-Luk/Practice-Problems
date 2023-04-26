# Given a list, write a function to get first, second best scores from the list.

def firstSecond(givenList):
    givenList.sort()
    return givenList[-1], givenList[-2]