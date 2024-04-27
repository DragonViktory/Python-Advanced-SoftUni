def print_row(n, row):
    print(' ' * (n - row), end="")
    print(*['*'] * row)


def print_triangle(n):
    for row in range(1, n + 1):
        print_row(number, row)


number = int(input())

for row in range(1, n + 1):
    print(' ' * (n - row), end="")
    print(*['*'] * row)

for row in range(n - 1, 0, -1):
    print(' ' * (n - row), end="")
    print(*['*'] * row)
