import random


def main():
    score = float(input("Enter score: "))
    result = determine_result(score)
    print(result)


def random_score():
    score = random.randint(0, 100)
    result = determine_result(score)
    print(result)


def determine_result(score):
    if score > 50:
        return "Passable"
    elif score > 90:
        return "Excellent"
    elif score < 50:
        return "Bad"
    else:
        return "Invalid score"


main()
