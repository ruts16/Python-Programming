class A:
    def geta(self):
        self.a=10
class B(A):
    def getb(self):
        self.b=20
class C(B):
    def getc(self):
        self.c=30
        self.res=self.a+self.b+self.c
        print("Addition os ",self.a,',',self.b,',',self.c,'is:',self.res)

obj=C()
obj.geta()
obj.getb()
obj.getc()
