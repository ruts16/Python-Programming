class A:
    def geta(self):
        self.dname=input("Enter the father name:")
class B(A):
    def getb(self):
        self.mname=input("enter the mother name:")
    def displayB(self):
        print("Father name is:",self.dname)
        print("Mother name is:",self.mname)
class C(A):
    def getc(self):
        self.bname=input("Enter the brother name:")
    def displayC(self):
        print("Brother name is:",self.bname)
        print("Father name is:",self.dname)
class D(B,C):
    def getd(self):
        self.sname=input("Enter the sister name:")
    def displayD(self):
        print("Sister name is:",self.sname)
        print("Father name is:",self.dname)
        print("Mother name is:",self.mname)
        print("brother name is:",self.bname)
    

d=D()


d.geta()
d.getb()
d.getc()
d.getd()
d.displayD()







