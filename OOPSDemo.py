#self keyword is mandatory for calling variable names into method
#instane & class variable has whole different purpose
#constructor name should be __init__
# new keyword is not required when you created object


class Calculator:
    num = 100 # class variable

    #defalut constructor
    def __init__(self, a, b): #self object reference
        self.firstNumber=a #instance variable
        self.secondNumber=b #instance variable
        print("Default constructor call automatically when object is created")

    def getData(self):
        print("I am now executing as method in class")

    def Summation(self):
        return self.firstNumber+self.secondNumber+Calculator.num;



obj = Calculator(2, 3) # Syntax to create object in python

obj.getData()
print(obj.Summation())


obj1 = Calculator(4, 5) # Syntax to create object in python

obj1.getData()
print(obj1.Summation())