''' This file contains all utilities functions that is necessity for part 2
'''
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

def release_child_from_visited(visited : list, child_node):
    i = 0
    while visited:
        if i > len(visited) - 1:
            break
        #print(f"{visited} with the i = {i} and len = {len(visited)}")
        visited_node = visited[i]
        if visited_node[0] == child_node[0] and visited_node[1] == child_node[1] and visited_node[2] == child_node[2]:
            visited.pop(i)
        else:
            i = i + 1
    return visited

def get_connected_nodes(node):
    connected_nodes = []
    nextIndex = node[3] + 1
    nextTitle = list(titles.keys())[nextIndex.item()]
    nextMap = titles[nextTitle]
    for row in nextMap:
        if (row[0] == node[1]) or \
        (node[1] > row[0] and row[0] + row[1] >= node[1]) or \
        (row[0] > node[1] and node[1] + node[2] >= row[0]):
            nxt_node = torch.stack((row[0], row[1], row[2], nextIndex), dim=0)
            connected_nodes.append(nxt_node)
    if connected_nodes:
        # Sort based on the first element in dimension 0
        connected_nodes = sorted(connected_nodes, key=lambda x: x[0], reverse=True)
    return connected_nodes

# Progagate universal src from final to start node (from seed -> location) 
# whenever source of current_node > destination of child_node
# final result of universal src = virtual minimum seed
# so the final condition is just to find if any seed range can cover virtual minimum seed
def find_universal_src(node, predecessor : dict):
    propagation_path = []
    current_node = node 
    universal_src = current_node[1]
    while current_node is not None:
        # propagation_path only contains child_nodes
        propagation_path.append(current_node)
        child_node = current_node
        current_node = predecessor[current_node] # get value from dict()
        if current_node is not None:
            if current_node[1] > child_node[0]:
                src = universal_src
                for successor_node in propagation_path:
                    # destination in child_node -> source in parent_node
                    src = src + (successor_node[0] - successor_node[1])
                if current_node[1] > src:
                    universal_src = universal_src + (current_node[1] - src)

    return universal_src
