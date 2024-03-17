import random

numbers = []
picks = int(input("How many quick picks? "))
for x in range(picks):
    for i in range(6):
        numbers.append(random.randint(1, 45))
        numbers.sort()
    for number in numbers:
        print(f"{number:>2}", end=" ")
    numbers.clear()
    print()
