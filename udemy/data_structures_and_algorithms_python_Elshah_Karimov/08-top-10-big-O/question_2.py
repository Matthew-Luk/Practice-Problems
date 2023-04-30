def printPairs(array):
    for i in array: # 0(n)
        for j in array: # 0(n)
            print(str(i) + "," + str(j)) # 0(1)

# Time Complexity = 0(n**2)