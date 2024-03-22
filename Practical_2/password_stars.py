def main():
    password = get_password()
    print("*" * len(password))


def get_password():
    length = 10
    password = input("password: ")
    while len(password) != length:
        print("invalid length")
        password = input("password: ")
    return password


main()
