def powerGame(line : str):
    _, bag = line.split(":")
    subsets = bag.split(";")

    # problem described "fewest # cubes of each color [in a given bag]"
    # but examples listed "highest # cubes of each color [in a given bag]"
    redCount = 0
    blueCount = 0
    greenCount = 0
    for subset in subsets:
        colors = subset.split(",")
        for color in colors:
            if color.find("blue") != -1:
                if int(color.split(" ")[1]) > blueCount:
                    blueCount = int(color.split(" ")[1])
            elif color.find("red") != -1:
                if int(color.split(" ")[1]) > redCount:
                    redCount = int(color.split(" ")[1])
            elif color.find("green") != -1:
                if int(color.split(" ")[1]) > greenCount:
                    greenCount = int(color.split(" ")[1])
    
    return greenCount*redCount*blueCount