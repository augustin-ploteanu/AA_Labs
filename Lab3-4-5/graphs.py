from collections import defaultdict

def create_graph(edge_list):
    graph = defaultdict(list)
    for u, v in edge_list:
        graph[u].append(v)
        graph[v].append(u)  # Undirected
    return graph

# 1. Complete Graph (K10) — every node connected to every other
complete_edges = [(i, j) for i in range(10) for j in range(i+1, 10)]
complete_graph = create_graph(complete_edges)

# 2. Bipartite Graph — two sets of 5 nodes each, edges only between sets
bipartite_edges = [(i, j) for i in range(5) for j in range(5, 10)]
bipartite_graph = create_graph(bipartite_edges)

# 3. Sparse Graph — 10 nodes, connected, lightly branched (15 edges)
sparse_edges = [
    (0, 1), (1, 2), (2, 3),
    (3, 4), (4, 5), (5, 6),
    (2, 7), (7, 8), (8, 9),
    (0, 9),  # shortcut
    (3, 7),  # cross connection
    (1, 6),  # cross connection
    (4, 8),  # cross connection
    (5, 9),  # new edge
    (0, 3)   # new edge
]
sparse_graph = create_graph(sparse_edges)

# 4. Dense Graph — not complete, but lots of edges (e.g., 70% of K10)
dense_edges = []
nodes = list(range(10))
for i in range(10):
    for j in range(i+1, 10):
        if len(dense_edges) < int(0.7 * 45):  # 45 = C(10,2)
            dense_edges.append((i, j))
dense_graph = create_graph(dense_edges)

# 5. Cyclic Graph — like a ring
cyclic_edges = [(i, (i+1) % 10) for i in range(10)]
cyclic_graph = create_graph(cyclic_edges)

# 6. Tree — 10 nodes, no cycles
# Example: binary-ish tree structure
tree_edges = [
    (0, 1), (0, 2),
    (1, 3), (1, 4),
    (2, 5), (2, 6),
    (3, 7), (4, 8), (5, 9)
]
tree_graph = create_graph(tree_edges)
