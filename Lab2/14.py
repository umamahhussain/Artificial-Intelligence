class Student:
    def __init__(self, name, roll_number, gender, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.gender = gender
        self.cgpa = cgpa
    
    def get_name(self):
        return self.name
    
    def get_roll_number(self):
        return self.roll_number
    
    def get_gender(self):
        return self.gender
    
    def get_cgpa(self):
        return self.cgpa
    
    def set_name(self, name):
        self.name = name
    
    def set_roll_number(self, roll_number):
        self.roll_number = roll_number
    
    def set_gender(self, gender):
        self.gender = gender
    
    def set_cgpa(self, cgpa):
        self.cgpa = cgpa



student1 = Student("Umamah", "1858", "Female", 3.2)

print("Name:", student1.get_name())
print("Roll Number:", student1.get_roll_number())
print("Gender:", student1.get_gender())
print("CGPA:", student1.get_cgpa())

student1.set_cgpa(2.0)
print("Updated CGPA:", student1.get_cgpa())

student2 = Student("Waleed", "5248", "Male", 3.6)
student3 = Student("Ali", "0248", "Male", 3.3)

if(student2.gender=="Male"):
    print("\n\nName:", student2.get_name())
    print("Roll Number:", student2.get_roll_number())
    print("Gender:", student2.get_gender())
    print("CGPA:", student2.get_cgpa())

if(student3.gender=="Male"):
    print("\n\nName:", student3.get_name())
    print("Roll Number:", student3.get_roll_number())
    print("Gender:", student3.get_gender())
    print("CGPA:", student3.get_cgpa())
