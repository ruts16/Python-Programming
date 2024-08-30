class dad:
    def getd(self):
        self.dname=input("Enter the father name:")
class sis(dad):
    def gets(self):
        self.sname=input("enter the sister name:")
    def displayS(self):
        print("Sister name is:",self.sname)
        print("Father name is:",self.dname)
class bro(dad):
    def getb(self):
        self.bname=input("Enter the brother name:")
    def displayB(self):
        print("Brother name is:",self.bname)
        print("Father name is:",self.dname)
    
s=sis()
b=bro()

s.getd()
s.gets()
s.displayS()

b.getd()
b.getb()
b.displayB()

