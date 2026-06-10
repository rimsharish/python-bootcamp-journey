class Student: 
    def __init__(self,name,age,marks):
        self.name = name
        self.age = age
        self.marks = marks

    def display(self):
        print(f"name: {self.name}")
        print(f"age: {self.age}")
        print(f"marks: {self.marks}")

s1 = Student("rim",19,85)
s1.display()

s2 = Student("abd",16,95)
s2.display()

