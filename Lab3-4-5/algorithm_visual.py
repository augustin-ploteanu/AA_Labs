import matplotlib.pyplot as plt
import matplotlib.animation as animation
import networkx as nx
from algorithms_steps import (
    bfs_steps, dfs_steps, dijkstra_steps, prim_steps,
    floyd_warshall_steps, kruskal_steps
)

# ---- Graph Setup ----
pos = {
    0: (0, 1),
    1: (1, 2),
    2: (2, 1),
    3: (1, 0),
    4: (2, 0),
}

edges = [
    (0, 1, 2),
    (0, 3, 1),
    (1, 2, 4),
    (2, 4, 3),
    (3, 4, 2),
    (1, 3, 3),
]

# Build undirected NetworkX graph for visualization
G = nx.Graph()
G.add_weighted_edges_from(edges)

# Adjacency list with weights (for algorithms needing weights)
adj_list = {node: [] for node in G.nodes}
for u, v, w in edges:
    adj_list[u].append((v, w))
    adj_list[v].append((u, w))  # undirected

# Unweighted adjacency list (for BFS & DFS only)
unweighted_adj_list = {u: [v for v, _ in neighbors] for u, neighbors in adj_list.items()}

# ---- Drawing Helper ----
def draw_frame(G, ax, edges, title, color):
    ax.clear()
    ax.set_title(title)
    ax.axis("off")
    nx.draw(G, pos, with_labels=True, node_color='lightgray', node_size=800,
            edge_color='lightgray', ax=ax)
    nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color=color, width=2, ax=ax)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, ax=ax)

# ---- Animation Function ----
def animate(title, step_generator, color_final="green", color_current="red"):
    fig, ax = plt.subplots(figsize=(6, 5))

    # Ensure each frame has (accepted_edges, current_edge)
    steps = list(step_generator)

    def update(frame):
        ax.clear()
        ax.set_title(title)
        ax.axis("off")

        accepted_edges, current_edge = steps[frame]
        nx.draw(G, pos, with_labels=True, node_color='lightgray', node_size=800,
                edge_color='lightgray', ax=ax)

        # Draw accepted edges
        nx.draw_networkx_edges(G, pos, edgelist=accepted_edges, edge_color=color_final, width=2, ax=ax)

        # Draw current edge in red
        if current_edge:
            nx.draw_networkx_edges(G, pos, edgelist=[current_edge], edge_color=color_current, width=2.5, ax=ax, style="dashed")

        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, ax=ax)

    ani = animation.FuncAnimation(fig, update, frames=len(steps), interval=800, repeat=False)
    plt.show()

animate("BFS Animation", bfs_steps(unweighted_adj_list, 0))
animate("DFS Animation", dfs_steps(unweighted_adj_list, 0))
animate("Dijkstra Animation", dijkstra_steps(adj_list, 0))
animate("Prim Animation", prim_steps(adj_list, 0))
#animate("Floyd-Warshall Animation", floyd_warshall_steps(adj_list))
animate("Kruskal Animation", kruskal_steps(edges, 5))
