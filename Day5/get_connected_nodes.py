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
