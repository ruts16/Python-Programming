# Single Level Inheritance
# Single -Level Inheritance enables a derived class to inherit characteristics from a single-parent class

class itvedant:   #base class
    def getitv(self):
        self.cname='itvedant'
    def display(self):
        print("class name is:",self.cname)

class branch(itvedant):   #derived class
    def getb(self):
        self.br='pimpri'

    def displayb(self):
        print("Class name is :",self.cname)
        print("Branch name is:",self.br)

b=branch()
b.getitv()
b.getb()
b.displayb()
