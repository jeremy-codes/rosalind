"""Solution for Algorithmic Heights Problem ID: DEG

Problem Title: Degree Array
Link: http://rosalind.info/problems/deg
"""

def construct_neighbour_tree(edges):
    tree = {}

    for edge in edges:
        if edge[0] not in tree.keys():
            tree[edge[0]] = []
        if edge[1] not in tree.keys():
            tree[edge[1]] = []

        tree[edge[0]].append(edge[1])
        tree[edge[1]].append(edge[0])

    return tree

input_path = "data/rosalind_deg.txt"
input_file = open(input_path, "r")
edges_list = [l.rstrip().split(" ") for l in input_file.readlines()[1:]]
neighbour_tree = construct_neighbour_tree(edges_list)
nodes = sorted([int(n) for n in neighbour_tree.keys()])

degrees = []

for node in nodes:
    # print(str(node) + "\t" + str(len(neighbour_tree[str(node)])))
    degrees.append(str(len(neighbour_tree[str(node)])))

print(" ".join(degrees))
