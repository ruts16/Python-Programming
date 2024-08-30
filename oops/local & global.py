#local variables

class student:
    def getdata(self):
        n=input("Enter the name:")  #data members or local variables=n
        mob=int(input("Enter the number:")) #data members or local variables=mob
        print("Student Name is:",n)
        print("Contact number is:",mob)
        
s=student() #object creation 
s.getdata() #getdata(s)


#--------------------------------------------------------------------------------
#global variables

class student:
    def getdata(self):
        self.n=input("Enter the name:")  #data members or local variables=n
        self.mob=int(input("Enter the number:")) #data members or local variables=mob
    def display(self):
        print("Student Name is:",self.n)
        print("Contact number is:",self.mob)
        
s=student()
s.getdata() #getdata(s)
s.display()
#--------------------------------------------------------------------------------
#using another variable in place of self 
class student:
    def getdata(x):
        x.n=input("Enter the name:")  #data members or local variables=n
        x.mob=int(input("Enter the number:")) #data members or local variables=mob
    def display(x):
        print("Student Name is:",x.n)
        print("Contact number is:",x.mob)
        
s=student()
s.getdata() #getdata(s)
s.display()

