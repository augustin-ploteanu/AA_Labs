from collections import defaultdict, deque
import heapq

# ---------- BFS ----------
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    result = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            result.append(node)
            queue.extend(graph[node])
    return result

# ---------- DFS ----------
def dfs(graph, start):
    visited = set()
    stack = [start]
    result = []
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            result.append(node)
            stack.extend(reversed(graph[node]))
    return result

# ---------- Dijkstra ----------
def dijkstra(graph, start):
    heap = [(0, start)]
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    while heap:
        current_dist, current_node = heapq.heappop(heap)
        for neighbor, weight in graph[current_node]:
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))
    return distances

# ---------- Floyd-Warshall ----------
def floyd_warshall(graph):
    nodes = list(graph.keys())
    dist = {i: {j: float('inf') for j in nodes} for i in nodes}

    for node in nodes:
        dist[node][node] = 0
        for neighbor, weight in graph[node]:
            dist[node][neighbor] = weight

    for k in nodes:
        for i in nodes:
            for j in nodes:
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist

# ---------- Kruskal ----------
def kruskal(edges, num_nodes):
    parent = list(range(num_nodes))

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        rootX = find(x)
        rootY = find(y)
        if rootX != rootY:
            parent[rootY] = rootX
            return True
        return False

    mst = []
    edges.sort(key=lambda x: x[2])

    for u, v, weight in edges:
        if union(u, v):
            mst.append((u, v, weight))

    return mst

# ---------- Prim ----------
def prim(graph, start):
    visited = set()
    min_heap = [(0, start, None)]
    mst = []

    while min_heap:
        weight, node, parent = heapq.heappop(min_heap)
        if node not in visited:
            visited.add(node)
            if parent is not None:
                mst.append((parent, node, weight))
            for neighbor, edge_weight in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (edge_weight, neighbor, node))
                    
    return mst