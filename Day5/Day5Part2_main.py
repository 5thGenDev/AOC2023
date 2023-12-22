import torch
from torch import tensor, cat, sort, empty
from .utils_part2 import find_universal_src, orgSeedRange, node_in_visited, release_child_from_visited, get_connected_nodes

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


def dfs_iterative(start_node):
    visited = []
    stack = [(start_node, None)]
    predecessor = {} # define a dict()
    target = None

    while stack:
        node, parent = stack.pop(-1)
        if not node_in_visited(visited, node):
            predecessor[node] = parent # add node : parent to dict
            visited.append(node)
            #print(f"Visiting: {node}, Parent: {parent}")

            if node[3] == 6: # equivalent of <if goal is reached>
                universal_src = find_universal_src(node, predecessor)

                seedFound = False
                for seed in seeds:
                    # seed[0] = source, seed[1] = range
                    if (universal_src == seed[0]) or \
                    (universal_src > seed[0] and seed[0] + seed[1] >= universal_src):
                        predecessor[seed] = node
                        target = seed
                        seedFound = True
                        print(f"Universal Source is : {universal_src}")
                        break
                if seedFound:
                    break
            else:
                connected_nodes = get_connected_nodes(node)
                if connected_nodes:
                    #print(f"Connected nodes of {node}: {connected_nodes} \n")
                    for next_node in connected_nodes:
                        visited = release_child_from_visited(visited, next_node)
                        if not node_in_visited(visited, next_node):
                            stack.append(tuple([next_node, node]))
                    visited.append(node)

    # construct a path backward from target -> start
    solution_path = []
    current_node = target
    while current_node is not None:
        solution_path.append(current_node)
        current_node = predecessor[current_node]
    return solution_path[::-1]

# Actually finding the right seed. The problem is treated as graph traversal but visited node can be revisited so that's the tricky part
row = (titles['humidity-to-location map:'])[0]
start_node = torch.stack((row[0], row[1], row[2], tensor(0)), dim=0)
print(dfs_iterative(start_node))
