def printUnorderedPairs(arrayA, arrayB):
    for i in range(len(arrayA)): # 0(arrayA)
        for j in range(len(arrayB)): # 0(arrayB)
            if arrayA[i] < arrayB[j]: # 0(1)
                print(str(arrayA[i]) + "," + str(arrayB[j])) # 0(1)

# a = len(arrayA)
# b = len(arrayB)

# Time Complexity = 0(ab)