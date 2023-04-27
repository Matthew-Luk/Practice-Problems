# Write a function to find the missing number in a given integer array of 1 to 100.

def missingNumber(myList, totalCount):
    sumMissing = int(totalCount * (totalCount+1) / 2)
    return sumMissing - sum(myList)