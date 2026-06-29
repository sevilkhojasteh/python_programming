class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house





# def main():    
#     name, house = get_student()
#     print(f"{name} lives in {house}.")


# def get_student():
#     name = input("What's your name? ")
#     house = input("What house do you belong to? ")
#     return name, house


# def main():
#     student = get_student()

#     if student["name"] == "Padma":
#         student["house"] = "Ravenclaw"

#     print(f"{student['name']} lives in {student['house']}.")

# def get_student():
#     student = {}
#     student["name"] = input("What's your name? ")
#     student["house"] = input("What house do you belong to? ")
#     return student

# def get_student():
#     name = input("What's your name? ")
#     house = input("What house do you belong to? ")
#     return {"name": name, "house": house}

def main():
    student = get_student()
    print(f"{student.name} lives in {student.house}.")

def get_student():
    student = Student()
    student.name = input("What's your name? ")
    student.house = input("What house do you belong to? ")
    return student



     
if __name__ == "__main__":
    main()
