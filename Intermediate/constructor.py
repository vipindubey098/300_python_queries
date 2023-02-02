class Math:
    def __init__(self, v1, v2): #constructor
        self.num1 = v1
        self.num2 = v2

    def arithmetic_op(self):
        print("Addition: "+str(self.num1 + self.num2))
        print("Subtraction: "+str(self.num1 - self.num2))
        print("Multiplication: "+str(self.num1 * self.num2))
        print("Mod: "+str(self.num1 % self.num2))
        print("Division: "+str(self.num1 / self.num2))


a = int(input("Enter a number: "))
b = int(input("Enter b number: "))

obj = Math(a,b)
obj.arithmetic_op()