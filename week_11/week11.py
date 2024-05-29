import pandas as pd
df = pd.read_csv('SIS.csv')
df
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        self.category = self.determine_category()
    
    def determine_category(self):
        if 14 < self.age <=18:
            return "The_Pirates"
        elif 18 < self.age <= 22:
            return "The_Yankees"
        elif 22 < self.age < 25:
            return "The_Bulls"
        else:
            return "Error"

# Example of creating a Student object and checking its category
student = Student("David Usim", 19, "A")
print(f"Student: {student.name}, Age: {student.age}, Category: {student.category}")
