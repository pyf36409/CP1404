menu = "(H)ello\n(G)oodbye\n(Q)uit"
name = input("Enter name: ")
print(menu)
choice = input(">>> ").capitalize()
while choice != "Q":
    if choice == "H":
        print(f"Hello {name}")
    elif choice == "G":
        print(f"Goodbye {name}")
    else:
        print("Invalid choice")
    print(menu)
    choice = input(">>> ").capitalize()
print("Finished.")