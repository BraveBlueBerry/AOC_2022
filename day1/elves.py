file = open("D:\AOC_2022\day1\elves_food_list.txt", "r")

calories = [[]]
elveCounter = 0
for line in file:
    if line == "\n":
        elveCounter += 1
        calories.append([])
    else:
        calories[elveCounter].append(int(line.replace('\n', '')))

totals = []

for x in range(len(calories)) :
    totals.append(sum(calories[x]))

totals.sort(reverse=True)
print(totals)

elve1Has = totals[0]
elve2Has = totals[1]
elve3Has = totals[2]

totalCarry = elve1Has + elve2Has + elve3Has


print('The calories on the top three elve calories carriers is: {calories}'.format(calories = totalCarry))
file.close()