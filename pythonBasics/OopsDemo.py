# Classes are user defined blueprint or prototype
# Sum, Multiplication, Addition, Constant
# Methods, class variables, instance variables, constructor etc
# objects for you classes

# Self keyword is mandatory for calling variable names into method
# Instance and class variables have whole different purpose
# Constructor name should be __init__
# new keyword is not required when you create object

class Calculator:
    num = 100 #class variables

    #default constructor
    def __init__(self,a,b):
        self.firstNumber = a
        self.secondNumber = b
        print("I am called automatically when object is created")

    def getData(self):
        print("I am now excuting as method in class")

    def Summation(self):
        return self.firstNumber + self.secondNumber + self.num


obj = Calculator(2,3) #syntax to create objects in python
obj.getData() #the object calls the class method "getData()"
print(obj.num)
print(obj.Summation()) #the object calls the class method "Summation()"

obj1 = Calculator(5,7)
obj1.getData()
print(obj1.num)
print(obj1.Summation()) #the object calls the class method "Summation()"



