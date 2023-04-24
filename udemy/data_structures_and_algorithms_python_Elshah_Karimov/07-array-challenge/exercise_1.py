# Write a function called middle that takes a list and returns a new list that contains all but the first and last elements.

def middle(lst):
    newList = lst[1:-1]
    return newList

myList = [1, 2, 3, 4]
middle(myList)