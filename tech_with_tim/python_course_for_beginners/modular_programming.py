# # Modular Programming
# import math
# import myModule

# print(math.radians(60))
# print(myModule.myFunc(6))
# print(myModule.anotherFunc(10192831293))


# # Optional Parameters
# def func(x=3,text="2"):
#     print(x)
#     if text == "1":
#         print("Text is 1")
#     else:
#         print(text)

# func(3,"5")

# # Try and Except
# text = input("Username: ")
# try:
#     number = int(text)
#     print(number)
# except:
#     print("Invalid username")


# Global vs Local variables
var = 9
loop = True

def func(x):
    global loop
    loop = 7

    if x == 5:
        return x

def otherFunc():
    newVar = 5

func(2)
print(loop)