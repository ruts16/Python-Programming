#magic methods and special methods
'''
special method - constructor
represented by '__'
'''
a=10
b=20
c=a+b

print("addition of",a,'and',b,'is:',c)
print("-----------------------------------------------")
#special method for addition of two normal variables
#__add__

a=10
b=20
c=a+b
d=int.__add__(a,b)
print("addition of",a,'and',b,'is:',c)
print("addition of",a,'and',b,'is:',d ,'by using special method')

#special method for addition of two objects

class student:
    def get(self):
        self.m=int(input("Enter the mark"))
        
    def __add__(s,s1): #x=s , y=s1 in case parameter is x,y
        
        t=student()  #object created inside class(temporary to store result)
        #10+20 = 30 will be stored inside t
        
        t.m=s.m+s1.m 

        return t
       #return object value will also be returned
       # t object will be assigned to s3
       #t has the variable m inside it

    
    def display(self):
        print("Addition of marks is:",self.m)
        #displays the variable m which is inside the s3
        
s=student()
s1=student()
s.get()
s1.get()
s3=s+s1  # when + operator is executed then it calls the method add inside the class
s3.display()

#program in sequence
'''
class student:
    def get(self):
        self.m=int(input("Enter the mark"))
    def __add__(s,s1): 
        t=student() 
        t.m=s.m+s1.m 
        return t
    def display(self):
        print("Addition of marks is:",self.m)    
s=student()
s1=student()
s.get()
s1.get()
s3=s+s1  
s3.display()
'''


























              
