class Student:
    def __init__(self, name, house, patronus = None):
        self.name = name
        self.house = house
        self.patronus = patronus



    def __str__(self):
        return f"{self.name} from {self.house}"
    
    def charm(self):
        if self.patronus == "Stag":
            return "Stag"
        elif self.patronus == "Otter":
            return "Otter"
        elif self.patronus == "Jack Russell terrier":
            return "Jack Russell terrier"
        else:
            return "No patronus"

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name


    @property
    def house(self):
        return self._house
    
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house





def main():
    student = get_student()
    print("Expecto Patronum!")
    print(student.charm())

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