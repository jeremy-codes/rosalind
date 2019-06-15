"""Solution for Algorithmic Heights Problem ID: FIBO

Problem Title: Fibonacci Numbers
Link: http://rosalind.info/problems/fibo
"""

input_path = "data/rosalind_fibo.txt"
input_file = open(input_path, "r")
n = int(input_file.read().rstrip())

fib_a = 0
fib_b = 1
fib_answer = None

if n == 1:
    fib_answer = fib_a
elif n == 2:
    fib_answer = fib_b
else:

    for i in range(2, n+1):
        new_fib = fib_a + fib_b
        fib_a, fib_b = fib_b, new_fib

    fib_answer = fib_b

print(fib_answer)
