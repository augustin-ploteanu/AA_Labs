import matplotlib.pyplot as plt
import networkx as nx
from graphs import (
    generate_complete_graph,
    generate_sparse_graph,
    generate_dense_graph,
    generate_tree,
    generate_bipartite_graph,
    generate_cyclic_graph,
    generate_acyclic_graph,
    generate_grid_graph
)

# ---- Visualization ----
def ensure_networkx_graph(graph, directed=False):
    if isinstance(graph, (nx.Graph, nx.DiGraph)):
        return graph  # already a networkx graph

    # Otherwise, convert adjacency list to networkx graph
    G = nx.DiGraph() if directed else nx.Graph()
    for u in graph:
        for v in graph[u]:
            if isinstance(v, tuple):  # handle weighted edges
                G.add_edge(u, v[0], weight=v[1])
            else:
                G.add_edge(u, v)
    return G

def draw_graph(G, title, layout_func=None, directed=False):
    plt.figure(figsize=(4, 4))
    plt.title(title)

    if layout_func:
        pos = layout_func(G)
    else:
        pos = nx.spring_layout(G, seed=42)

    if directed:
        nx.draw_networkx(G, pos, node_color='lightblue', arrows=True)
    else:
        nx.draw_networkx(G, pos, node_color='lightgreen')

    plt.axis('off')
    plt.tight_layout()
    plt.show()

# ---- Main Execution ----

n = 10

graphs = [
    ("Complete Graph", generate_complete_graph(n), False),
    ("Sparse Graph", generate_sparse_graph(n), False),
    ("Dense Graph", generate_dense_graph(n), False),
    ("Tree Graph", generate_tree(n), False),
    ("Bipartite Graph", generate_bipartite_graph(n), False),
    ("Cyclic Graph", generate_cyclic_graph(n), False),
    ("Acyclic Graph (DAG)", generate_acyclic_graph(n), True),
    ("Grid Graph", generate_grid_graph(2, 5), False),
]

for title, graph_data, is_directed in graphs:
    G = ensure_networkx_graph(graph_data, directed=is_directed)
    layout = nx.spring_layout if not isinstance(G, nx.grid_2d_graph.__class__) else nx.kamada_kawai_layout
    draw_graph(G, title, layout_func=layout, directed=is_directed)