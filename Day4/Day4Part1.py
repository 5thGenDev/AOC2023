def countPoint(winningNumbers : list, ownedNumbers : list):
    point = 0
    matchedCount = 0

    for number in winningNumbers:
        if number in ownedNumbers:
            matchedCount = matchedCount + 1
            if matchedCount == 1:
                point = point + 1
            elif matchedCount > 1:
                point = point*2

    return point, matchedCount

winningNumbers = ['41', '48', '83', '86', '17']
ownedNumbers = ['83', '86',  '6', '31', '17',  '9', '48', '53']
point = countPoint(winningNumbers, ownedNumbers)
print(point)
