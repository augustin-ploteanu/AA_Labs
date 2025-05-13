import time
from statistics import mean
from algorithms import bfs, dfs, dijkstra, floyd_warshall, kruskal, prim
from graphs import (
    complete_graph, bipartite_graph, sparse_graph,
    dense_graph, cyclic_graph, tree_graph
)

graphs = {
    "Complete Graph": complete_graph,
    "Bipartite Graph": bipartite_graph,
    "Sparse Graph": sparse_graph,
    "Dense Graph": dense_graph,
    "Cyclic Graph": cyclic_graph,
    "Tree Graph": tree_graph
}

def average_time(func, graph, nodes, is_weighted=False):
    times = []
    for start_node in nodes:
        args = (graph, start_node) if not is_weighted else (graph, start_node)
        start = time.time()
        func(*args)
        end = time.time()
        times.append(end - start)
    return mean(times)

def run_all_algorithms(graph_dict, graph_name):
    print(f"\n--- {graph_name} ---")

    # Get 10 unique start nodes (filter out isolated ones)
    all_nodes = [n for n, neighbors in graph_dict.items() if neighbors]
    start_nodes = all_nodes[:10] if len(all_nodes) >= 10 else all_nodes

    if not start_nodes:
        print("Graph is empty or all nodes are isolated.")
        return

    # BFS and DFS
    print(f"BFS Avg Time: {average_time(bfs, graph_dict, start_nodes):.6f} s")
    print(f"DFS Avg Time: {average_time(dfs, graph_dict, start_nodes):.6f} s")

    # Convert to weighted format for Dijkstra, Floyd-Warshall, Prim
    weighted_graph = {
        node: [(neighbor, 1) for neighbor in neighbors]
        for node, neighbors in graph_dict.items()
    }

    print(f"Dijkstra Avg Time: {average_time(dijkstra, weighted_graph, start_nodes, is_weighted=True):.6f} s")
    print(f"Floyd-Warshall Avg Time: {average_time(lambda g, _: floyd_warshall(g), weighted_graph, start_nodes):.6f} s")

    # Kruskal: same input every time
    edge_list = []
    added = set()
    for u in graph_dict:
        for v in graph_dict[u]:
            if (v, u) not in added:
                edge_list.append((u, v, 1))
                added.add((u, v))

    num_nodes = len(graph_dict)
    print(f"Kruskal Avg Time: {average_time(lambda e, _: kruskal(e, num_nodes), edge_list, start_nodes):.6f} s")
    print(f"Prim Avg Time: {average_time(prim, weighted_graph, start_nodes, is_weighted=True):.6f} s")

# Run benchmarks on all graphs
for name, g in graphs.items():
    run_all_algorithms(dict(g), name)