#parameterised constructor


class student:
    def __init__(self,age):
        self.n=input("Enter the name:")
        self.a=age

    def display(self):
        print("Student name is:",self.n)
        print("Student name is:",self.a)
s=student(23) #object created 
s.display()
