age = input("What is your age?: ")

if int(age) >= 16:
    print("Hey you're older than 16")
else:
    print("You're younger than 16")

height = input("How tall are you?: ")

if float(height) <= 1:
    print("you cannot ride, under 1 meter")
elif float(height) == 5:
    print("wow you are tall")
elif float(height) >= 2:
    print("you cannot ride, over 2 meters")
else:
    print("you can ride")


x = 2
y = 5
if not(x == y or x + y == 6):
    print("ran")
else:
    print(":(")

if x == 2:
    if y == 3:
        print("x = 2, y = 3")
    else:
        print("x = 2, y != 3")
else:
    print("x != 2")