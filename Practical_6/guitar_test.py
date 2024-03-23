from Practical_6.guitar import Guitar

guitar = Guitar("Gibson L-5 CES", 1922, 16035.4)
anotherguitar = Guitar("Another Guitar", 2013, 12345.6)

print(guitar.get_age())
print(anotherguitar.get_age())
print(guitar.is_vintage())
print(anotherguitar.is_vintage())
