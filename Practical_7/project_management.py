from Practical_7.project import Project


def main():
    menu = "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new project\n- (U)pdate project\n- (Q)uit"
    projects = []
    print("Welcome to Pythonic Project Management")
    in_file = open("projects.txt", "r", newline="")
    in_file.readline().strip().split("  ")
    for line in in_file:
        project = Project(line[0], line[1], line[2], line[3], line[4])
        projects.append(project)
    in_file.close()


main()
