def reverse(array):
    for i in range(0, int(len(array)/2)): # 0(n)
        other = len(array)-i-1 # 0(1)
        temp = array[i] # 0(1)
        array[i] = array[other] # 0(1)
        array[other] = temp # 0(1)
    print(array) # 0(1)

# Time Complexity = 0(n)