my_list = [11,3,23,7]

# 0(1) because we are removing and adding from the end of the list
my_list.append(17)
# my_list = [11,3,23,7,17]

my_list.pop()
# my_list = [11,3,23,7]


# 0(n) because when removing or adding from the front of the list we are reindexing
my_list.pop(0)
# my_list = [3,23,7]

my_list.insert(0,11)
# my_list = [11,3,23,7]

# still 0(n)
my_list.insert(1,"Hi")
# my_list = [11,"Hi",3,23,7]
my_list.pop(1)

# searching for value in for loop = 0(n)
def search(n):
    for i in my_list:
        if i == n:
            print(n)

# searching by index = 0(1)
print(my_list[3])