n=int(input("Enter column:"))
r=int(input("Enter rows:"))

for x in range(n):
    for y in range(r):
        if x == 0 or x == n - 1 or y == 0 or y == r -1:
            print("*", end= " ")
        else:
            print(" ", end= " ")
    print()
