import csv
from Practical_7.guitar import Guitar


def main():
    guitars = []
    in_file = open("guitars.csv", "r", newline='')
    in_file.readline()
    reader = csv.reader(in_file)
    for line in reader:
        guitar = Guitar(line[0], line[1], line[2])
        guitars.append(guitar)
    in_file.close()
    sorted_guitars = sorted(guitars)
    print("My guitars!")
    for guitar in sorted_guitars:
        print(guitar)
    name = input("Name: ")
    while name != "":
        year = input("Year: ")
        cost = input("Cost: $")
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        name = input("Name: ")
    print("\n... snip ...\n")
    print("These are my guitars:")
    sorted_guitars = sorted(guitars)
    for guitar in sorted_guitars:
        print(guitar.name)
    in_file = open("guitars.csv", "w", newline='')
    for guitar in sorted_guitars:
        data = [guitar.name, guitar.year, guitar.cost]
        writer = csv.writer(in_file)
        writer.writerow(data)
    in_file.close()


main()
