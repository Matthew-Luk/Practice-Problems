fruits = ["apples", "pears","strawberries",3,8,90]
print(fruits)
fruits[1] = "blueberry"
print(fruits)

position = (2,"hello")
color = (255,255,255)
print(type(color))

for x in range(0,10):
    print(x)

for fruit in fruits:
    if fruit == "pears":
        print(fruit)
    else:
        print("not pears")

for x in range(len(fruits)):
    if fruits[x] == "pears":
        print(fruits[x])
    else:
        print("not pears")

text = input("Input something: ")
print(text)
print(len(text))
print(text.lower())
print(text.upper())
print(text.split())


fruits = ["apples", "pears","strawberries"]
text = "Hello I like python"

# print(text[3::3])
fruits[3:3] = "B"
print(fruits)