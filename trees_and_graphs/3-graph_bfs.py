from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['C', 'D'],
    'C': ['D'],
    'D': ['C'],
    'E': ['F'],
    'F': ['C'],
}

def iterative_bfs(graph, start):
 
    visited = []
    queue = deque()
    queue.append(start)

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            unvisited = [n for n in graph[node] if n not in visited]
            queue.extend(unvisited)

    return visited

def find_paths_bfs(graph, start, end):

    queue = deque()
    queue.append((start, [start]))

    while queue:
        node, path = queue.popleft()
        adjacent_nodes = [n for n in graph[node] if n not in path]
        for adjacent_node in adjacent_nodes:
            if adjacent_node == end:
                yield path + [adjacent_node]
            else:
                queue.append((adjacent_node, path + [adjacent_node]))

print(iterative_bfs(graph, 'A'))
print(list(find_paths_bfs(graph, 'A', 'D')))
