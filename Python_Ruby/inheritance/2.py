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

class MultipleCalculator(Calculator):
    def multiply(self):
        return self.v1 * self.v2

class DivideCalculator(MultipleCalculator):
    def divide(self):
        return self.v1 / self.v2

c1 = MultipleCalculator(10, 10)
print('add', c1.add())
print('subtract', c1.subtract())
print('multiply', c1.multiply())

c2 = DivideCalculator(20, 10)
print('add', c2.add())
print('subtract', c2.subtract())
print('multiply', c2.multiply())
print('divide', c2.divide())