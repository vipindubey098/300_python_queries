class destructure:
    def show(self):
        print("This is a function")
    
    def __del__(self):
        print("This is destructure")

obj = destructure()
obj1 = destructure()
obj.show()