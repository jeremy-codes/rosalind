"""Solution for Bioinformatics Stronghold Problem ID: FIB

Problem Title: Rabbits and Recurrence Relations
Link: http://rosalind.info/problems/fib
"""

input_data = open("data/rosalind_fib.txt", "r").read().rstrip().split(" ")
total_generations = int(input_data[0])
litter_size = int(input_data[1])

n_newborn = 1
n_matings = 0
n_mature = 0

for i in range(1, total_generations):
    n_babies_born = n_mature * litter_size
    n_babies_matured = n_newborn

    n_mature += n_babies_matured
    n_newborn = n_babies_born

total = n_mature + n_newborn
print(total)
