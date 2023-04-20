# Question 4 - How to find maximum product of two integers in the array where all elements are positive
list = [1,20,30,44,5,56,57,8,9,10,31,12,13,14,35,16,27,58,19,21]

def maxProduct(array):
    answer = 0
    for i in range(len(array)):
        for j in range(i+1, len(array)):
           if array[i] * array[j] > answer:
                answer = array[i] * array[j]
                pairs = str(array[i]) + "," + str(array[j])
    print(pairs)
    print(answer)

maxProduct(list)