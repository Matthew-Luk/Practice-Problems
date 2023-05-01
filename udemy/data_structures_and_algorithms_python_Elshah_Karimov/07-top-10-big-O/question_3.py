def printUnorderedPairs(array):
    for i in range(0,len(array)): # 0(n)
        for j in range(i+1,len(array)): # 0(n)
            print(array[i] + "," + array[j]) # 0(1)

# Time Complexity = 0(n**2)