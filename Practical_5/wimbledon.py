lines = []
words = []
CHAMPIONS = {}
countries = []
with open("wimbledon.csv", "r", encoding="utf-8-sig") as in_file:
    text = in_file.readlines()
    for line in text:
        lines.append(line)
    for line in lines:
        line_split = line.split(",")
        country = line_split[1]
        champion = line_split[2]
        if country not in countries:
            countries.append(country)
        if champion in CHAMPIONS:
            CHAMPIONS[champion] += 1
        else:
            CHAMPIONS[champion] = 1
    CHAMPIONS.pop("Champion")
    countries.pop(0)
    print("Wimbledon Champions: ")
    for champion, times in CHAMPIONS.items():
        print(f"{champion} {times}")
    print(f"These {len(countries)} countries have won Wimbledon: ")
    for country in countries:
        print(country, end=", ")
