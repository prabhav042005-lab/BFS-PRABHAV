from collections import deque


def bfs(graph, start):
    visited = set()
    queue = deque([start])

    visited.add(start)

    print("BFS Traversal:", end=" ")

    while queue:
        current = queue.popleft()
        print(current, end=" ")

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


# Graph representation using adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

# Starting node
start_node = 'A'

# Perform BFS
bfs(graph, start_node)