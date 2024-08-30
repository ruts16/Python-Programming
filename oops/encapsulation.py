class student:
    branch='Pimpri'
    def getdata(self,name ,age): #public
        self.n=name
        self.a=age
    def display(self): #public
        print("Student Name is:",self.n)
        print("Student age is:",self.a)
        print("Branch is:",self.branch)
s=student()
s.getdata('rutuja',20)
s.display()
print(student.branch)
    
