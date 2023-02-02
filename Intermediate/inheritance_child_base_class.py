class A:
    name = "abc"
    age = 232
    contact = 23949709
    #above are data members that are declared initialized in the parent class

    def method1(self, course):
        print(course)
        print("This is method of class A")

class B(A):
    city = "Mumbai"

    def method2(self, a, b):
        print(a+b)
        print("This is method of class B")
    
obj = B()
obj.method1("Python")
obj.method2(1,2)