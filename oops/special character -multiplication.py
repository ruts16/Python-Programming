#special character for multiplication
# within 2 classes

class emp:
    def __init__(self,name,sal):
        self.n=name
        self.s=sal
    def __mul__(e,h):
        return e.s*h.p

class HR:
    def __init__(self,days):
        self.p=days

    

e=emp('ritika',500) # sal per day
h=HR(20) # he is present for 20 days
# 20 * 500

print("total Salary of",e.n,"is:",e*h) 


