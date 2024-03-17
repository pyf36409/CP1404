name = input("name: ")
file = open("name.txt", "w")
file.write(name)
file.close()

file = open("name.txt", "r")
name = file.read()
file.close()
print(f"Your name is {name}")

numbers = []
file = open("numbers.txt", "r")
for i in range(2):
    number = file.readline()
    numbers.append(number)
file.close()
total = int(numbers[0]) + int(numbers[1])
print(total)

numbers = []
total = 0
file = open("numbers.txt", "r")
number = file.readline()
while number != "":
    numbers.append(number)
    number = file.readline()
file.close()
for count in range(len(numbers)):
    total = total + int(numbers[count])
print(total)
