from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['C', 'D'],
    'C': ['D'],
    'D': ['C'],
    'E': ['F'],
    'F': ['C'],
}

def recursive_dfs(graph, node, visited=None):

    if visited is None:
        visited = []

    if node not in visited:
        visited.append(node)

    unvisited = [n for n in graph[node] if n not in visited]

    for node in unvisited:
        recursive_dfs(graph, node, visited)

    return visited

def iterative_dfs(graph, node):

    visited = []
    stack = deque()
    stack.append(node)

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            unvisited = [n for n in graph[node] if n not in visited]
            stack.extend(unvisited)

    return visited

def find_paths_dfs(graph, start, end):

    stack = deque()
    stack.append((start, [start]))

    while stack:
        (node, path) = stack.pop()
        adjacent_nodes = [n for n in graph[node] if n not in path]
        for adjacent_node in adjacent_nodes:
            if adjacent_node == end:
                yield path + [adjacent_node]
            else:
                stack.append((adjacent_node, path + [adjacent_node]))


print(recursive_dfs(graph, 'A'))
print(iterative_dfs(graph, 'A'))
print(list(find_paths_dfs(graph, 'A', 'D')))
