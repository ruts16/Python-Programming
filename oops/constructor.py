#Constructor name:-__init__()
#we need not to call the constructor
#becoz constructor is called when the object is created.

class student:
    def __init__(self):
        self.n=input("Enter the name:")

    def display(self):
        print("Student name is:",self.n)
s=student()
s.display()
