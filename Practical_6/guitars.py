from Practical_6.guitar import Guitar

names = []
years = []
costs = []

print("My guitars!")
name = input("Name: ")
while name != "":
    names.append(name)
    year = int(input("Year: "))
    years.append(year)
    cost = float(input("Cost: $"))
    costs.append(cost)
    print(Guitar(name, year, cost))
    name = input("Name: ")

print("\n... snip ...\n")
print("These are my guitars:")
for count in range(len(names)):
    guitar = Guitar(names[count], years[count], costs[count])
    print(f"Guitar {count + 1}: {guitar} {guitar.is_vintage()}")
