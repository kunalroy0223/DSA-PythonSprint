# --------------------------------------------------------  
# Task 1: Depth-First Search (DFS)  
# --------------------------------------------------------  

print('...................................Depth-First Search (DFS)...................................')

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=" ")  # Print the current node

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Sample graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
print("DFS Traversal:")
dfs(graph, 'A')
print()

# --------------------------------------------------------  
# Task 2: Breadth-First Search (BFS)  
# --------------------------------------------------------  

print('...................................Breadth-First Search (BFS)...................................')

from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=" ")  # Print the current node

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

print("BFS Traversal:")
bfs(graph, 'A')
print()

# --------------------------------------------------------  
# Task 3: Dijkstra's Algorithm  
# --------------------------------------------------------  

print('...................................Dijkstra\'s Algorithm...................................')

import heapq

def dijkstra(graph, start):
    # Priority queue to store (distance, node) pairs
    pq = [(0, start)]
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

# Sample weighted graph represented as an adjacency list
weighted_graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'D': 2, 'E': 5},
    'C': {'A': 4, 'F': 3},
    'D': {'B': 2},
    'E': {'B': 5, 'F': 1},
    'F': {'C': 3, 'E': 1}
}

print("Shortest distances from node A:")
print(dijkstra(weighted_graph, 'A'))

# --------------------------------------------------------  
# Task 4: Practical Use Case - Detecting Cycles in a Graph  
# --------------------------------------------------------  

print('...................................Detecting Cycles in a Graph...................................')

def has_cycle(graph, node, visited, parent):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            if has_cycle(graph, neighbor, visited, node):
                return True
        elif parent != neighbor:
            return True
    return False

# Sample graph with no cycle
graph_no_cycle = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A'],
    'D': ['B']
}

# Sample graph with a cycle
graph_with_cycle = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}

visited = set()
print("Graph with no cycle:")
print("Cycle detected?" if has_cycle(graph_no_cycle, 'A', visited, None) else "No cycle detected")

visited = set()
print("Graph with cycle:")
print("Cycle detected?" if has_cycle(graph_with_cycle, 'A', visited, None) else "No cycle detected")

print('...................................Detecting Cycles in a Graph...................................')

