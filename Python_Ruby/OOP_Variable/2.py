class C(object):
    def __init__(self, value):
        self.value = value

    def setValue(self, value):
        self.value = value

    def getValue(self):
        return self.value
    
    def show(self):
        print(self.value)

c1 = C(10)
print(c1.getValue())

c1.setValue(20)
print(c1.getValue())

c1.show()