def MiddleAdjacentCase(TwoD_List : list, row: int, column: int):
    sweepLeft = [schematic[row][column]]    
    sweepRight = [schematic[row][column]]

    # SL will be used as finalised list to compute Digit
    # so If SL and SR are adjacent to each other, merge them
    # Or if SL can't find any number from sweeping, also merge w/ SR
    # This condition also works if neither SL or SR can find any number.
    merge = False
    if (schematic[row][column-1].isnumeric() and schematic[row][column+1].isnumeric()) or (len(sweepLeft) == 1):
        merge = True
    
    # sweep left (SL)
    i = column - 1
    while  i > - 1 and schematic[row][i].isnumeric():
        sweepLeft.insert(0, schematic[row][i])
        schematic[row][i] = '.'
        i = i - 1

    # sweep right (SR)
    i = column + 1
    while i < len(schematic[row]) and schematic[row][i].isnumeric():
        sweepRight.append(schematic[row][i])
        schematic[row][i] = '.'
        i = i + 1

    schematic[row][column] = '.' # cover first-adjacent element

    if merge:
        # item[0] is middle adjacent and is the last item in sweepLeft
        for i in range(1, len(sweepRight)): 
            sweepLeft.append(sweepRight[i])

    Digit = 0
    for i in range (len(sweepLeft)):
        Digit = Digit + int(sweepLeft[i]) * pow(10, len(sweepLeft) - i - 1)
    return Digit

schematic = [['2', '6', '3', '2', '1', '2'], 
              ['.', '.', '.', '*', '.', '.']] 
Digit = MiddleAdjacentCase(schematic, 0, 3)
print(Digit)
print(schematic)

def LeftAdjacentCase(TwoD_List : list, row: int, column: int):
    # sweep upper left (sUL)
    sweepLeft = [schematic[row][column]]    
    i = column - 1
    while i > -1 and schematic[row][i].isnumeric():
        sweepLeft.insert(0, schematic[row][i])
        schematic[row][i] = '.'
        i = i - 1
    
    schematic[row][column] = '.' # cover first-adjacent element

    Digit = 0
    for i in range (len(sweepLeft)):
        Digit = Digit + int(sweepLeft[i]) * pow(10, len(sweepLeft) - i - 1)
    return Digit

schematic = [['3', '1', '3', '.', '.', '.'], 
                      ['.', '.', '.', '*', '.', '.']] 
Digit = LeftAdjacentCase(schematic, 0, 2)

def RightAdjacentCase(TwoD_List : list, row: int, column: int):
    # sweep upper right (sUR)
    sweepRight = [schematic[row][column]]
    i = column + 1
    while i < len(schematic[row]) and schematic[row][i].isnumeric():
        sweepRight.append(schematic[row][i])
        schematic[row][i] = '.'
        i = i + 1

    schematic[row][column] = '.' # cover first-adjacent element

    Digit = 0
    for i in range (len(sweepRight)):
        Digit = Digit + int(sweepRight[i]) * pow(10, len(sweepRight) - i - 1)
    return Digit

schematic = [['.', '.', '.', '.', '1', '2'], 
              ['.', '.', '.', '*', '.', '.']] 
Digit = RightAdjacentCase(schematic, 0, 4)
print(Digit)
print(schematic)
