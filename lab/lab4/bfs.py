
graph = {
    '1': ['2', '3', '4'],
    '2': ['5', '6'],
    '3': [],
    '4': ['7', '8'],
    '5': ['9', '10'],
    '6': [],
    '7': ['11', '12'],
    '8': [],
    '9': [],
    '10': [],
    '11': [],
    '12': []

}

visited = []  # List for visited nodes.
queue = []  # Initialize a queue


def bfs(visited, graph, node, key):  # function for BFS
    visited.append(node)
    queue.append(node)

    while queue:          # Creating loop to visit each node
        m = queue.pop(0)
        print(m, end=" ")
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

    if key in visited:
        return True
    else:
        return False


# Driver Code
node = 1

bfs(visited, graph, node, '8')    # function calling
