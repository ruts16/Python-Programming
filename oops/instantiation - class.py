#class is the blueprint of the object
#self is a parameter
#if we do not use self it will give us an error 
'''
class class_name:
    properties of class

#to call the class we need to create the object - instantiation method
    obj=class_name()
'''

class student:
    def getdata(self):
        n=input("Enter the name:")  #data members or local variables=n
        mob=int(input("Enter the number:")) #data members or local variables=mob
        print("Student Name is:",n)
        print("Contact number is:",mob)
        
s=student()
s.getdata() #getdata(s)
