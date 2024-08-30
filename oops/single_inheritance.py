class itvedant:
    def getitv(self):
        self.cname='itvedant'
    def display(self):
        print("class name is:",self.cname)

class branch(itvedant):
    def getb(self):
        self.br='pimpri'

    def displayb(self):
        print("Class name is :",self.cname)
        print("Branch name is:",self.br)

b=branch()
b.getitv()
b.getb()
b.displayb()
