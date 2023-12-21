def dfs_iterative(start_node):
    visited = []
    stack = [(start_node, None)]
    predecessor = {} # define a dict()
    target = None

    while stack:
        node, parent = stack.pop(-1)
        node_visited, visited = node_in_visited(visited, node, parent)
        if not node_in_visited(visited, node, parent):
            predecessor[node] = parent # add node : parent to dict
            print(f"Visiting: {node}, Parent: {parent}")

            if node[3] == 6: # equivalent of <if goal is reached>
                # Progagate universal src from final to start node (from seed -> location)
                # whenever source of current_node > destination of child_node
                # final result of universal src = virtual minimum seed 
                propagation_path = []
                current_node = node 
                universal_src = current_node[1]
                while current_node is not None:
                    # notice how propagation_path only contains child_nodes
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
            
                #print(f"Universal Source is : {universal_src}")

                seedFound = False
                for seed in seeds:
                    # seed[0] = source, seed[1] = range
                    if (universal_src == seed[0]) or \
                    (universal_src > seed[0] and seed[0] + seed[1] >= universal_src):
                        predecessor[seed] = node
                        target = seed
                        seedFound = True
                        print("\n \nTarget reach")
                        break
                if seedFound:
                    break
            else:
                connected_nodes = get_connected_nodes(node)
                if not connected_nodes:
                    visited.append(node)
                if connected_nodes:
                    print(f"Connected nodes of {node}: {connected_nodes} \n")
                    for next_node in connected_nodes:
                        next_node_visited, visited = node_in_visited(visited, next_node, node)
                        if not next_node_visited:
                            stack.append(tuple([next_node, node]))
                    visited.append(node)

    # construct a path backward from target -> start
    solution_path = []
    current_node = target
    while current_node is not None:
        solution_path.append(current_node)
        current_node = predecessor[current_node]
    return solution_path[::-1]
