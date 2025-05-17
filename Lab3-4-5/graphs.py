import random
from collections import defaultdict

def generate_complete_graph(n):
    graph = defaultdict(list)
    for i in range(n):
        for j in range(n):
            if i != j:
                graph[i].append(j)
    return graph

def generate_sparse_graph(n):
    graph = defaultdict(list)
    for i in range(n - 1):
        graph[i].append(i + 1)
        graph[i + 1].append(i)
    for i in range(n):
        for j in range(i + 1, n):
            if j not in graph[i] and random.random() < 0.1:
                graph[i].append(j)
                graph[j].append(i)

    return graph


def generate_dense_graph(n):
    graph = defaultdict(list)
    for i in range(n):
        for j in range(i + 1, n):
            if random.random() < 0.8:
                graph[i].append(j)
                graph[j].append(i)
    return graph

def generate_tree(n):
    graph = defaultdict(list)
    for i in range(1, n):
        parent = random.randint(0, i - 1)
        graph[parent].append(i)
        graph[i].append(parent)
    return graph

def generate_bipartite_graph(n):
    graph = defaultdict(list)
    left = set(range(n // 2))
    right = set(range(n // 2, n))
    for u in left:
        connections = random.sample(sorted(right), random.randint(1, len(right)))
        for v in connections:
            graph[u].append(v)
            graph[v].append(u)
    return graph

def generate_cyclic_graph(n, extra_edges=None):
    graph = generate_tree(n)
    if extra_edges is None:
        extra_edges = n // 2
    added = 0
    while added < extra_edges:
        u, v = random.sample(range(n), 2)
        if v not in graph[u]:
            graph[u].append(v)
            graph[v].append(u)
            added += 1
    return graph

def generate_acyclic_graph(n):
    graph = defaultdict(list)
    for i in range(n):
        graph[i] = []
    for i in range(n):
        for j in range(i + 1, n):
            if random.random() < 0.3:
                graph[i].append(j)
    return graph  # This is a DAG (Directed Acyclic Graph)

def generate_grid_graph(rows, cols):
    graph = defaultdict(list)
    for r in range(rows):
        for c in range(cols):
            node = r * cols + c
            if c < cols - 1:
                right = node + 1
                graph[node].append(right)
                graph[right].append(node)
            if r < rows - 1:
                down = node + cols
                graph[node].append(down)
                graph[down].append(node)
    return graph

def generate_weighted_graph(n, edge_prob=0.5, max_weight=10):
    graph = defaultdict(list)
    for i in range(n):
        for j in range(i + 1, n):
            if random.random() < edge_prob:
                weight = random.randint(1, max_weight)
                graph[i].append((j, weight))
                graph[j].append((i, weight))
    return graph

def generate_directed_graph(n, edge_prob=0.3):
    graph = defaultdict(list)
    for i in range(n):
        for j in range(n):
            if i != j and random.random() < edge_prob:
                graph[i].append(j)
    return graph
