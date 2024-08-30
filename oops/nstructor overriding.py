#whichever object is created only that constructor will be called
class A:
    def __init__(self):
        print("Inside Class A constructor")
class B(A):
    def __init__(self):
        super().__init__()  #to call the class whose object has not been created 
        print("Inside Class B Constructor")
b=B()
