import wikipedia

phrase = input("search: ")
while phrase != "":
    result = wikipedia.search(phrase)
    for part in result:
        print(part)
    phrase = input("search: ")
