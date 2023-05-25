import numpy as np
import random

# Set the patterns
patterns = [[0, 0, 0, 0, 0,
             0, 1, 1, 0, 0,
             0, 0, 1, 0, 0,
             0, 0, 1, 0, 0,
             0, 0, 1, 0, 0],
            [1, 1, 1, 1, 1,
             1, 0, 0, 1, 1,
             1, 1, 0, 1, 1,
             1, 1, 0, 1, 1,
             1, 1, 0, 1, 1]]

matches = [0] * len(patterns)

# Set the parameters
T = 1
n = 25
num_iterations = 1000

# Define the activation function
def f(u, T=1):
    return 1 / (1 + np.exp(-(u/T)))

# Initialize the Boltzmann machine variables
z =[0, 0, 0, 0, 0,
    0, 1, 1, 0, 0,
    0, 0, 1, 0, 0,
    0, 0, 1, 0, 0,
    0, 0, 1, 0, 0]

# set the initial state of the Boltzmann machine
x = [random.randint(0, 1) for _ in range(n)]

# Initialize c
c = np.zeros((n, n), dtype=np.float64)

for i in range(n):
    for j in range(n):
        if i != j:
            c[i, j] = (z[i] - 0.5) * (z[j] - 0.5)

# Initialize weights
w = np.array(2 * c, dtype=np.float64)

# Initialize theta
theta = np.zeros(n, dtype=np.float64)
for i in range(n):
    theta[i] = sum(c[i])

# Initialize u
u = np.zeros(n, dtype=np.float64)

# Boltzmann machine algorithm
for t in range(1, num_iterations):

    beta = [random.uniform(0, 1) for _ in range(n)]

    for i in range(n):
        u[i] = sum(w[i][j] * x[j] for j in range(n)) - theta[i]

    for i in range(n):
        x[i] = 1 if 0 <= beta[i] <= f(u[i], T=T) else 0

    print(f"x({t}): ")
    print(str(np.array(x).reshape(5, 5)))

    # Check if the current state matches any of the patterns
    for i in range(len(patterns)):
        if x == patterns[i]:
            matches[i] += 1

# Print the final state of the Boltzmann machine
print("Final state:")
print(str(np.array(x).reshape(5, 5)))

# Print the number of matches
print("Number of matches:")
print(matches)
