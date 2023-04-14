# a = [1,2,3]
# b = [4,5,6]
# c = a + b
# print(c)


# a = [0,1]1
# a = a * 4
# print(a)

# a = [0,1,2,3,4,5,6]
# print(len(a))
# print(max(a))
# print(min(a))
# print(sum(a)/len(a))


total = []
while(True):
    inp = input("Enter a number: ")
    if inp == "done": break
    value = float(inp)
    total.append(value)
    average = sum(total)/len(total)

print("Average: ", average)


# a = "spam-spam1-spam2"
# b = a.split("-")
# print(b)
# print("-".join(b))

# myList = [2,4,3,1,5,7]
# myList.sort()
# print(myList)

a=[1,2,3,4,5]
print(a[3:0:-1])