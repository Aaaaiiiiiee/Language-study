class Cs(object):
    count = 0

    def __init__(self):
        Cs.count = Cs.count + 1
    
    @classmethod
    def getCount(cls):
        return Cs.count

i1 = Cs()
i2 = Cs()
i3 = Cs()
i4 = Cs()
print(Cs.getCount())

# method 밖, class 안에 변수를 선언하면 class variable