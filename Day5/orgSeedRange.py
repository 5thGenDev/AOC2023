import torch
from torch import tensor

# line = "seeds: 79 14 55 13"
# line = line.split("seeds: ")[1]
def orgSeedRange(seedNumbers : str):
    numbers = list(map(int, seedNumbers.split(" ")))
    numbers = list(map(tensor, numbers))
    seeds = []
    for i in range(len(numbers) - 1):
        if i % 2 == 0:
            if numbers[i].numel() and numbers[i+1].numel():
                seeds.append((numbers[i], numbers[i+1]))

    seeds.sort()
    return seeds

# print(orgSeedRange(line))
