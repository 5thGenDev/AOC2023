def node_in_visited(visited : list, child_node, parent_node):
    if visited:
        parent_in_visited = False
        for node in visited:
            if node[0] == parent_node[0] and node[1] == parent_node[1] and node[2] == parent_node[2]:
                parent_in_visited = True   
                break
        if not parent_in_visited:
            for i in range(len(visited)):
                node = visited[i]
                if node[0] == child_node[0] and node[1] == child_node[1] and node[2] == child_node[2]:
                    visited.pop(i)
                    break

        for node in visited:
            if node[0] == child_node[0] and node[1] == child_node[1] and node[2] == child_node[2]:
                return True, visited
                break
    return False, visited
