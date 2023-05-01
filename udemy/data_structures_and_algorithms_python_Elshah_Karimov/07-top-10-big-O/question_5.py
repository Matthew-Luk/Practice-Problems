def printUnorderedPairs(arrayA, arrayB):
    for i in range(len(arrayA)): # 0(arrayA)
        for j in range(len(arrayB)): # 0(arrayB)
            for k in range(0,100000): # 0(1)
                print(str(arrayA[i]) + "," + str(arrayB[j])) # 0(1)

# Time Complexity = 0(ab)