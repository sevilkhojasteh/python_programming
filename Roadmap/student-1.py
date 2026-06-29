class Student:
    def __init__(self, name, house, patronus = None):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
        self.patronus = patronus



    def __str__(self):
        return f"{self.name} from {self.house}"


def main():
    student = get_student()
    print(student)

def get_student():
    name = input("What's your name? ")
    house = input("What house do you belong to? ")
    patronus = input("What's your patronus? ")
    return Student(name, house, patronus)



     
if __name__ == "__main__":
    main()


# __str__ and __rpr__ : rpr for programmers and show 
# more information on the object but str just prints the info

# When a function is inside a class it is called "method"