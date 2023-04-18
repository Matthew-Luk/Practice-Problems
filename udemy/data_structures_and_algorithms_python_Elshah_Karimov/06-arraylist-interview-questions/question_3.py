# Question 3 - Finding a number in an array
def findNumber(array, number):
    for i in array:
        if i == number:
            print(True)


array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
findNumber(array,15)