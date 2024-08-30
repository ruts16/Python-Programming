# '__' -> to declare it private
'''
class student:
    __branch='Pimpri' #declared private so cant call outside the class
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
#print(student.branch) # cannot be called
 '''   
class student:
    branch='Pimpri' #declared private so cant call outside the class
    def getdata(self,name ,age): #public
        self.n=name
        self.a=age
        self.__display() #__display(self)
    def __display(self): #public
        print("Student Name is:",self.n)
        print("Student age is:",self.a)
        print("Branch is:",self.branch)
s=student()
s.getdata('rutuja',20)
#s.display()
#print(student.branch) # cannot be called
    
