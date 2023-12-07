def sumEngineParts(schematic : list, coordSymbols: list):
    """
    schematic = 2D-list
    coordSymbols = 1D-list
    """
    engineParts = 0

    # check any number adjacent to special symbol
    for row, column in coordSymbols:
        # Middle adjacent case
        if row != 0:
            if schematic[row-1][column].isnumeric():
                engineParts = engineParts + MiddleAdjacentCase(schematic, row-1, column) 
        if row < len(schematic) - 1: 
            if schematic[row+1][column].isnumeric():
                engineParts = engineParts + MiddleAdjacentCase(schematic, row+1, column)

        # Left adjacent case
        if column != 0:
            if schematic[row][column-1].isnumeric():
                engineParts = engineParts +LeftAdjacentCase(schematic, row, column-1)
            if row != 0:
                if schematic[row-1][column-1].isnumeric():
                    engineParts = engineParts + LeftAdjacentCase(schematic, row-1, column-1)
            if row < len(schematic) - 1:
                if schematic[row+1][column-1].isnumeric():
                    engineParts = engineParts + LeftAdjacentCase(schematic, row+1, column-1)

        # Right adjacent case
        if column < len(schematic[row]) - 1:
            if schematic[row][column+1].isnumeric():
                engineParts = engineParts + RightAdjacentCase(schematic, row, column+1)
            if row != 0:
                if schematic[row-1][column+1].isnumeric():
                    engineParts = engineParts + RightAdjacentCase(schematic, row-1, column+1)
            if row < len(schematic) - 1:
                if schematic[row+1][column+1].isnumeric():
                    engineParts = engineParts + RightAdjacentCase(schematic, row+1, column+1)
    
    return engineParts
