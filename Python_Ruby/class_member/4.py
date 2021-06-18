class Calculator(object):
    _history = []

    @classmethod
    def history(cls):
        print("---History of the Calculator---")
        for item in Calculator._history:
            print(item)

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
        result = self.v1 + self.v2
        Calculator._history.append("add : %d+%d=%d" % (self.v1, self.v2, result))
        return result
    def subtract(self):
        result = self.v1 - self.v2
        Calculator._history.append("subtract : %d-%d=%d" % (self.v1, self.v2, result))
        return result

class MultipleCalculator(Calculator):
    def multiply(self):
        result = self.v1 * self.v2
        Calculator._history.append("multiply : %d*%d=%d" % (self.v1, self.v2, result))
        return result

class DivideCalculator(MultipleCalculator):
    def divide(self):
        result = self.v1 / self.v2
        Calculator._history.append("divide : %d/%d=%d" % (self.v1, self.v2, result))
        return result

c1 = MultipleCalculator(10, 10)
print('add', c1.add())
print('subtract', c1.subtract())
print('multiply', c1.multiply())

c2 = DivideCalculator(20, 10)
print('add', c2.add())
print('subtract', c2.subtract())
print('multiply', c2.multiply())
print('divide', c2.divide())

Calculator.history()