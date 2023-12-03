def possibleGame(line : str):
    gameID, bag = line.split(":")
    subsets = bag.split(";")

    for subset in subsets:
        colors = subset.split(",")
        for color in colors:
            if color.find("blue") != -1:
                if int(color.split(" ")[1]) > 14:
                    return 0
            elif color.find("red") != -1:
                if int(color.split(" ")[1]) > 12:
                    return 0
            elif color.find("green") != -1:
                if int(color.split(" ")[1]) > 13:
                    return 0
    
    return int(gameID.split(" ")[1])