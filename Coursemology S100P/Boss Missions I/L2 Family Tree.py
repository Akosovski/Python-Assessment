class Person:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName


class Parent(Person):
    def __init__(self, firstName, lastName):
        super().__init__(firstName, lastName)
        self.children = []

    def addChild(self, child):
        if len(child.parents) < 2:
            self.children.append(child)
            child.addParent(self)
            print(f"Child {child.firstName} {child.lastName} added to {self.firstName}'s children.")
        else:
            print(f"Error: {child.firstName} {child.lastName} already has 2 parents.")

    def removeChild(self, child):
        if child in self.children:
            self.children.remove(child)
            child.removeParent(self)
            print(f"Child {child.firstName} {child.lastName} removed from {self.firstName}'s children.")
        else:
            print(f"Error: {child.firstName} {child.lastName} is not a child of {self.firstName}.")

    def displayChildren(self):
        children_names = [f"{child.firstName} {child.lastName}" for child in self.children]
        print(f"{self.firstName}'s Children: {', '.join(children_names)}")


class Child(Person):
    def __init__(self, firstName, lastName):
        super().__init__(firstName, lastName)
        self.parents = []

    def addParent(self, parent):
        if len(self.parents) < 2:
            self.parents.append(parent)
            parent.addChild(self)
            print(f"{self.firstName} {self.lastName} added to {parent.firstName}'s children.")
        else:
            print(f"Error: {self.firstName} {self.lastName} already has 2 parents.")

    def removeParent(self, parent):
        if parent in self.parents:
            self.parents.remove(parent)
            parent.removeChild(self)
            print(f"{self.firstName} {self.lastName} removed from {parent.firstName}'s children.")
        else:
            print(f"Error: {self.firstName} {self.lastName} is not a child of {parent.firstName}.")

    def displayParents(self):
        parents_names = [f"{parent.firstName} {parent.lastName}" for parent in self.parents]
        print(f"{self.firstName}'s Parents: {', '.join(parents_names)}")


def main():
    parents = []
    children = []

    while True:
        print("\nMenu:")
        print("1. Create Parent")
        print("2. Create Child")
        print("3. Add Child to Parent")
        print("4. Remove Child from Parent")
        print("5. Display Children of Parent")
        print("6. Display Parents of Child")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            first_name = input("Enter parent's first name: ")
            last_name = input("Enter parent's last name: ")
            parent = Parent(first_name, last_name)
            parents.append(parent)
            print(f"Parent {first_name} {last_name} created.")

        elif choice == "2":
            first_name = input("Enter child's first name: ")
            last_name = input("Enter child's last name: ")
            child = Child(first_name, last_name)
            children.append(child)
            print(f"Child {first_name} {last_name} created.")

        elif choice == "3":
            parent_index = int(input("Enter the index of the parent: "))
            child_index = int(input("Enter the index of the child: "))
            if 0 <= parent_index < len(parents) and 0 <= child_index < len(children):
                parents[parent_index].addChild(children[child_index])
            else:
                print("Invalid parent or child index.")

        elif choice == "4":
            parent_index = int(input("Enter the index of the parent: "))
            child_index = int(input("Enter the index of the child: "))
            if 0 <= parent_index < len(parents) and 0 <= child_index < len(children):
                parents[parent_index].removeChild(children[child_index])
            else:
                print("Invalid parent or child index.")

        elif choice == "5":
            parent_index = int(input("Enter the index of the parent: "))
            if 0 <= parent_index < len(parents):
                parents[parent_index].displayChildren()
            else:
                print("Invalid parent index.")

        elif choice == "6":
            child_index = int(input("Enter the index of the child: "))
            if 0 <= child_index < len(children):
                children[child_index].displayParents()
            else:
                print("Invalid child index.")

        elif choice == "7":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 7.")


if __name__ == "__main__":
    main()