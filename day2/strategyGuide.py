from posixpath import split


points = {
    "X" : 0, #lose
    "Y" : 3, #draw
    "Z" : 6  #win
}

outcomePoints = {
    "rock"      : 1,
    "paper"     : 2,
    "scissor"   : 3
}

def get_points(oChoice, yChoice):
    totalPoints = 0

    #draw
    if oChoice == "A" and yChoice == "Y":
        totalPoints += outcomePoints["rock"]
    if oChoice == "B" and yChoice == "Y":
        totalPoints += outcomePoints["paper"]
    if oChoice == "C" and yChoice == "Y":
        totalPoints += outcomePoints["scissor"]
    
    #win
    if oChoice == "A" and yChoice == "Z":
        totalPoints += outcomePoints["paper"]
    if oChoice == "B" and yChoice == "Z":
        totalPoints += outcomePoints["scissor"]
    if oChoice == "C" and yChoice == "Z":
        totalPoints += outcomePoints["rock"]

    #lose
    if oChoice == "A" and yChoice == "X":
        totalPoints += outcomePoints["scissor"]
    if oChoice == "B" and yChoice == "X":
        totalPoints += outcomePoints["rock"]
    if oChoice == "C" and yChoice == "X":
        totalPoints += outcomePoints["paper"]
    
    return totalPoints + points[yChoice]


strategyGuide = {
    "A" : "Y",  #Rock - Paper
    "B" : "X",  #Paper - Rock
    "C" : "Z",   #Scissors - Scissors
}

# print(strategyGuide)

file = open("D:\AOC_2022\day2\strategyguide.txt", "r")


totalPoints = 0

for line in file:
    # print(line)
    if(line == "\n"):
        continue
    splitLine = line.split()
    totalPoints += get_points(splitLine[0], splitLine[1])


file.close()


# for o, y in strategyGuide.items():
#     totalPoints += get_points(o, y)

print("Total points with this strategy: " + str(totalPoints))
