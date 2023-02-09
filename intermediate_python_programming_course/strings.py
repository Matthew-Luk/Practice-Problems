# Strings: ordered, immutable, text representation

mystring = """Hello \
World"""
print(mystring)

mystring2 = "Hello World"
char = mystring2[-1]
substring2 = mystring2[::-1]
print(substring2)

greeting = "Hello"
name = "Matt"
sentence = greeting + " " + name
print(sentence)

for i in greeting:
    print(i)

if "ell" in greeting:
    print("yes")
else:
    print("no")

mystring3 = "   Hello World   "
mystring3 = mystring3.strip()
print(mystring3.upper())
print(mystring3.lower())
print(mystring3.startswith("Hello"))
print(mystring3.endswith("World"))
print(mystring3.find("lo"))
print(mystring3.count("o"))
print(mystring3.replace("World", "Universe"))
print(mystring3)

mystring4 = "how,are,you,doing"
mylist = mystring4.split(",")
newstring = "".join(mylist)
print(mylist)
print(newstring)

from timeit import default_timer as timer

mylist2 = ["a"] * 10
print(mylist2)

# bad code very expensive
start = timer()
mystring5 = ""
for i in mylist2:
    mystring5 += i
print(mystring5)
stop = timer()
print(stop-start)

# good code, cleaner and faster
start = timer()
mystring6 = "".join(mylist2)
print(mystring6)
stop = timer()
print(stop-start)

var = "Matt"
var2 = 3
var3 = 4.1231239017
mystring7 = "the variable is %s" % var
mystring8 = "the variable is %d" % var2
mystring9 = "the variable is %.2f" % var3

mystring10 = "the variable is {}".format(var)
mystring11 = "the variable is {}".format(var2)
mystring12 = "the variable is {:.2f} and {}".format(var3,var)

mystring13 = f"the variable is {var}"
mystring14 = f"the variable is {var2}"
mystring15 = f"the variable is {var3}"

print(mystring15)