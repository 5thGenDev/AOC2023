def copyScratchCards(matchedCount: int, cardInstances : list, index: int):
    cardInstances[index] = cardInstances[index] + 1
    
    # only add up copies beyond this line of code
    for instance in range (cardInstances[index]): 
        for i in range(1, matchedCount + 1):
            cardInstances[index + i] = cardInstances[index  + i] + 1
    
    return cardInstances
