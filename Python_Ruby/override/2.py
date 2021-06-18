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

    def info(self):
        return "Cal => v1 : %d, v2 : %d" % (self.v1, self.v2)

class MultipleCalculator(Calculator):
    def multiply(self):
        result = self.v1 * self.v2
        Calculator._history.append("multiply : %d*%d=%d" % (self.v1, self.v2, result))
        return result

    def info(self):
        return "MultipleCalculator => %s" % super().info()

class DivideCalculator(MultipleCalculator):
    def divide(self):
        result = self.v1 / self.v2
        Calculator._history.append("divide : %d/%d=%d" % (self.v1, self.v2, result))
        return result

    def info(self):
        return "DivideCalculator => %s" % super().info()

c0 = Calculator(30, 60)
print(c0.info())

c1 = MultipleCalculator(10, 10)
print(c1.info())

c2 = DivideCalculator(20, 10)
print(c2.info())

Calculator.history()