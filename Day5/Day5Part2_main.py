import torch
from torch import tensor, cat, sort, empty

humid_location = empty((0,3), dtype=torch.int8)
temp_humid = empty((0,3), dtype=torch.int8)
light_temp =empty((0,3), dtype=torch.int8)
water_light = empty((0,3), dtype=torch.int8)
fert_water = empty((0,3), dtype=torch.int8)
soil_fert = empty((0,3), dtype=torch.int8)
seed_soil = empty((0,3), dtype=torch.int8)

# Titles must be manually preordered in reverse w.r.t text file
titles = {
    'humidity-to-location map:' : humid_location,
    'temperature-to-humidity map:' : temp_humid,
    'light-to-temperature map:' : light_temp,
    'water-to-light map:' : water_light,
    'fertilizer-to-water map:' : fert_water,
    'soil-to-fertilizer map:' : soil_fert,
    'seed-to-soil map:' : seed_soil
}

seeds = []

scanNumber = False
currentTitle = ""
file1 = open('demo.txt', 'r')
Lines = file1.readlines()

# Convert seed line into a list of tuple (for part 2)
# Convert each map into 2D tensor
for line in Lines:
    line = line.split("\n")[0]
    if line == '':
        continue
    elif line in titles.keys():
        currentTitle = line
    elif line[0:5] == "seeds":
        seedNumbers = line.split("seeds: ")[1]
        seeds = orgSeedRange(seedNumbers)

    elif line[0].isnumeric():
        x = tensor([list(map(int, line.split(' ')))])
        titles[currentTitle] = cat((titles[currentTitle], x), dim=0)

# Filling the gaps in each map
for title in titles.keys():
    x = titles[title]
    sorted_values, sorted_indices = torch.sort(x[:, 0])
    x = x[sorted_indices]
    titles[title] = x
    if x[0,0] != 0:
        new_row = tensor([[0,0, x[0,0]]])
        titles[title] = cat((new_row, titles[title]), dim=0)
    new_row = tensor([[x[-1,0] + x[-1,2], x[-1,0] + x[-1,2], 1000]])
    titles[title] = cat((titles[title], new_row), dim=0)

# Actually finding the right seed. The problem is treated as graph traversal but visited node can be revisited so that's the tricky part
row = (titles['humidity-to-location map:'])[0]
start_node = torch.stack((row[0], row[1], row[2], tensor(0)), dim=0)
print(dfs_iterative(start_node))
