# Given 2D list calculate the sum of diagonal elements.

def sumDiagonal(a):
    sum = 0
    for i in range(len(a)):
        sum += a[i][i]
    return sum