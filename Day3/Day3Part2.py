import numpy as np 

def gearRatios(schematic : list, coordSymbols: list):
    """
    schematic = 2D-list
    coordSymbols = 1D-list
    """
    gearRatios = 0

    # check any number adjacent to special symbol
    for row, column in coordSymbols:
        adjacentParts = []
        # Middle adjacent case
        if row != 0:
            if schematic[row-1][column].isnumeric():
                enginePart = MiddleAdjacentCase(schematic, row-1, column) 
                if enginePart > 0:
                    adjacentParts.append(enginePart)
        if row < len(schematic) - 1: 
            if schematic[row+1][column].isnumeric():
                enginePart = MiddleAdjacentCase(schematic, row+1, column)
                if enginePart > 0:
                    adjacentParts.append(enginePart)

        # Left adjacent case
        if column != 0:
            if schematic[row][column-1].isnumeric():
                enginePart = LeftAdjacentCase(schematic, row, column-1)
                if enginePart > 0:
                    adjacentParts.append(enginePart)
            if row != 0:
                if schematic[row-1][column-1].isnumeric():
                    enginePart = LeftAdjacentCase(schematic, row-1, column-1)
                    if enginePart > 0:
                        adjacentParts.append(enginePart)
            if row < len(schematic) - 1:
                if schematic[row+1][column-1].isnumeric():
                    enginePart = LeftAdjacentCase(schematic, row+1, column-1)
                    if enginePart > 0:
                        adjacentParts.append(enginePart)

        # Right adjacent case
        if column < len(schematic[row]) - 1:
            if schematic[row][column+1].isnumeric():
                enginePart = RightAdjacentCase(schematic, row, column+1)
                if enginePart > 0:
                    adjacentParts.append(enginePart)
            if row != 0:
                if schematic[row-1][column+1].isnumeric():
                    enginePart = RightAdjacentCase(schematic, row-1, column+1)
                    if enginePart > 0:
                        adjacentParts.append(enginePart)
            if row < len(schematic) - 1:
                if schematic[row+1][column+1].isnumeric():
                    enginePart = RightAdjacentCase(schematic, row+1, column+1)
                    if enginePart > 0:
                        adjacentParts.append(enginePart)

        if len(adjacentParts) > 1:
            #print(adjacentParts)
            gearRatios = gearRatios + np.prod(adjacentParts)
    
    return gearRatios
