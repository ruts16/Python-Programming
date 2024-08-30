class university:
    def geta(self):
        self.cname='Dbatu'
    def displaya(self):
        print("university name is:",self.cname)

class college(university):
    def getb(self):
        self.clg='AITRC'

    def displayb(self):
        print("college name is:",self.clg)
        
class department(college):
    def getc(self):
        self.dept='CSE'

    def displayc(self):
        print("university name is:",self.cname)
        print("college name is:",self.clg)
        print("department name is:",self.dept)


d=department()
d.geta()
d.getb()
d.getc()
d.displayc()
