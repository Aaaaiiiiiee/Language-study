class C1:
    def m(self):
        return 'parent'

class C2(C1):
    def m(self):
        return super().m() + 'child'
    # pass
    # use this keyword, when you make emtpy class

o = C2()
print(o.m())


# Python에서 super()는 부모 클래스 객체를
# Ruby에서 super()는 부모 클래스의 override한 메소드를 가리킨다.