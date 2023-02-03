# file = open("file.txt","r")
# f = file.readlines()

# newList = []

# for line in f:
#     if line[-1] == "\n":
#         newList.append(line[:-1])
#     else:
#         newList.append(line)

# print(newList)

file = open("file.txt", "w")
file.write("hello\n")
file.write("I am learning how to write to a file")
file.close()