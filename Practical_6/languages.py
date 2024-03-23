from Practical_6.programming_language import ProgrammingLanguage
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
eiffel = ProgrammingLanguage("Eiffel", "Static", True, 1985)
java = ProgrammingLanguage("Java", "Static", True, 1995)
c = ProgrammingLanguage("C++", "Static", False, 1983)
dynamic = []
languages = [python, ruby, visual_basic, eiffel, java, c]
for language in languages:
    if language.is_dynamic() == True:
        dynamic.append(language.name)
print("The dynamically typed languages are:")
for name in dynamic:
    print(name)
