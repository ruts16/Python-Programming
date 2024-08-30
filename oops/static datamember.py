#Static data members
class student:
    cls="Itvedant"
    branch='Pimpri'

    def getdata(x):
        x.n=input("Enter the name:")
        x.mob=int(input("Enter the number:"))

    def display(self):
        print("Student Name is:",self.n)
        print("Contact Number is:",self.mob)
        print("Class Name is:",self.cls)
        print("Branch is:",self.branch)

s=student()
'''
s.getdata()  #getdata(s)
s.display()
'''
print("Class Name is:",student.cls)
print("Branch is:",student.branch)

student.branch='Pune'

print("class name is:",student.cls)
print("Branch is:",student.branch)

print(type(s))
