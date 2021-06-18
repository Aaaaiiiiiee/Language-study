class C1(object):
    def c1_m(self):
        print("c1_m")

class C2():
    def c2_m(self):
        print("C2_m")

class C3(C1, C2):
    pass

c = C3()
c.c1_m()
c.c2_m()

print(C3.__mro__)