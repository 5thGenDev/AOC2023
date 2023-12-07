# schematic = nested of 2 lists containing string (or 2D list)
schematic = []

def lineToSchematic(line : str):
    noNewLineSymbol = list(filter(lambda x : x != '\n', [*line]))
    schematic.append(noNewLineSymbol)

file1 = open('engineParts.txt', 'r')
Lines = file1.readlines()
""" ------- index all occurrences of all symbols in each line --------- """
symbols = ['*']
coordSymbols = [] 
row = 0
for line in Lines:
    lineToSchematic(line)
    column =  0
    for symbol in symbols:
        while column != -1:
            column = line.find(symbol, column)
            if column != -1:
                coordSymbols.append((row, column))
                column = column + 1
        column = 0
    row = row + 1

total = gearRatios(schematic, coordSymbols)
print(total)
