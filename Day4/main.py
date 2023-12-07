file1 = open('scratchedCards.txt', 'r')
Lines = file1.readlines()

totalPoint = 0
cardInstances = [0] * 208 # there are 208 cardID
index = 0

for line in Lines:
    line = line.split("\n")
    _, numbers = line[0].split(":")
    winningNumbers, ownedNumbers = numbers.split("|")
    winningNumbers = list(filter(lambda x : x != "", winningNumbers.split(" ")))  
    ownedNumbers = list(filter(lambda x :x != "", ownedNumbers.split(" ")))
    point, matchedCount = countPoint(winningNumbers, ownedNumbers)
    totalPoint = totalPoint + point
    cardInstances = copyScratchCards(matchedCount, cardInstances, index)
    index = index + 1

# for part 1
#print(totalPoint) 

# for part 2
totalScratchCards = 0
print(cardInstances)
for i in cardInstances:
    totalScratchCards = totalScratchCards + i
print(totalScratchCards)
