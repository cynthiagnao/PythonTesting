#Child implementation Class
from OopsDemo import Calculator #from this filename import className


class ChildImplementation(Calculator): #Child class call the Parent class
    num2 = 200

    def __init__(self): #Child constructor must call the Parent constructor
        Calculator.__init__(self,2,10) 

    def getCompleteData(self):
        return self.num2 + self.num + self.Summation()


obj = ChildImplementation()
print(obj.getCompleteData())


