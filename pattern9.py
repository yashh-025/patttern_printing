

n = 10
# Top half (1, 3, 5, 7, 9 stars)
for i in range(1, n, 2):
    for j in range(n - 1 - i):
        print("", end=" ")
    for k in range(i):
        print("*", end=" ")
    print()
# Bottom half (7, 5, 3, 1 stars)
for i in range(n - 3,0,-2):  # Changed start from -1 to -3
    for j in range(n -1 - i):
        print("", end=" ")
    for k in range(i):
        print("*", end=" ")
    print()