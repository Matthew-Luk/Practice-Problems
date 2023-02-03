def addTwo(x):
    return (x + 2)**2

def subtractTwo(number):
    return number - 2

def printString(string):
    print(string)

def accel(mass,force):
    a = mass * force
    return a

def doSomething():
    print("Hi")

newNumber = (addTwo(12))
print(subtractTwo(4))
print(newNumber)
printString("Hello my name is Matt")
print(accel(2,5))

string = input("Type something: ")
print(string.find("o"))
print(string.count("m"))
if string.count("_") > 0:
    print("Not good!")
else:
    print("Good")