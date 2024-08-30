#destructor method is used to realise the space that is used create the oject
#syntax : __del__
#destructor is called automatically when your entire code execute
#(i.e.end of the program)

class student:
    def __init__(self):
        print("Constructor is called")
    def __def__(self):
        print("Destructor is called")  
        
s=student()


