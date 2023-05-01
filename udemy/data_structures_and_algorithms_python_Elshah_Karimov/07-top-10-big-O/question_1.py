def foo(array):
    sum = 0 # 0(1)
    product = 1 # 0(1)

    for i in array: # 0(n)
        sum += i # 0(1)

    for i in array: # 0(n)
        product *= i # 0(1)

    print("Sum = " + str(sum) +", Product = " + str(product)) # 0(1)

# Time Complexity = 0(n)