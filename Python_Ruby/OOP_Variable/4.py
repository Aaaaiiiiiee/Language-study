class C(object):
    def __init__(self, value):
        self.__value = value

    def show(self):
        print(self.__value)

c1 = C(10)
#print(c1.__value)
c1.show()