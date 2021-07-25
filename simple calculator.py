
#calculator using classes and functions
print("what function would you like to execute\n")
print("1.add")
print("2.subtract")
print("3.multiply")
print("4.divide")


operation = int(input("which operation would like to excute 1/2/3/4"))
input1 = int(input('enter first number'))
input2 = int(input('enter second number'))

class Calculator:

    def __init__(self,input1,input2):
        self.input1=input1
        self.input2=input2
        
    def multiply(self):
        return self.input1 * self.input2
    
    def divide(self):
        return self.input1/self.input2

    def add(self):
        return self.input1 + self.input2
    
    def subtract(self):
        return self.input1 - self.input1

object=Calculator(input1,input2)

if operation == 1:
    print(object.add())
elif operation == 2:
    print(object.subtract())
elif operation == 3:
    print(object.multiply())
elif operation == 4:
    print(object.divide())
