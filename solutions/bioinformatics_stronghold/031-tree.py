"""Solution for Bioinformatics Stronghold Problem ID: TREE

Problem Title: Completing a Tree
Link: http://rosalind.info/problems/tree
"""

input_path = "data/rosalind_tree.txt"

input_file = open(input_path, "r")
n_nodes = int(input_file.readline().rstrip())
nodes = [str(i) for i in range(1, n_nodes+1)]
edges = [l.rstrip().split(" ") for l in input_file.readlines()]
input_file.close()

all_captured_nodes = []
for edge in edges:
    all_captured_nodes.append(edge[0])
    all_captured_nodes.append(edge[1])

subtrees = [set(edge) for edge in edges]

first_run = True
n_joins = 0
iter = 0

while first_run or n_joins > 0:
    iter += 1
    first_run = False
    n_joins = 0

    a = 0

    while a < len(subtrees):
        b = a + 1

        while b < len(subtrees):
            subtree_a = subtrees[a]
            subtree_b = subtrees[b]
            deleted_b = False

            nodes_not_in_subtrees = True

            intersect_length = len(subtree_a.intersection(subtree_b))

            if intersect_length > 0:
                new_set = subtree_a.union(subtree_b)
                subtrees[a] = new_set
                del subtrees[b]

                deleted_b = True
                nodes_not_in_subtrees = False
                n_joins += 1

            if not deleted_b:
                b += 1
        a += 1

all_captured_nodes = set(all_captured_nodes)
orphaned_nodes = set(nodes).difference(all_captured_nodes)

required_edges = len(orphaned_nodes) + len(subtrees) - 1
print(required_edges)
