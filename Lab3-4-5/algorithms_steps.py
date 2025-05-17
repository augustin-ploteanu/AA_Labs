from collections import deque
import heapq

# ---------- BFS ----------
def bfs_steps(graph, start):
    visited = set()
    queue = deque([start])
    tree_edges = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                current_edge = (node, neighbor)
                if neighbor not in visited:
                    queue.append(neighbor)
                    tree_edges.append(current_edge)
                    yield tree_edges[:], current_edge
                else:
                    yield tree_edges[:], current_edge
    yield tree_edges[:], None

# ---------- DFS ----------
def dfs_steps(graph, start):
    visited = set()
    stack = [start]
    tree_edges = []

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            for neighbor in reversed(graph[node]):
                current_edge = (node, neighbor)
                if neighbor not in visited:
                    stack.append(neighbor)
                    tree_edges.append(current_edge)
                    yield tree_edges[:], current_edge
                else:
                    yield tree_edges[:], current_edge
    yield tree_edges[:], None

# ---------- Dijkstra ----------
def dijkstra_steps(graph, start):
    heap = [(0, start)]
    distances = {node: float('inf') for node in graph}
    prev = {node: None for node in graph}
    distances[start] = 0
    tree_edges = []

    while heap:
        current_dist, current_node = heapq.heappop(heap)
        for neighbor, weight in graph[current_node]:
            distance = current_dist + weight
            current_edge = (current_node, neighbor)
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                prev[neighbor] = current_node
                tree_edges.append(current_edge)
                heapq.heappush(heap, (distance, neighbor))
                yield tree_edges[:], current_edge
            else:
                yield tree_edges[:], current_edge
    yield tree_edges[:], None

# ---------- Prim ----------
def prim_steps(graph, start):
    visited = set()
    min_heap = [(0, start, None)]
    mst = []

    while min_heap:
        weight, node, parent = heapq.heappop(min_heap)
        current_edge = (parent, node) if parent is not None else None

        if node not in visited:
            visited.add(node)
            if parent is not None:
                mst.append(current_edge)
            yield mst[:], current_edge
        elif parent is not None:
            yield mst[:], current_edge

        for neighbor, edge_weight in graph[node]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (edge_weight, neighbor, node))
    yield mst[:], None

# ---------- Floyd-Warshall ----------
def floyd_warshall_steps(graph):
    nodes = list(graph.keys())
    dist = {i: {j: float('inf') for j in nodes} for i in nodes}
    for node in nodes:
        dist[node][node] = 0
        for neighbor, weight in graph[node]:
            dist[node][neighbor] = weight

    result_edges = []

    for k in nodes:
        for i in nodes:
            for j in nodes:
                old = dist[i][j]
                new = dist[i][k] + dist[k][j]
                current_edge = (i, j)
                if new < old:
                    dist[i][j] = new
                    result_edges.append(current_edge)
                    yield result_edges[:], current_edge
                else:
                    yield result_edges[:], current_edge
    yield result_edges[:], None

# ---------- Kruskal ----------
def kruskal_steps(edges, num_nodes):
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
    edges = sorted(edges, key=lambda x: x[2])

    for u, v, weight in edges:
        current_edge = (u, v)
        if union(u, v):
            mst.append(current_edge)
            yield mst[:], current_edge
        else:
            yield mst[:], current_edge
    yield mst[:], None