"""Solution for Bioinformatics Stronghold Problem ID: LONG

Problem Title: Genome Assembly as Shortest Superstring
Link: http://rosalind.info/problems/long
"""

import math
import itertools
from rosalindutils.fasta_parser import FastaParser

input_path = "data/rosalind_long.txt"
# input_path = "data/rosalind_long.ex.txt"
output_path = "output/rosalind_long.output.txt"
seqs = FastaParser(input_path).parse_fasta()
seqs_d = {s["header"]: s["sequence"] for s in seqs}
seq_headers = seqs_d.keys()

directed_edges = []

# get a list of directed edges, in which the 3' end of seq a overlaps with the
# 5' end of seq b (more than 50% overlap for both seqs)
# print("part 1")
for i in range(0, len(seqs)):
    for j in range(0, len(seqs)):
        if i != j:

            match_not_found = True
            max_offset = min(math.ceil(float(len(seqs[i]["sequence"])) / 2.0),
                             math.ceil(float(len(seqs[j]["sequence"])) / 2.0))

            for offset in range(0, max_offset):
                if match_not_found:
                    subseq_i = seqs[i]["sequence"][offset:]
                    subseq_j = seqs[j]["sequence"][0: len(subseq_i)]

                    if subseq_i == subseq_j:
                        match_not_found = False
                        # new edge, capture various info
                        new_elem = [
                            seqs[i]["header"], # seq i header
                            seqs[j]["header"], # seq j header
                            len(subseq_i), # length of shared subseq
                            offset # starting index of shared subseq in i
                        ]
                        directed_edges.append(new_elem)

edge_dict = {edge[0] + "-" + edge[1]: edge for edge in directed_edges}
edge_set = set(edge_dict.keys())
edge_l = list(edge_set)

# we need to reconstruct all possible permutations/graphs given our edge list
# create a dict of a node's possible 5 primer and 3 prime neighbors
neighbors_dict = {
    node: {
        "3p": [],
        "5p": []
    } for node in seq_headers
}

for edge in edge_l:
    node_5p, node_3p = edge.split("-")
    neighbors_dict[node_5p]["3p"].append(node_3p)
    neighbors_dict[node_3p]["5p"].append(node_5p)

# starting nodes have 0 5prime neighbors,
# ending nodes have 0 3prime neighbors
starting_nodes = []
ending_nodes = []
for nk in neighbors_dict.keys():
    if len(neighbors_dict[nk]["5p"]) == 0:
        starting_nodes.append(nk)
    if len(neighbors_dict[nk]["3p"]) == 0:
        ending_nodes.append(nk)

# build a series of possible graphs, each starting with the starting node,
# each taking on a new neighbor for each iteration
# print("part 2")
graph_builder = [starting_nodes]
end_not_reached = True

while end_not_reached:
    next_iteration_graph_builder = []
    end_nodes_reached = 0

    for graph in graph_builder:

        latest_node = graph[-1]
        if latest_node in set(ending_nodes):
            end_nodes_reached += 1
        else:
            latest_node_3p_neighbours = neighbors_dict[latest_node]["3p"]
            for neighbour in latest_node_3p_neighbours:
                next_iteration_graph_builder.append(graph + [neighbour])


    if end_nodes_reached == len(graph_builder):
        end_not_reached = False
    else:
        graph_builder = next_iteration_graph_builder

# only choose graphs that have the right number of nodes and all unique nodes
# print("part 3")
possible_permutations = []
for graph in graph_builder:
    if len(graph) == len(seq_headers) and len(set(graph)) == len(seq_headers):
        possible_permutations.append(graph)

# iterate through possible permutations, finding which one has the shortest
# length
# print("part 4")
shortest_length = float("inf")
shortest_permutation = None

for perm in possible_permutations:
    length = 0

    for node_idx in range(1, len(perm)):
        edge_key = perm[node_idx - 1] + "-" + perm[node_idx]
        non_overlap_seq_length = edge_dict[edge_key][3]
        length += non_overlap_seq_length

    # add the final sequence
    final_3p_length = len(seqs_d[perm[-1]])

    length += final_3p_length

    if length < shortest_length:
        shortest_length = length
        shortest_permutation = perm

# construct the sequence for the shortest_permutation
seq = ""
for node_idx in range(1, len(shortest_permutation)):
    edge_key = shortest_permutation[node_idx - 1] + "-" + shortest_permutation[node_idx]
    non_overlap_seq_length = edge_dict[edge_key][3]
    non_overlap_seq = seqs_d[shortest_permutation[node_idx - 1]][:non_overlap_seq_length]

    seq += non_overlap_seq

# add the final sequence
seq += seqs_d[shortest_permutation[-1]]

open(output_path, "w").write(seq+"\n")
