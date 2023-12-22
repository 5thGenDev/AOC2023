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
