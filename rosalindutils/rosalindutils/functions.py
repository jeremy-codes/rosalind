def factorial(i):
    sum = 1
    for i in range(1, i + 1):
        sum *= i
    return sum

def combination_without_replacement(n, r):
    # n - total number of elements in the pool
    # r - number of elements selected

    n_fact = factorial(n)
    r_fact = factorial(r)
    n_minus_r_fact = factorial(n - r)
    return int(n_fact / (r_fact * n_minus_r_fact))

def permutation_without_replacement(n, r):
    # n - total number of elements in the pool
    # r - number of elements selected

    n_fact = factorial(n)
    n_minus_r_fact = factorial(n-r)
    return int(n_fact / n_minus_r_fact)
