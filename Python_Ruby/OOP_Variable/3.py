class Calculator(object):
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2

    def setV1(self, v):
        if(isinstance(v, int)):
            self.v1 = v
        else:
            print('You tried changing v1 by not integer')

    def getV1(self):
        return self.v1

    def add(self):
        return self.v1 + self.v2
    def subtract(self):
        return self.v1 - self.v2

c1 = Calculator(10, 10)
print(c1.add())
print(c1.subtract())

c1.setV1(20)
print(c1.add())

c1.setV1('one')
print(c1.add())