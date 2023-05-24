
def dfs(visited, graph, node, key):

    if key in visited:
        return True
    if node not in visited:
        visited.add(node)

        print("visited", visited)
        print("node", node)
        for neightbour in graph[node]:
            dfs(visited, graph, neightbour, key)
    else:
        return False

# def dfs(node, data):
#     if node is None:
#         return False
#     if node.data == data:
#         return True
#     for ne in graph[node]:
#         return dfs(ne, data)


# Driver Code
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
node = '1'
visited = set()
# g = Graph(graph, node, visited)
result = dfs(visited, graph, node, '3')

print(result)
