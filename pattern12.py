n = 5

# Top half (1 to 5 stars on wing)
for i in range(1, n + 1):
    # Left wing stars
    for j in range(i):
        print("*", end=" ")
    # Middle spaces: 8, 6, 4, 2, 0 space-pairs
    for j in range(2 * (n - i)):
        print(" ", end=" ")
        
    # Right wing stars
    for j in range(i):
        print("*", end=" ")
    print()

# Bottom half(4 down to 1 stars on wing)
for i in range(n - 1, 0, -1):
    # Left wing stars
    for j in range(i):
        print("*", end=" ")

    # Middle spaces: 2, 4, 6, 8 space-pairs
    for j in range(2 * (n - i)):
        
        print(" ", end=" ")

    # Right wing stars
    for j in range(i):
        print("*", end=" ")
    print()