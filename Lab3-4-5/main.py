import time
import random
from graphs import (
    generate_complete_graph,
    generate_sparse_graph,
    generate_dense_graph,
    generate_tree,
    generate_bipartite_graph,
    generate_cyclic_graph,
    generate_acyclic_graph,
    generate_grid_graph,
)
from algorithms import bfs, dfs, dijkstra, floyd_warshall, kruskal, prim

def measure_time(func, *args):
    start = time.perf_counter()
    result = func(*args)
    end = time.perf_counter()
    return end - start, result

def to_weighted(graph, directed=False, max_weight=10):
    weighted_graph = {}
    for u in range(max(graph.keys()) + 1):
        weighted_graph[u] = []
    for u in graph:
        for v in graph[u]:
            weight = random.randint(1, max_weight)
            weighted_graph[u].append((v, weight))
            if not directed:
                weighted_graph[v].append((u, weight))
    return weighted_graph

def to_edge_list(graph):
    edges = set()
    for u in graph:
        for v, w in graph[u]:
            if (v, u, w) not in edges:
                edges.add((u, v, w))
    return list(edges)

def main():
    sizes = [10, 25, 50, 100, 200, 400]
    graph_generators = {
        "complete": generate_complete_graph,
        "sparse": generate_sparse_graph,
        "dense": generate_dense_graph,
        "tree": generate_tree,
        "bipartite": lambda n: generate_bipartite_graph(n),
        "cyclic": generate_cyclic_graph,
        "acyclic": generate_acyclic_graph,
        "grid": lambda n: generate_grid_graph(int(n ** 0.5), int(n ** 0.5)),
    }

    print(f"{'Type':<10} {'Size':<6} | {'BFS':<8} {'DFS':<8} | {'Dijkstra':<10} {'Floyd-Warshall':<16} | {'Kruskal':<10} {'Prim':<10}")
    print("-" * 100)

    for name, gen_func in graph_generators.items():
        for size in sizes:
            try:
                base_graph = gen_func(size)

                bfs_time, _ = measure_time(bfs, base_graph, 0)
                dfs_time, _ = measure_time(dfs, base_graph, 0)

                directed_graph = to_weighted(base_graph, directed=True)
                dijkstra_time, _ = measure_time(dijkstra, directed_graph, 0)
                floyd_time, _ = measure_time(floyd_warshall, directed_graph)

                undirected_graph = to_weighted(base_graph, directed=False)
                edge_list = to_edge_list(undirected_graph)
                kruskal_time, _ = measure_time(kruskal, edge_list, size)
                prim_time, _ = measure_time(prim, undirected_graph, 0)

                print(f"{name:<10} {size:<6} | {bfs_time:<8.6f} {dfs_time:<8.6f} | "
                      f"{dijkstra_time:<10.6f} {floyd_time:<16.6f} | "
                      f"{kruskal_time:<10.6f} {prim_time:<10.6f}")
            except Exception as e:
                print(f"{name:<10} {size:<6} | Error: {e}")

if __name__ == "__main__":
    main()
