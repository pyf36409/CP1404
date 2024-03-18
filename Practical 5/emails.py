emails = {}
email = input("Email: ")
while email != "":
    name = email.title().split("@")[0]
    choice = input(f"Is your name {name}? (Y/n)").upper()
    if choice != "Y" and choice != "":
        name = input("Name: ")
    emails[email] = name
    email = input("Email: ")
for email, name in emails.items():
    print(f"{name} ({email})")
