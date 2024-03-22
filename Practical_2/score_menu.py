def main():
    menu = "(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"
    score = 0
    print(menu)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
            print(score)
        elif choice == "P":
            result = determine_result(score)
            print(result)
        elif choice == "S":
            print("*" * score)
        print(menu)
        choice = input(">>> ").upper()
    print("farewell")


def get_valid_score():
    score = int(input("score: "))
    while score > 100 or score < 0:
        print("invalid score")
        score = input("score: ")
    return score


def determine_result(score):
    if score > 90:
        return "Excellent"
    elif score > 50:
        return "Passable"
    elif score < 50:
        return "Bad"
    else:
        return "Invalid score"


main()
