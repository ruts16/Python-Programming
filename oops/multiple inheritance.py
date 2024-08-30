# Multiple Inheritance
# Multiple inheritance enables one derived class to inherit properties from one or more base class

class dad:
    def getd(self):
        self.dname=input("enter the father name:")
class mom:
    def getm(self):
        self.mname=input("enter the mother name:")
class child(dad,mom):
    def getc(self):
        self.cname=input("enter the child name:")

    def display(self):
        print("Student name is:",self.cname)
        print("Father name is:",self.dname)
        print("Mother name is:",self.mname)
c=child()
c.getd()
c.getm()
c.getc()
c.display()
