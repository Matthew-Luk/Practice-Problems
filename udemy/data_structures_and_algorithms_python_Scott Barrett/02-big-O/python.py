def print_items(n):
    # 1. 0(n)
    # O(n) - linear/proportional
    for i in range(n):
        print(i)

    # O(2n) drop constants == O(n)
    for i in range(n):
        print(i)

    for j in range(n):
        print(j)


    # 2. 0(n**2) - very inefficient - loop within a loop
    # n * n == O(n**2)
    for i in range(n):
        for j in range(n):
            print(i, j)

    # n * n * n = n**3 drop constants == O(n**2)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                print(i, j, k)

    # 0(n**2 + n) drop non-dominants == 0(n**2)
    for i in range(n):
        for j in range(n):
            print(i, j)

    for k in range(n):
        print(k)


print_items(10)


# 3. 0(1) - constant time
# 0(1) - we do not increase the number of operations (most efficient)
def add_items(n):
    return n+n
    # # Also 0(1)
    # return n+n+n

print(add_items(10))

# 4. 0(log n) - divide and conquer
# 5, 0(nlog n) - some sorting algorithms - very efficient for sorting algorithms


# two different parameters a != n and b != n
# 0(a+b)
def print_items2(a, b):
    for i in range(a):
        print(i)

    for j in range(b):
        print(j)

# 0(a*b)
def print_items2(a, b):
    for i in range(a):
        for j in range(b):
            print(i,j)