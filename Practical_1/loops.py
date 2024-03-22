for i in range(1, 21, 2):
    print(i, end=' ')
print()

# a
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# b
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# c
amount = int(input("Number of stars: "))
print("*" * amount)

# d
amount = int(input("Number of stars: "))
for time in range(1, amount + 1):
    print("*" * time)
