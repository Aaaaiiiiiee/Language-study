class MultipleCalculator():
    def multiply(self):
        return self.v1 * self.v2

class DivideCalculator():
    def divide(self):
        return self.v1 / self.v2


class Calculator(MultipleCalculator, DivideCalculator):
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

c = Calculator(100, 10)
print(c.add())
print(c.multiply())
print(c.divide())