import matplotlib.pyplot as plt
import networkx as nx

from graphs import (
    complete_graph, bipartite_graph, sparse_graph,
    dense_graph, cyclic_graph, tree_graph
)

def visualize(graph_dict, title, filename):
    G = nx.Graph()
    for node, neighbors in graph_dict.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)

    plt.figure(figsize=(6, 5))
    pos = nx.spring_layout(G, seed=42)  # Consistent layout
    nx.draw(G, pos, with_labels=True, node_color='skyblue',
            edge_color='gray', node_size=800, font_size=10)
    plt.title(title)
    plt.tight_layout()

    # Save to current directory
    plt.savefig(filename)
    print(f"Saved: {filename}")

    plt.show()

# Visualize and save each graph
visualize(complete_graph, "Complete Graph (10 nodes)", "complete_graph.png")
visualize(bipartite_graph, "Bipartite Graph (5+5 nodes)", "bipartite_graph.png")
visualize(sparse_graph, "Sparse Graph (Chain of 10 nodes)", "sparse_graph.png")
visualize(dense_graph, "Dense Graph (~70% of Complete)", "dense_graph.png")
visualize(cyclic_graph, "Cyclic Graph (Ring of 10 nodes)", "cyclic_graph.png")
visualize(tree_graph, "Tree (10 nodes, no cycles)", "tree_graph.png")
