def print_triangle(row):
    for i in range(row):
        print(" ", end=" ")
        for j in range(row - i):
            print(".", end=" ")
        for j in range(0, i + 1):
            print(j, end="  ")
        for i in range(row, -1, -1):
            print(j, end="  ")
        print()

print_triangle(3)