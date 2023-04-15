numDays = int(input("How many day's temperature?: "))
total = 0
temp = []
for i in range(numDays):
    nextDay = int(input("Day " + str(i+1) + "'s high temp:"))
    temp.append(nextDay)
    total += temp[i]

average = round(sum(temp) / len(temp), 2)


above = 0
for i in temp:
    if i > average:
        above += 1


print("Average = " + str(average) + "Days above average = " + str(above))