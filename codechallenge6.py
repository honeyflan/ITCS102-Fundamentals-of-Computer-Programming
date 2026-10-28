size = int(input("Please input the size of x _______?"))

for x in range(size):
    for y in range(size):
        if x + y == size -1 or x == y:
            print("*", end=" ")
        else:
            print(" ", end= " ")
    print()
