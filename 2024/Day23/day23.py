from itertools import combinations
import networkx as nx

file = open('input.txt', 'r')
text = file.read().strip()


def part1(text: str):
    # Create graph from input
    G = nx.Graph()
    for line in text.splitlines():
        start, end = line.strip().split('-')
        G.add_edge(start, end)

    # Find all cliques and filter for triangles
    cliques = nx.enumerate_all_cliques(G)
    result = 0
    for clique in cliques:
        if len(clique) == 3 and any(n.startswith('t') for n in clique):
            result += 1
    return result


def part2(text: str):
    lines = text.splitlines()
    connections = [line.split('-') for line in lines]

    G = nx.Graph()
    for start, end in connections:
        G.add_edge(start, end)

    best_clique = []
    cliques = nx.enumerate_all_cliques(G)
    for clique in cliques:
        if len(clique) > len(best_clique):
            best_clique = clique
    return ','.join(sorted(best_clique))


print('Solution 1:', part1(text))
print('Solution 2:', part2(text))
