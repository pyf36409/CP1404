COLOR = {"Absolutezero": "#0048ba", "Acidgreen": "#b0bf1a", "Aliceblue": "#f0f8ff", "Alizarincrimson": "#e32636", "Amaranth": "#e52b50", "Amber": "#ffbf00", "Amethyst": "#9966cc", "Antiquewhite": "#faebd7", "Apricot": "#fbceb1", "Aqua": "#00ffff"}
print(COLOR)

color = input("color: ").capitalize()
while color != "":
    if color not in COLOR:
        print("Invalid")
    else:
        print(color, "is", COLOR[color])
    color = input("color: ").capitalize()
