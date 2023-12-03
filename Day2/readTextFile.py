file1 = open('gameID.txt', 'r')
Lines = file1.readlines()

# sumID for part 1, sumPower for part 2. it's just var name so doesn't matter
sumID = 0
for line in Lines:
    sumID = sumID + possibleGame(line)
print(sumID)
