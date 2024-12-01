import matplotlib.pyplot as plt
import networkx as nx

file = open("input.txt", "r")
text = file.read().strip()
lines = text.splitlines()


def part1(lines):
    nodes = [line.split(": ")[0] for line in lines]
    connections = [line.split(": ")[1].split() for line in lines]

    G = nx.Graph()
    for node, connection in zip(nodes, connections):
        for node2 in connection:
            G.add_edge(node, node2)

    nx.draw(G, with_labels=True)
    plt.show()

    # Seen from graph
    G.remove_edge("hbr", "sds")
    G.remove_edge("pzv", "xft")
    G.remove_edge("dqf", "cbx")

    nx.draw(G, with_labels=True)
    plt.show()

    product = 1
    for g in nx.connected_components(G):
        product *= len(g)

    return product


print("Solution 1: ", part1(lines))
