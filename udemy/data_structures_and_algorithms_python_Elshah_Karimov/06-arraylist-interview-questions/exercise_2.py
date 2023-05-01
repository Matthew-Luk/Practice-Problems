# Find the maximum product of two integers in an array where all elements are positive.

def max_product(arr):
    arr.sort(reverse=True)
    return arr[0]*arr[1]

arr = [1, 7, 3, 4, 9, 5] 
print(max_product(arr))