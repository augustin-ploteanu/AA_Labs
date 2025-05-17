import matplotlib.pyplot as plt

graph_types = [
    "complete", "sparse", "dense", "tree", "bipartite",
    "cyclic", "acyclic", "grid"
]

sizes = [10, 25, 50, 100, 200, 400]

bfs_times = {
    "complete": [0.000018, 0.000028, 0.000093, 0.000405, 0.001542, 0.006900],
    "sparse": [0.000014, 0.000013, 0.000018, 0.000069, 0.000172, 0.001251],
    "dense": [0.000016, 0.000024, 0.000069, 0.000260, 0.001122, 0.005834],
    "tree": [0.000010, 0.000011, 0.000028, 0.000045, 0.000043, 0.000094],
    "bipartite": [0.000007, 0.000014, 0.000048, 0.000114, 0.000361, 0.002487],
    "cyclic": [0.000008, 0.000012, 0.000014, 0.000041, 0.000067, 0.000131],
    "acyclic": [0.000008, 0.000006, 0.000038, 0.000105, 0.000346, 0.002008],
    "grid": [0.000014, 0.000022, 0.000021, 0.000042, 0.000073, 0.000157],
}

dfs_times = {
    "complete": [0.000010, 0.000031, 0.000098, 0.000327, 0.001471, 0.006439],
    "sparse": [0.000010, 0.000019, 0.000026, 0.000103, 0.000181, 0.000749],
    "dense": [0.000010, 0.000028, 0.000077, 0.000259, 0.001098, 0.005528],
    "tree": [0.000008, 0.000011, 0.000031, 0.000035, 0.000053, 0.000102],
    "bipartite": [0.000007, 0.000021, 0.000049, 0.000125, 0.000365, 0.002482],
    "cyclic": [0.000014, 0.000012, 0.000017, 0.000039, 0.000073, 0.000136],
    "acyclic": [0.000007, 0.000006, 0.000044, 0.000127, 0.000355, 0.001596],
    "grid": [0.000009, 0.000017, 0.000025, 0.000056, 0.000120, 0.000190],
}

dijkstra_times = {
    "complete": [0.000021, 0.000067, 0.000234, 0.001064, 0.005049, 0.015731],
    "sparse": [0.000014, 0.000058, 0.000040, 0.000200, 0.000435, 0.001772],
    "dense": [0.000018, 0.000047, 0.000160, 0.000809, 0.003595, 0.012526],
    "tree": [0.000014, 0.000017, 0.000029, 0.000104, 0.000104, 0.000208],
    "bipartite": [0.000011, 0.000053, 0.000076, 0.000272, 0.001024, 0.006114],
    "cyclic": [0.000016, 0.000021, 0.000030, 0.000051, 0.000144, 0.000287],
    "acyclic": [0.000012, 0.000014, 0.000142, 0.000245, 0.000832, 0.004033],
    "grid": [0.000017, 0.000036, 0.000105, 0.000093, 0.000182, 0.000404],
}

floyd_times = {
    "complete": [0.000150, 0.001647, 0.013172, 0.097512, 0.793611, 6.102134],
    "sparse": [0.000114, 0.001599, 0.013841, 0.104000, 0.820470, 6.206496],
    "dense": [0.000133, 0.001458, 0.012849, 0.099291, 0.809946, 6.335234],
    "tree": [0.000136, 0.001785, 0.015588, 0.122430, 0.858482, 6.581588],
    "bipartite": [0.000147, 0.001814, 0.012951, 0.110689, 0.844824, 6.562632],
    "cyclic": [0.000132, 0.002019, 0.012723, 0.114756, 0.860615, 8.758523],
    "acyclic": [0.000218, 0.002821, 0.027215, 0.191004, 1.551574, 11.906310],
    "grid": [0.000163, 0.003133, 0.023263, 0.185739, 1.378649, 7.056158],
}

kruskal_times = {
    "complete": [0.000036, 0.000191, 0.000931, 0.003169, 0.012383, 0.055565],
    "sparse": [0.000043, 0.000036, 0.000118, 0.000406, 0.001252, 0.004984],
    "dense": [0.000025, 0.000136, 0.000549, 0.002424, 0.010617, 0.045980],
    "tree": [0.000024, 0.000022, 0.000060, 0.000077, 0.000138, 0.000575],
    "bipartite": [0.000012, 0.000057, 0.000196, 0.000872, 0.003026, 0.014321],
    "cyclic": [0.000021, 0.000028, 0.000052, 0.000136, 0.000241, 0.000762],
    "acyclic": [0.000015, 0.000059, 0.000226, 0.000828, 0.003322, 0.014678],
    "grid": [0.000022, 0.000051, 0.000194, 0.000222, 0.000454, 0.000675],
}

prim_times = {
    "complete": [0.000038, 0.000227, 0.001120, 0.004808, 0.024485, 0.125589],
    "sparse": [0.000044, 0.000055, 0.000192, 0.000608, 0.001981, 0.008632],
    "dense": [0.000024, 0.000175, 0.000868, 0.004048, 0.018869, 0.096518],
    "tree": [0.000019, 0.000023, 0.000084, 0.000105, 0.000232, 0.000528],
    "bipartite": [0.000010, 0.000063, 0.000305, 0.001439, 0.005329, 0.030543],
    "cyclic": [0.000017, 0.000035, 0.000076, 0.000170, 0.000533, 0.000989],
    "acyclic": [0.000009, 0.000067, 0.000270, 0.001148, 0.004767, 0.023691],
    "grid": [0.000016, 0.000048, 0.000141, 0.000277, 0.000526, 0.000977],
}

# ----------- PLOTTING FUNCTION -----------
def plot_per_type_with_fixed_colors(title, times_a, times_b, label_a, label_b, color_a, color_b):
    plt.figure(figsize=(12, 7))

    markers = ['o', 's', 'v', '^', 'D', '*', 'P', 'X']
    marker_map = {gtype: markers[i % len(markers)] for i, gtype in enumerate(graph_types)}

    for gtype in graph_types:
        marker = marker_map[gtype]
        plt.plot(
            sizes, times_a[gtype],
            marker=marker, linestyle='-', color=color_a, alpha=0.7,
            label=f"{gtype} ({label_a})"
        )
        plt.plot(
            sizes, times_b[gtype],
            marker=marker, linestyle='--', color=color_b, alpha=0.7,
            label=f"{gtype} ({label_b})"
        )

    plt.xlabel("Number of Nodes")
    plt.ylabel("Time (seconds)")
    plt.title(title)
    plt.grid(True)
    plt.legend(ncol=2, fontsize='small', loc='upper left')
    plt.tight_layout()

    safe_title = title.lower().replace(" ", "_").replace("'", "")
    plt.savefig(f"{safe_title}.png", dpi=300)
    plt.close()

def plot_single_algorithm(title, data, color):
    plt.figure(figsize=(12, 7))

    markers = ['o', 's', 'v', '^', 'D', '*', 'P', 'X']
    marker_map = {gtype: markers[i % len(markers)] for i, gtype in enumerate(graph_types)}

    for gtype in graph_types:
        marker = marker_map[gtype]
        plt.plot(
            sizes, data[gtype],
            marker=marker, linestyle='-', color=color, alpha=0.8,
            label=gtype
        )

    plt.xlabel("Number of Nodes")
    plt.ylabel("Time (seconds)")
    plt.title(f"{title} Timing Across Graph Types")
    plt.grid(True)
    plt.legend(ncol=2, fontsize='small', loc='upper left')
    plt.tight_layout()

    safe_title = title.lower().replace(" ", "_").replace("'", "")
    plt.savefig(f"{safe_title}.png", dpi=300)
    plt.close()

# ----------- GENERATE PLOTS -----------
#plot_per_type_with_fixed_colors("BFS vs DFS", bfs_times, dfs_times, "BFS", "DFS", "red", "blue")
#plot_per_type_with_fixed_colors("Dijkstra vs Floyd-Warshall", dijkstra_times, floyd_times, "Dijkstra", "Floyd-Warshall", "red", "blue")
#plot_per_type_with_fixed_colors("Kruskal vs Prim", kruskal_times, prim_times, "Kruskal", "Prim", "red", "blue")

plot_single_algorithm("BFS", bfs_times, "blue")
plot_single_algorithm("DFS", dfs_times, "blue")
plot_single_algorithm("Dijkstra", dijkstra_times, "blue")
plot_single_algorithm("Floyd-Warshall", floyd_times, "blue")
plot_single_algorithm("Kruskal", kruskal_times, "blue")
plot_single_algorithm("Prim", prim_times, "blue")
