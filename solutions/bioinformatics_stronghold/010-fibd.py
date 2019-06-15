"""Solution for Bioinformatics Stronghold Problem ID: FIBD

Problem Title: Mortal Fibonacci Rabbits
Link: http://rosalind.info/problems/fibd
"""

input_data = open("data/rosalind_fibd.txt", "r").read().rstrip().split(" ")
total_generations = int(input_data[0])
lifespan = int(input_data[1])

litter_size = 1
n_newborn = 1
n_matings = 0
n_mature = 0

lifespan_l = [0 for i in range(0, lifespan + 1)]
lifespan_l[0] = n_newborn

for i in range(1, total_generations):

    # babies born this month dependent on mature rabbits
    # (months 1 to mortality - 1)
    n_babies_born = sum(lifespan_l[1:-1]) * litter_size

    # babies born becomes 0th element in age array
    # everything gets shifted up one, and rabbits at end of array get pushed out
    # print(range(lifespan - 1, -1, -1))
    for a in range(lifespan - 1, -1, -1):
        lifespan_l[a+1] = lifespan_l[a]
    lifespan_l[0] = n_babies_born

total_alive = sum(lifespan_l[:-1])
print(total_alive)
