class A:
    def get(self):
        print("This from class A get method")
    def display(Self):
        print("Inside class A")
class B(A):
    def get(self):
        print("Inside Class B Constructor get method")
        super().get()
    def dis(Self):
        print("Inside the class B")
b=B()
b.get()
